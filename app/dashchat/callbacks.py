from datetime import datetime as dt
from flask_login import current_user
from app.dashchat.layout import textbox
from transformers import AutoModelWithLMHead, AutoTokenizer
from dash.dependencies import Input, Output, State
import torch

# Define app
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#server = app.server

# device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"
print(f"Device: {device}")

print("Start loading model...")
name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(name)
model = "g"



print("Done.")

def register_callbacks(dashapp):
    @dashapp.callback(
        Output("display-conversation", "children"), [Input("store-conversation", "data")]
    )
    def update_display(chat_history):
        return [
            textbox(x, box="self") if i % 2 == 0 else textbox(x, box="other")
            for i, x in enumerate(chat_history.split(tokenizer.eos_token)[:-1])
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