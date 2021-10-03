import datetime

import pandas as pd
from flask_login import current_user
from app.dashchat.layout import textbox
# from transformers import AutoModelWithLMHead, AutoTokenizer
# from dash.dependencies import Input, Output, State
import pandas
from dash_extensions.enrich import Output, Input, State

# name = "microsoft/DialoGPT-medium"
# tokenizer = AutoTokenizer.from_pretrained(name)
# model = "g"

current_time = datetime.datetime.now() 

quiz = pd.read_csv('app/questions/COVIDquiz.csv')
qdata = pd.read_csv('app/questions/alzhimersquiz.csv')
q_count = 0


def register_callbacks(dashapp):

    # questionnair modal
    @dashapp.callback(
        [Output("modal-centered", "is_open"),
         Output(component_id='body-div', component_property='children')],
        [Input("open-centered", "n_clicks"),
         Input("close-centered", "n_clicks")],
        [State("modal-centered", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open, qdata.iloc[0][0]
        return is_open,

    #quiz - question
    @dashapp.callback(
        [Output('body-div', 'children'), Output('score', "data"), Output('quizinput', "value"), Output('img_watch','style'), Output('img_watch','src'),Output('score_output','children'), Output('quizinput', "style")],
        Input('nextbutton', 'n_clicks'),
        [State('quizinput', "value"), State('score', "data")]
    )
    def update_output(n_clicks, value, score,):
                

        if n_clicks == 1:
            print(score)
            if value == str(current_time.day):
                return "What month is it?", score + 1, '', {'display': 'none'}, '','', {'display': 'block'}
            else:
                return "What month is it?", score + 0, '', {'display': 'none'}, '','', {'display': 'block'}
        
        if n_clicks == 2:
            print(score)
            if value == str(current_time.month) or value.lower() == str(current_time.strftime("%B")).lower() or value.lower() == str(current_time.strftime("%b")).lower():
                return "What year is it?", score + 1, '', {'display': 'none'}, '','', {'display': 'block'}
            else:
                return "What year is it?", score + 0, '', {'display': 'none'}, '','', {'display': 'block'}

        if n_clicks == 3:
            print(score)
            if value == str(current_time.year):
                return "What day of the week is it today?", score + 1, '', {'display': 'none'}, '','', {'display': 'block'}
            else:
                return "What day of the week is it today?", score + 0, '', {'display': 'none'}, '','', {'display': 'block'}

        if n_clicks == 4:
            print(score)
            if value == str(current_time.weekday()) or value.lower() == current_time.strftime('%A').lower() or  value.lower() == current_time.strftime('%A').lower():
                return "What time is it now to nearest hour? Example: 8", score + 1, '', {'display': 'none'}, '','', {'display': 'block'}
            else:
                return "What time is it now to nearest hour Example: 8",score +  0, '', {'display': 'none'}, '','', {'display': 'block'}

        #fix fix fix answer check
        if n_clicks == 5: 
            print(score)
            if value == str(current_time.weekday()):
                return "What is the name of this site?", score + 1, '', {'display': 'none'}, '','', {'display': 'block'}
            else:
                return "What is the name of this site?", score + 0, '',{'display': 'none'}, '','', {'display': 'block'}
        
        if n_clicks == 6:
            print(score)
            if value == 'mmse':
                return "Remember these words: Ball Car Tree     I'll ask you later", score + 1, '', {'display': 'none'}, '','', {'display': 'none'}
            else:
                return "Remember these words: Bill Car Tree     I'll ask you later", score + 0, '', {'display': 'none'}, '','', {'display': 'none'}

        if n_clicks == 7:
            print(score)
            if value == 'qer' :
                return "If you start at 100,and count backwards by 7. What is the number after 5 subtractions?", score + 0, '', {'display': 'none'}, '','', {'display': 'block'}
            else:
                return "If you start at 100,and count backwards by 7. What is the number after 5 subtractions?", score + 0, '',{'display': 'none'}, '','', {'display': 'block'}
        if n_clicks == 8:
            print(score)
            if value == str(65):
                return "What are the words mentioned before?", score + 5, '', {'display': 'none'}, '','', {'display': 'block'}
            else:
                return "What are the words mentioned before?", score + 0, '', {'display': 'none'}, '','', {'display': 'block'}

        if n_clicks == 9:
            print(score)
            li = value.lower().split()
            if "ball" in li:
                return "What is this object?", score + 2, '',  {'display': 'block'}, '../static/images/watch.jpg','', {'display': 'block'}
            if 'tree' in li:
                return "What is this object?", score + 2, '',  {'display': 'block'}, '../static/images/watch.jpg','', {'display': 'block'}
            if 'car' in li:
                return "What is this object?", score + 2, '',  {'display': 'block'}, '../static/images/watch.jpg','', {'display': 'block'}
            else:
                return "What is this object?",score +  0, '', {'display': 'block'}, '../static/images/watch.jpg','', {'display': 'block'}
        
        if n_clicks == 10:
            print(score)
            if value == 'watch' or value == 'wrist watch':
                return "What is this object?",score +  1, '', {'display': 'block'}, '../static/images/pen3.jpg','', {'display': 'block'}
            else:
                return "What is this object?", score + 0, '', {'display': 'block'}, '../static/images/pen3.jpg','', {'display': 'block'}

        if n_clicks == 11:
            print(score)
            if value.lower() == 'ball pen' or value.lower() == 'pen':
                return "Remember the Sentence below", score + 1, '', {'display': 'block'}, '../static/images/sentence.jpg','', {'display': 'none'}
            else:
                return "Remember the Sentence below", score + 0, '', {'display': 'block'}, '../static/images/sentence.jpg','', {'display': 'none'}

        if n_clicks == 12:
            print(score)
            return "Repeat the sentence", score + 0, '', {'display': 'none'}, '','', {'display': 'block'}

        if n_clicks == 13:
            print(score)
            if value.lower() == 'no ifs ands or buts':
                return "What is the number written in the box in your right?",score +  2, '', {'display': 'block'}, '../static/images/leftright.jpg','', {'display': 'block'}
            else:
                return "What is the number written in the box in your right?",score +  0, '', {'display': 'block'}, '../static/images/leftright.jpg','', {'display': 'block'}
        
        if n_clicks == 14:
            print(score)
            if value == '23':
                return "What is the shape that is similar to the intersection of two shapes in the image?",score +  1, '', {'display': 'block'}, '../static/images/shapes.jpg','', {'display': 'block'}
            else:
                return "What is the shape that is similar to the intersection of two shapes in the image?",score +  0, '', {'display': 'block'}, '../static/images/shapes.jpg','', {'display': 'block'}

        if n_clicks == 15:
            print(score)
            if value == 'B':
                return "What is the correct output when the first shape is flipped horizontaly?", score + 2, '', {'display': 'block'}, '../static/images/spatial.jpg',''
            else:
                return "What is the correct output when the first shape is flipped horizontaly?", score + 0, '', {'display': 'block'}, '../static/images/spatial.jpg',''
        
        if n_clicks == 16:
            print(score)
            if value == 'D':
                return "What are the correct words to fill the blanks?", score + 1, '', {'display': 'block'}, '../static/images/complete.jpg','', {'display': 'block'}
            else:
                return "What are the correct words to fill the blanks?", score, '', {'display': 'block'}, '../static/images/complete.jpg','', {'display': 'block'}

        if n_clicks == 17:
            print(score)
            li2 = value.lower().split()
            if 'sitting' in li2:
                return "What is a rotation of the first object?", score + 1, '', {'display': 'block'}, '../static/images/rotation.jpg','', {'display': 'block'}
            if 'bench' in li2:
                return "What is a rotation of the first object?",score +  1, '', {'display': 'block'}, '../static/images/rotation.jpg','', {'display': 'block'}
            else:
                return "What is a rotation of the first object?", score , '', {'display': 'block'}, '../static/images/rotation.jpg','', {'display': 'block'}
        if n_clicks == 18:
            print(score)
            li2 = value.lower().split()
            if value.upper() == 'B':
                return "Type 'Hello world' to continue", score + 2, '', {'display': 'none'}, '','', {'display': 'block'}
            else:
                return "Type 'Hello world' to continue", score, '', {'display': 'none'}, '','', {'display': 'block'}

        if n_clicks == 19:
            print(score)
            li2 = value.lower().split()
            if value.lower() == 'hello world':
                return "Test Completed", score , '', {'display': 'none'}, '',score, {'display': 'none'}
            else:
                return "Test Completed' to continue", score , '', {'display': 'none'}, '',score, {'display': 'none'}
 
 

    @dashapp.callback(
        Output("display-conversation",
               "children"), [Input("store-conversation", "data")]
    )
    def update_display(chat_history):
        return [
            textbox(x, box="self") if (i %
                                       2 == 0 or i <= 2) else textbox(x, box="other")
            for i, x in enumerate(chat_history)
        ]

    @dashapp.callback(
        [Output("store-conversation", "data"), Output("user-input", "value"), Output("store-qcount", "data"),
         Output("store-ans", "data")],
        [Input("submit", "n_clicks"), Input("user-input", "n_submit")],
        [State("user-input", "value"), State("store-conversation", "data"), State("store-qcount", "data"),
         State("store-ans", "data")]
    )
    def run_chatbot(n_clicks, n_submit, user_input, chat_history, qcount, ans):

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
        if (not (user_input.isnumeric()) ^ (quiz.loc[qcount - 1]['type'] == 'str') or
                user_input.isnumeric() ^ (quiz.loc[qcount - 1]['type'] == 'int')):
            chat_history.append("Please input a valid answer")

            return chat_history, "", qcount, ans

        ans.append(user_input)

        if qcount == len(quiz):
            print("Questionnaire completed!")
            print(ans)
            chat_history.append("Questionnaire completed!")
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
         State('onload_delay', 'disabled')]
    )
    def on_load(d, v, f):
        print("Loading complete")
        print(d, v, f)
        v.append('Hi! Welcome to our service')
        v.append('You have to provide some information for testing')
        v.append('Do you like to continue ?')
        return v, ""

# def ask(question, valid):
