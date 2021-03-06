import datetime
import plotly.express as px
import pandas as pd
import numpy as np
import pickle
from flask_login import current_user
from app.dashchat.layout import textbox, mmse_btn
# from transformers import AutoModelWithLMHead, AutoTokenizer
# from dash.dependencies import Input, Output, State
import pandas
from dash_extensions.enrich import Output, Input, State
from sklearn.cluster import KMeans

# name = "microsoft/DialoGPT-medium"
# tokenizer = AutoTokenizer.from_pretrained(name)
# model = "g"

current_time = datetime.datetime.now()

q_covid = pd.read_csv('app/questions/COVIDquiz.csv')
q_alz = pd.read_csv('app/questions/Alz.csv')
qdata = pd.read_csv('app/questions/alzhimersquiz.csv')
q_count = 0

print("Loading models....")
# covid-19 models
tree1 = pickle.load(open("app/models/covid/covid1.sav", 'rb'))
tree2 = pickle.load(open("app/models/covid/covid2.sav", 'rb'))
tree3 = pickle.load(open("app/models/covid/covid3.sav", 'rb'))

# alzheimer models
model = pickle.load(open("app/models/alz/alz.sav", 'rb'))
print("Model loading completed")


def register_callbacks(dashapp):
    # questionnair modal
    @dashapp.callback(
        [Output("modal-centered", "is_open"),
         Output(component_id='body-div', component_property='children')],
        Input("open-centered", "n_clicks"),

        [State("modal-centered", "is_open")],
    )
    def toggle_modal(n1,  is_open):
        print(is_open)
        if n1:
            return True, qdata.iloc[0][0]
        return False, " "

    @dashapp.callback([Output("user-input", "value"), Output("modal-centered", "is_open")], Input("close-centered", "n_clicks"), State('score', "data"))
    def fill_mmse(n, score):
        print("Closing modal..")
        return str(score), False

    # Update conversation
    @dashapp.callback(
        Output("display-conversation",
               "children"), [Input("store-conversation", "data")]
    )
    def update_display(chat_history):
        # if chat_history[-1] == 'MMSE':
        #     return mmse_btn()
        # return [
        #     textbox(x, box="self") if (i %
        #                                2 == 0 or i <= 2) else textbox(x, box="other")
        #     for i, x in enumerate(chat_history)
        # ]

        l = []
        for i, x in enumerate(chat_history):
            if x == 'MMSE':
                l.append(mmse_btn())
            elif i % 2 == 0 or i <= 2:
                l.append(textbox(x, box="self"))
            else:
                l.append(textbox(x, box="other"))
        return l

    @dashapp.callback(
        [Output("store-conversation", "data"), Output("user-input", "value"), Output("store-qcount", "data"),
         Output("store-ans", "data")],
        [Input("submit", "n_clicks"), Input("user-input", "n_submit")],
        [State("user-input", "value"), State("store-conversation", "data"), State("store-qcount", "data"),
         State("store-ans", "data"), State('url', 'pathname')]
    )
    def run_chatbot(n_clicks, n_submit, user_input, chat_history, qcount, ans, url):
        # Check chatbot type
        t = 0
        quiz = q_alz
        if "covid" in url.lower():
            t = 1
            quiz = q_covid

        if qcount == -1:
            return chat_history, "Refresh to attempt again", -1, []

        if n_clicks == 0:
            return "", "", 0, []

        if user_input is None or user_input == "":
            return chat_history, "", 0, []

        chat_history.append(user_input)

        # User confirmation and the first question
        if qcount == 0:
            if user_input.lower() != 'yes':
                chat_history.append('Thank you')
                return chat_history, "", -1, []
            else:
                q = quiz.loc[qcount]['question']
                chat_history.append(q)
                qcount += 1
                return chat_history, "", qcount, ans

        # print(not(user_input.isnumeric()) ^ (quiz.loc[qcount - 1]['type'] == 'str'))
        # print(user_input.isnumeric() ^ (quiz.loc[qcount - 1]['type'] == 'int'))

        # User input validation
        if (not (user_input.replace('.', '', 1).isnumeric()) ^ (quiz.loc[qcount - 1]['type'] == 'str') or
                user_input.replace('.', '', 1).isnumeric() ^ (quiz.loc[qcount - 1]['type'] == 'int')):
            chat_history.append("Please input a valid answer")

            return chat_history, "", qcount, ans

        # Check all strings for 'yes' & 'no'
        if not user_input.replace('.', '', 1).isnumeric():
            if not (user_input.lower() == 'yes' or user_input.lower() == 'no'):
                chat_history.append("Answer is not clear. Please input again")
                return chat_history, "", qcount, ans

        # Input encoding
        encoded = ''
        if user_input.lower() == 'yes':
            encoded = 1
        elif user_input.lower() == 'no':
            encoded = 0
        else:
            encoded = float(user_input)
        ans.append(encoded)

        if qcount == len(quiz):
            print("Questionnaire completed!")
            print(ans)
            chat_history.append("Questionnaire completed!")
            if t == 1:
                rslt = predict_covid(ans)
                if rslt == 1:
                    rslt = "High probability"
                else:
                    rslt = "Low probability"
                print("Results : ", rslt)
                chat_history.append(rslt)
            else:
                rslt = predict_alz(ans)
                if rslt == 0:
                    rslt = "Converted"
                elif rslt == 1:
                    rslt = "Non-demented"
                else:
                    rslt = "Demented"
                print("Results : ", rslt)
                chat_history.append(rslt)
            return chat_history, "", qcount, ans

        q = quiz.loc[qcount]['question']
        chat_history.append(q)
        qcount += 1
        return chat_history, "", qcount, ans

    # Executed after page loading
    @dashapp.callback(
        Output("store-conversation", "data"), Output("user-input", "value"),
        [Input('onload_delay', 'n_intervals')],
        [State("store-conversation", "data"),
         State('onload_delay', 'disabled'), State('url', 'pathname')]
    )
    def on_load(d, v, f, url):
        if "covid" in url.lower():
            print("Covid application")
        print("Loading complete")
        print(d, v, f)
        v.append('Hi! Welcome to our service')
        v.append('You have to provide some information for testing')
        v.append('Do you like to continue ?')
        return v, ""

    # @dashapp.callback(Output("user-input", "value"), Input('url', 'pathname'))
    # def test(s):
    #     print(type(s))
    #     return ""

    # quiz - question
    @dashapp.callback(
        [Output('body-div', 'children'), Output('score', "data"), Output('quizinput', "value"),
         Output('img_watch', 'style'), Output('img_watch',
                                              'src'), Output('score_output', 'children'),
         Output('quizinput', "style")],
        Input('nextbutton', 'n_clicks'),
        [State('quizinput', "value"), State('score', "data")]
    )
    def update_output(n_clicks, value, score, ):
        if n_clicks == 1:
            print(score)
            if value == str(current_time.day):
                return "What month is it?", score + 1, '', {'display': 'none'}, '', '', {'display': 'block'}
            else:
                return "What month is it?", score + 0, '', {'display': 'none'}, '', '', {'display': 'block'}

        if n_clicks == 2:
            print(score)
            if value == str(current_time.month) or value.lower() == str(
                current_time.strftime("%B")).lower() or value.lower() == str(
                    current_time.strftime("%b")).lower():
                return "What year is it? Ex:1992", score + 1, '', {'display': 'none'}, '', '', {'display': 'block'}
            else:
                return "What year is it? Ex:1992", score + 0, '', {'display': 'none'}, '', '', {'display': 'block'}

        if n_clicks == 3:
            print(score)
            if value == str(current_time.year):
                return "What day of the week is it today? Ex: Sunday", score + 1, '', {'display': 'none'}, '', '', {
                    'display': 'block'}
            else:
                return "What day of the week is it today? Ex: Sunday", score + 0, '', {'display': 'none'}, '', '', {
                    'display': 'block'}

        if n_clicks == 4:
            print(score)
            if value == str(current_time.weekday()) or value.lower() == current_time.strftime(
                    '%A').lower() or value.lower() == current_time.strftime('%A').lower():
                return "What time is it now to nearest hour? Example: 8", score + 1, '', {
                    'display': 'none'}, '', '', {'display': 'block'}
            else:
                return "What time is it now to nearest hour Example: 8", score + 0, '', {
                    'display': 'none'}, '', '', {'display': 'block'}

        # fix fix fix answer check
        if n_clicks == 5:
            print(score)
            if value == str(current_time.weekday()):
                return "What is the name of this site?", score + 1, '', {'display': 'none'}, '', '', {
                    'display': 'block'}
            else:
                return "What is the name of this site?", score + 0, '', {'display': 'none'}, '', '', {
                    'display': 'block'}

        if n_clicks == 6:
            print(score)
            if value == 'mmse':
                return "Remember these words: Ball Car Tree     I'll ask you later", score + 1, '', {
                    'display': 'none'}, '', '', {'display': 'none'}
            else:
                return "Remember these words: Bill Car Tree     I'll ask you later", score + 0, '', {
                    'display': 'none'}, '', '', {'display': 'none'}

        if n_clicks == 7:
            print(score)
            if value == 'qer':
                return "If you start at 100,and count backwards by 7. What is the number after 5 subtractions?", score + 0, '', {
                    'display': 'none'}, '', '', {'display': 'block'}
            else:
                return "If you start at 100,and count backwards by 7. What is the number after 5 subtractions?", score + 0, '', {
                    'display': 'none'}, '', '', {'display': 'block'}
        if n_clicks == 8:
            print(score)
            if value == str(65):
                return "What are the words mentioned before?", score + 5, '', {'display': 'none'}, '', '', {
                    'display': 'block'}
            else:
                return "What are the words mentioned before?", score + 0, '', {'display': 'none'}, '', '', {
                    'display': 'block'}

        if n_clicks == 9:
            print(score)
            li = value.lower().split()
            if "ball" in li:
                return "What is this object?", score + 2, '', {
                    'display': 'block'}, '../static/images/watch.jpg', '', {'display': 'block'}
            if 'tree' in li:
                return "What is this object?", score + 2, '', {
                    'display': 'block'}, '../static/images/watch.jpg', '', {'display': 'block'}
            if 'car' in li:
                return "What is this object?", score + 2, '', {
                    'display': 'block'}, '../static/images/watch.jpg', '', {'display': 'block'}
            else:
                return "What is this object?", score + 0, '', {
                    'display': 'block'}, '../static/images/watch.jpg', '', {'display': 'block'}

        if n_clicks == 10:
            print(score)
            if value == 'watch' or value == 'wrist watch':
                return "What is this object?", score + 1, '', {
                    'display': 'block'}, '../static/images/pen3.jpg', '', {'display': 'block'}
            else:
                return "What is this object?", score + 0, '', {
                    'display': 'block'}, '../static/images/pen3.jpg', '', {'display': 'block'}

        if n_clicks == 11:
            print(score)
            if value.lower() == 'ball pen' or value.lower() == 'pen':
                return "Remember the Sentence below", score + 1, '', {
                    'display': 'block'}, '../static/images/sentence.jpg', '', {'display': 'none'}
            else:
                return "Remember the Sentence below", score + 0, '', {
                    'display': 'block'}, '../static/images/sentence.jpg', '', {'display': 'none'}

        if n_clicks == 12:
            print(score)
            return "Repeat the sentence", score + 0, '', {'display': 'none'}, '', '', {'display': 'block'}

        if n_clicks == 13:
            print(score)
            if value.lower() == 'no ifs ands or buts':
                return "What is the number written in the box in your right?", score + 2, '', {'display': 'block'}, '../static/images/leftright.jpg', '', {'display': 'block'}
            else:
                return "What is the number written in the box in your right?", score + 0, '', {'display': 'block'}, '../static/images/leftright.jpg', '', {'display': 'block'}

        if n_clicks == 14:
            print(score)
            if value == '23':
                return "What is the shape that is similar to the intersection of two shapes in the image?", score + 1, '', {'display': 'block'}, '../static/images/shapes.jpg', '', {'display': 'block'}
            else:
                return "What is the shape that is similar to the intersection of two shapes in the image?", score + 0, '', {'display': 'block'}, '../static/images/shapes.jpg', '', {'display': 'block'}

        if n_clicks == 15:
            print(score)
            if value == 'B':
                return "What is the correct output when the first shape is flipped horizontaly?", score + 2, '', {'display': 'block'}, '../static/images/spatial.jpg', ''
            else:
                return "What is the correct output when the first shape is flipped horizontaly?", score + 0, '', {'display': 'block'}, '../static/images/spatial.jpg', ''

        if n_clicks == 16:
            print(score)
            if value == 'D':
                return "What are the correct words to fill the blanks?", score + 1, '', {'display': 'block'}, '../static/images/complete.jpg', '', {'display': 'block'}
            else:
                return "What are the correct words to fill the blanks?", score, '', {'display': 'block'}, '../static/images/complete.jpg', '', {'display': 'block'}

        if n_clicks == 17:
            print(score)
            li2 = value.lower().split()
            if 'sitting' in li2:
                return "What is a rotation of the first object?", score + 1, '', {'display': 'block'}, '../static/images/rotation.jpg', '', {'display': 'block'}
            if 'bench' in li2:
                return "What is a rotation of the first object?", score + 1, '', {'display': 'block'}, '../static/images/rotation.jpg', '', {'display': 'block'}
            else:
                return "What is a rotation of the first object?", score, '', {'display': 'block'}, '../static/images/rotation.jpg', '', {'display': 'block'}

        if n_clicks == 18:
            print(score)

            li2 = value.lower().split()
            if value.upper() == 'B':
                return "Type 'Hello world' to continue", score + 2, '', {'display': 'none'}, '', '', {'display': 'block'}
            else:
                return "Type 'Hello world' to continue", score, '', {'display': 'none'}, '', '', {'display': 'block'}

        if n_clicks == 19:
            print(score)
            li2 = value.lower().split()
            if value.lower() == 'hello world':
                return "Test Completed", score, '', {'display': 'none'}, '', score, {'display': 'none'}
            else:
                return "Test Completed", score, '', {'display': 'none'}, '', score, {'display': 'none'}

    @dashapp.callback([Output("cluster-plot", "figure"), Output('rslt_txt', 'children'), Output('cat_txt', 'children'), Output("modal-result", "is_open"), Output('graph-container', 'style')], Input("store-ans", "data"), State('url', 'pathname'))
    def show_output(ans, url):
        if ("covid" in url.lower()) and len(ans) == 5:
            rslt = predict_covid(ans)
            if rslt == 1:
                rslt = "High probability of covid-19 infection"
            else:
                rslt = "Low probability of covid-19 infection"
            return "", rslt, "", True, {'display': 'none'}
        elif len(ans) == 9:
            rslt = predict_alz(ans)
            if rslt == 0:
                rslt = "Converted"
            elif rslt == 1:
                rslt = "Non-demented"
            else:
                rslt = "Demented"

            sct, clster = show_scatter(ans)
            cls = " *Patient's category(cluster) is {}".format(clster)
            return sct, rslt, cls, True, {'display': 'block'}
        else:
            return "", "", "", False, {'display': 'none'}

    @dashapp.callback(Output("sidebarImg", "src"), Output("sidebarTxt", "children"), Output("sidetitle", "children"), Output("rw1", "children"), Output("rw2", "children"), Output("rw3", "children"), Output("rw4", "children"), Input('url', 'pathname'))
    def getpath(url):
        print(url)
        # chatbot type
        t = 0
        sideImg = '../static/images/mental.png'
        sideTxt = ''
        sideTitle = 'Alzhimers'
        siderw1 = 'Three quarters of people with dementia have not received a diagnosis'
        siderw2 = 'Over 10 millions of new cases of Dimentia reported each year worldwide'
        siderw4 = 'Global annual cost of Dimentia is above US$ 1.3 trillion '
        siderw3 = 'Global annual cost of Dimentia expected to rise to US$ 2.8 trillion by 2050'

        if 'covid' in url.lower():
            t = 1
            #quiz = q_covidfl
            sideImg = '../static/images/covid.png'
            sideTitle = 'COVID-19'
            sideTxt = ''
            siderw1 = 'Total reported cases : 235 537 526'
            siderw2 = 'New Cases : +140 752'
            siderw4 = 'Total Deaths : 4 813 806 '
            siderw3 = 'Total Recovered : 212 398 206'
        return sideImg, sideTxt, sideTitle, siderw1, siderw2, siderw3, siderw4


