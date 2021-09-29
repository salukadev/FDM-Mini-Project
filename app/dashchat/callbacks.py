from datetime import datetime as dt

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

quiz = pd.read_csv('app/questions/COVIDquiz.csv')
q_count = 0


def register_callbacks(dashapp):
    @dashapp.callback(
        Output("display-conversation", "children"), [Input("store-conversation", "data")]
    )
    def update_display(chat_history):
        return [
            textbox(x, box="self") if (i % 2 == 0 or i <= 2) else textbox(x, box="other")
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
        [State("store-conversation", "data"), State('onload_delay', 'disabled')]
    )
    def on_load(d, v, f):
        print("Loading complete")
        print(d, v, f)
        v.append('Hi! Welcome to our service')
        v.append('You have to provide some information for testing')
        v.append('Do you like to continue ?')
        return v, ""

# def ask(question, valid):
