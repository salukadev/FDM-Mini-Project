import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State


def textbox(text, box="other"):
    style = {
        "max-width": "55%",
        "width": "max-content",
        "padding": "10px 15px",
        "border-radius": "25px",
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


# questionnair modal
modal = html.Div(
    [
        dbc.Button("Open", id="open-centered"),
        dbc.Modal(
            [
                dbc.ModalHeader("Header123"),
                dbc.ModalBody(

                    html.Div([
                        html.Div(id='body-div'),
                        dcc.Dropdown(
                                id='dropdown',
                                options=[
                                    {'label':i, 'value':i} for i in df['c'].unique()
                                ],
                            ),
                        html.Div(id='output'),
                        html.Button('Next',
                                    id='ques'),
                       
                    ])
                ),
                dbc.ModalFooter(

                    dbc.Button(
                        "Close",
                        id="close-centered",
                        className="ml-auto",
                        n_clicks=0,
                    )

                ),
            ],
            id="modal-centered",
            centered=True,
            is_open=False,
        ),
    ]
)


conversation = html.Div(style={
    "width": "80%",
    "max-width": "800px",
    "height": "70vh",
    "margin": "auto",
    "overflow-y": "auto",
},
    id="display-conversation",)

controls = dbc.InputGroup(
    style={"width": "80%", "max-width": "800px", "margin": "auto"},
    children=[
        dbc.Input(id="user-input",
                  placeholder="Write to the chatbot...", type="text"),
        dbc.InputGroupAddon(dbc.Button(
            "Submit", id="submit"), addon_type="append",),
    ],
)


# Define Layout
layout = dbc.Container(
    fluid=True,
    children=[
        html.H1("Dash Chatbot (with DialoGPT)"),
        html.Hr(),
        dcc.Store(id="store-conversation", data=""),
        modal,
        conversation,
        controls,
    ],
)
