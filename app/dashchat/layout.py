import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

def textbox(text, box="other"):
    style = {
        "max-width": "55%",
        "width": "max-content",
        "padding": "10px 15px",
        "border-radius": "15px",
        "margin-bottom": "5px"
    }

    if box == "self":
        style["margin-left"] = "auto"
        style["margin-right"] = 0

        color = "primary"
        inverse = True

    elif box == "other":
        style["margin-left"] = 0
        style["margin-right"] = "auto"

        color = "light"
        inverse = False

    else:
        raise ValueError("Incorrect option for `box`.")

    return dbc.Card(text, style=style, body=True, color=color, inverse=inverse)

conversation = html.Div( style={
        "width": "80%",
        "max-width": "800px",
        "height": "78vh",
        "margin": "auto",
        "overflow-y": "auto",
        "padding": "10px 5px",
    },
    id="display-conversation",)

controls = dbc.InputGroup(
    style={"width": "80%", "max-width": "800px", "margin": "auto"},
    children=[
        dbc.Input(id="user-input", placeholder="Write to the chatbot...", type="text"),
        dbc.InputGroupAddon(dbc.Button("Submit", id="submit"), addon_type="append",),
    ],
)

# Define Layout
layout = dbc.Container(
    fluid=True,
    children=[
        html.H1("Chatbot", style={"margin": "auto","text-align" : "center"}),
        html.Hr(),
        dcc.Store(id="store-conversation", data=[]),
        dcc.Store(id="store-qcount", data=0),
        dcc.Store(id="store-ans", data=[]),
        dcc.Location(id='url', refresh=False),
        conversation,
        controls,
        dcc.Interval(
            id='onload_delay',
            max_intervals=1,
            interval=1*1000, # in milliseconds
            n_intervals=0)
    ],
)