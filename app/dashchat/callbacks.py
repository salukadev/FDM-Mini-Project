from datetime import datetime as dt
from flask_login import current_user
from app.dashchat.layout import textbox
from transformers import AutoModelWithLMHead, AutoTokenizer
from dash.dependencies import Input, Output, State
import pandas as pd

# Define app
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#server = app.server

# device = "cuda" if torch.cuda.is_available() else "cpu"
qlist = ["What is today's date?", "What month is it?", "What year is it?", "What day of the week is it today?"]

qdata = pd.read_csv("app\questions\alzhimersquiz.csv")

device = "cpu"
print(f"Device: {device}")

print("Start loading model...")
name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(name)
model = "g"
quizno = 0

print("Done.")
chat_history = []


def register_callbacks(dashapp):

    # questionnair modal
    @dashapp.callback(
        Output("modal-centered", "is_open"),
        [Input("open-centered", "n_clicks"),
         Input("close-centered", "n_clicks")],
        [State("modal-centered", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open
    
    #quiz - question
    @dashapp.callback(
        Output(component_id='body-div', component_property='children'),
        Input(component_id='ques', component_property='n_clicks')
    )
    
    def update_output(n_clicks):
        if n_clicks is None:
            return qdata.iloc[0][0]
        else:

            return qdata.iloc[n_clicks][0]
    
    #quiz answer display
    @dashapp.callback(
        Output('output', 'children'),
        [Input('dropdown', 'value')]
        )

    def dropdown(value):
        filtered_df = df[df['c'] == value]
        return filtered_df.iloc[0]['c']

    @dashapp.callback(
        Output("display-conversation",
               "children"), [Input("store-conversation", "data")]
    )
    def update_display(chat_history):
        return [
            #textbox('Saluka', box="self")
            textbox(x, box="self") if i % 2 == 0 else textbox(x, box="other")
            for i, x in enumerate(chat_history)

            # for i, x in enumerate(chat_history.split(tokenizer.eos_token)[:-1])
        ]

    @dashapp.callback(
        [Output("store-conversation", "data"), Output("user-input", "value")],
        [Input("submit", "n_clicks"), Input("user-input", "n_submit")],
        [State("user-input", "value"), State("store-conversation", "data")],
    )
    def run_chatbot(n_clicks, n_submit, user_input, chat_history):
        if n_clicks == 0:
            return "", ""

        if user_input is None or user_input == "":
            return chat_history, ""

        chat_history.append(user_input)

        return chat_history, ""

        # # temporary
        # return chat_history + user_input + "<|endoftext|>" + user_input + "<|endoftext|>", ""

        # encode the new user input, add the eos_token and return a tensor in Pytorch
        bot_input_ids = tokenizer.encode(
            chat_history + user_input + tokenizer.eos_token, return_tensors="pt"
        )

        # generated a response while limiting the total chat history to 1000 tokens,
        chat_history_ids = model.generate(
            bot_input_ids, max_length=1024, pad_token_id=tokenizer.eos_token_id
        )
        chat_history = tokenizer.decode(chat_history_ids[0])

        return chat_history, ""

