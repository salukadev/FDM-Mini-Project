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


conversation = html.Div(style={
    "width": "80%",
    "max-width": "800px",
    "height": "78vh",
    "margin": "auto",
    "overflow-y": "auto",
    "padding": "10px 5px",
},
    id="display-conversation",)

quizmodal = html.Div(
    [
        dbc.Button("Open", id="open-centered"),
        dbc.Modal(
            [
                dbc.ModalHeader("Header123"),
                dbc.ModalBody(

                    html.Div([
                        html.Div(id='body-div'),

                        html.Br(),
                        html.Div(
                            [html.Img(
                                id="img_watch",
                                src='',
                                height = '200px',
                                width = '300px',
                                style={'height': '10 rem', 'width': '10 rem', 'display': 'none'})
                             ], style={'max-height': '20rem',
                                       'max-width': '20rem',
                                       'height':'auto',
                                       'width':'auto', 
                                       'display': 'block', 
                                       'justifyContent': 'center',
                                       'object-fit': 'fill'}
                        ),

                        dbc.Input(id="quizinput",
                                  placeholder="Type something...", type="text"),

                        html.H4(id='score_output'),
                        html.Br(),
                        html.Button('Next', id='nextbutton', n_clicks=0,),

                    ]),
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

        ),
    ]
)

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
        html.H1("Chatbot", style={"margin": "auto", "text-align": "center"}),
        html.Hr(),
        dcc.Store(id="store-conversation", data=[]),
        dcc.Store(id="store-qcount", data=0),
        dcc.Store(id="store-ans", data=[]),
        dcc.Store(id="quizcount", data=0),
        dcc.Store(id="score", data=0),
        quizmodal,
        conversation,
        controls,
        dcc.Interval(
            id='onload_delay',
            max_intervals=1,
            interval=1*1000,  # in milliseconds
            n_intervals=0)
    ],
)