def predict_covid(ans):
    # age,fever temp,body pain,runny nose, diff breath
    j = np.array(ans[0:2])  # age,bodypain
    k = np.array(ans[2:5])  # fever,runny,diffBreath
    print(j, k)
    y_pred1 = tree1.predict(j.reshape(1, 2))
    y_pred2 = tree2.predict(k.reshape(1, 3))

    XL = np.array([y_pred1[0], y_pred2[0]])
    XL = np.append(j, XL, axis=0)
    XL = np.append(k, XL, axis=0)
    XL = pd.DataFrame(XL.reshape(1, 7))

    y_out = tree3.predict(XL)
    return y_out[0]


def predict_alz(ans):
    # sex,age,educ, ses, mmse, cdr, eyiv, mwbv, asf
    ds = np.array([ans[1], ans[0], ans[2], ans[3],
                  ans[8], ans[4], ans[5], ans[6], ans[7]])
    y = model.predict(ds.reshape(1, 9))
    return y[0]


def show_scatter(rslt):
    data = pd.read_csv('app/datasets/alzheimer.csv')
    data = data.dropna()
    data["M/F"].replace({"M": 1}, inplace=True)
    data["M/F"].replace({"F": 0}, inplace=True)

    # Divide into labels and data
    X = data.drop("Group", axis=1)
    y = data["Group"]

    # Select features
    x = X[['CDR', 'MMSE', 'ASF']].copy()
    kmeans = KMeans(3)
    kmeans.fit(x)

    # Predict on user data
    h = np.array([0.5, 23.0, 0.7])
    ic = kmeans.predict(h.reshape(1, 3))

    # Output cluster info for existing data
    kdata = kmeans.fit_predict(x)
    fig = px.scatter_3d(x, x='CDR', y='MMSE', z='ASF',
                        color=kdata)
    return fig, ic[0]
