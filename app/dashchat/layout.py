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

        color = "#00407d"
        inverse = True

    elif box == "other":
        style["margin-left"] = 0
        style["margin-right"] = "auto"

        color = "rgb(0,64,125, 0.5)"
        inverse = False

    else:
        raise ValueError("Incorrect option for `box`.")

    return dbc.Card(text, style=style, body=True, color=color, inverse=inverse)

def mmse_btn():
    style = {
        "max-width": "55%",
        "width": "max-content",
        "padding": "10px 15px",
        "border-radius": "15px",
        "margin-bottom": "5px"
    }

    style["margin-left"] = "auto"
    style["margin-right"] = 0

    color = "primary"
    inverse = True

    return dbc.Card(dbc.Button("Take Quiz", id="open-centered",color=color), style=style, body=True, color=color, inverse=inverse)


conversation = html.Div(style={
    'background-color': 'rgba(225, 232, 242, 0.4)',
    #'background-image': 'url("../static/images/dna.png")',
    # 'opacity': '0.5',
    'display': 'block',
    #'background-size': 'fit',
    #'background-repeat': 'no-repeat',
    #'background-size': '300px 50px',
    'padding-top': "2rem",
    'padding-left': "3rem",
    'padding-right': "3rem",
    'margin-bottom': "1.75 rem",
    "width": "80%",
    "max-width": "800px",
    "height": "78vh",
    "margin": "auto",
    "overflow-y": "auto",
    "padding": "10px 5px",
    'border': '2px solid #e1e8f2',
    'border-radius': '15px',
    '-moz-border-radius': '15px',
},
    id="display-conversation",)

quizmodal = html.Div(
    [
        # dbc.Button("Open", id="open-centered"),
        dbc.Modal(
            [
                dbc.ModalHeader("Mini Mental State Quiz"),
                dbc.ModalBody(

                    html.Div([
                        html.Div(id='body-div'),

                        html.Br(),
                        html.Div(
                            [html.Img(
                                id="img_watch",
                                src='',
                                height='200px',
                                width='200px',
                                style={'height': '10 rem', 'width': '10 rem', 'display': 'none'})
                             ], style={'max-height': '20rem',
                                       'max-width': '20rem',
                                       'height': 'auto',
                                       'width': 'auto',
                                       'display': 'block',
                                       'justifyContent': 'center',
                                       'align': 'center',
                                       'object-fit': 'contain'}
                        ),

                        dbc.Input(id="quizinput",
                                  placeholder="Type answer...", type="text"),
                        html.Div([html.H4(id='score_output')],
                                 style={"text-align": 'center'}),

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
            backdrop="static",
        ),
    ]
)

resultmodal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader("Results"),
                dbc.ModalBody(
                    html.Div(
                        [
                        html.Div([html.H4(id='rslt_txt')], style={"text-align": 'center'}),
                        html.Div(id="graph-container",
                                   children =[dcc.Graph(id="cluster-plot")]),
                        html.Div([html.H5(id='cat_txt')],
                                 style={"text-align": 'left'})
                         ]
                    )
                ),
            ],
            id="modal-result",
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

sidebar = html.Div(
    style = {
        'background-color': 'rgba(225, 232, 242)',
        'min-width':'20%',
        'height':"100%",
    }
)

header = html.Div(
    style={
        'background-color': '#00407d',
        'width': '100%',
        'height': "auto",
        "margin-left": '0px',
        "padding-top": '1rem',
        "padding-bottom": '1rem',
    },
    children=[
        html.H1('AI-Doc', style={"margin": "auto", "text-align": "center", 'color':'white'}),
    ]
)

list_group = dbc.ListGroup(
   
    children = [
        dbc.ListGroupItem(id = 'rw1'),
        dbc.ListGroupItem(id = 'rw2'),
        dbc.ListGroupItem(id = 'rw3'),
        dbc.ListGroupItem(id = 'rw4'),
    ]
)

# Define Layout
layout = dbc.Container(
    fluid=True,
    children=[
        
        dcc.Store(id="store-conversation", data=[]),
        dcc.Store(id="store-qcount", data=0),
        dcc.Store(id="store-ans", data=[]),
        dcc.Location(id='url', refresh=False),
        dcc.Store(id="quizcount", data=0),
        dcc.Store(id="score", data=0),

        header,
        html.Div(
            style={
                'margin-top': '1rem',
                "float": "left",
                'width': '35%',
                'height': '100%',
                'background-color': 'rgba(225, 232, 242, 0.4)',
                'border': '2px solid #ffffff',
                'border-radius': '10px',
                '-moz-border-radius': '10px',
            },
            children=[
                html.Br(),
                html.H3(id='sidetitle', style={
                        "margin": "auto", "text-align": "center"}),
                html.Br(),
                html.Img(
                    id='sidebarImg',
                    src='',
                    style={
                        'vertical-align': 'middle',
                        #'padding-top': '2rem',
                        #'padding-left': '3rem',
                        'padding': 'auto',
                        'margin':'auto',
                        'height': '12rem',
                        "width": 'auto',
                        "object-fit": "contain",
                        'display':'block',
                        "text-align": "center"
                    }
                ),
                html.Br(),
                html.Br(),
                list_group,

                html.Div(
                    id='sidebarTxt',
                    style={
                        'padding-top': '3rem',
                        'padding-left': '3rem',
                        'padding-right': '3rem',
                        'height': '20rem',
                        "width": 'auto',
                    }
                )
            ]
        ),
        html.Div(
            style={
                "float": "left",
                'width': '65%',
                'height': '100%',
                # 'background-color': 'blue'
            },
            children=[
                quizmodal,
                sidebar,
                conversation,
                resultmodal,
                html.Br(),
                controls,
                html.Br(),
            ]
        ),
        
        dcc.Interval(
            id='onload_delay',
            max_intervals=1,
            interval=1*1000,  # in milliseconds
            n_intervals=0)
    ],
    style={
        'padding': '0',
        'margin': '0',
        'overflow': 'hidden'
    }
)
