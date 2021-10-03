from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from ..Plots import alzheimer_clusterringPlot as ac
import plotly.graph_objs as go

import plotly.express as px
import pandas as pd
import os
# navbar = 
fig2 = ac.alzheimer_clusterPlot()
fig2.update_layout({
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
"font_color":"white",
"legend_font_color" : "white"
})


#data retrieval alzheimer
alzheimerlength = pd.read_csv("app/datasets/alzheimer.csv")
alzheimerdatalength = len(alzheimerlength)

dementedPatients = alzheimerlength[alzheimerlength['Group'].str.contains('Demented')]
dementedPatients = len(dementedPatients)

noncritical = alzheimerlength[alzheimerlength['Group'].str.contains('Converted')]
noncritical = len(noncritical)

#data retrieval covid 19
covidlength = pd.read_csv("app/datasets/covid-19 symptoms dataset.csv")
covidDatalength = len(covidlength)

# covidPatients = covidlength[covidlength['infectionProb'].str.contains(1)]


#pie chart plot 
pieChartFig = px.pie(alzheimerlength, values='MMSE', names='Group')
pieChartFig.update_layout({
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
"font_color":"white",
"legend_font_color" : "white"
})

pieChartFig2 = px.pie(alzheimerlength, names='M/F', color='M/F', color_discrete_sequence=px.colors.sequential.RdBu)
pieChartFig2.update_layout({
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
"font_color":"white",
"legend_font_color" : "white"
})

pieChartFig3 = px.pie(alzheimerlength, names='CDR', color_discrete_sequence=px.colors.sequential.RdBu)
pieChartFig3.update_layout({
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
"font_color":"white",
"legend_font_color" : "white"
})

#covid plots
a = ['Total cases', 'Confirmed cases', 'Non-critical cases']
figc1 = go.Figure([go.Bar(x=a, y=[2575, 1005, 1570])])
figc1.update_layout({
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
"font_color":"white",
"legend_font_color" : "white",
# "coloraxis" : "red"
})

figc2 = px.pie(covidlength, names='bodyPain', color='bodyPain', color_discrete_sequence=px.colors.sequential.RdBu)
figc3 = px.pie(covidlength, names='fever', color='fever', color_discrete_sequence=px.colors.sequential.RdBu)

df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')

layout = html.Div(id='main', children=[
    dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="HealthGO Dasboard",
    brand_href="#",
    color="black",
    dark=True,
    ),

    html.Div(
    [
            html.H4("Alzheimer", className="card-title",style={"color": "white", "margin": "10px"}), 
            dbc.Row(
            [
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Total visits", className="card-title"),
                                html.H1(alzheimerdatalength, className="card-subtitle"),
                                # html.P(
                                #     "Some quick example text to build on the card title and make "
                                #     "up the bulk of the card's content.",
                                #     className="card-text",
                                # )
                            ]
                        ),
                    style={"width": "500", "margin": "10px","color": "white" ,"background-color":"#2a2a72", "border-radius":"20px"},
                )
                )),
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Confirmed cases", className="card-title"),
                                html.H1(dementedPatients, className="card-subtitle"),
                                # html.P(
                                #     "Some quick example text to build on the card title and make "
                                #     "up the bulk of the card's content.",
                                #     className="card-text",
                                # ),
                                # dbc.CardLink("Card link", href="#"),
                                # dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    style={"width": "500", "margin": "10px", "color": "white" ,"background-color":"red", "border-radius":"20px"},
                )
                )),
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Non- Critical", className="card-title"),
                                html.H1(noncritical, className="card-subtitle"),
                                # html.P(
                                #     "Some quick example text to build on the card title and make "
                                #     "up the bulk of the card's content.",
                                #     className="card-text",
                                # ),
                                # dbc.CardLink("Card link", href="#"),
                                # dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    style={"width": "500", "margin": "10px", "color": "white" ,"background-color":"green", "border-radius":"20px"},
                )
                )),
            ]
        ),


        dbc.Row(dbc.Col(html.Div(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("Title", className="card-title"),
                        html.P(
                            "Alzheimer's is the most common cause of dementia, a general term for memory loss and other cognitive abilities serious enough to interfere with daily life. Alzheimer's disease accounts for 60-80% of dementia cases.Alzheimer's is not a normal part of aging. The greatest known risk factor is increasing age, and the majority of people with Alzheimer's are 65 and older. Alzheimer’s disease is considered to be younger-onset Alzheimer’s if it affects a person under 65. Younger-onset can also be referred to as early-onset Alzheimer’s. People with younger-onset Alzheimer’s can be in the early, middle or late stage of the disease.",
                            className="card-text",
                        ),
                        html.Center([
                            html.H2("Alzheimer types Plot", className="card-subtitle"),
                            dcc.Graph(id='plot2', figure = fig2 )
                        ])

                        
                        # dbc.CardLink("Card link", href="#"),
                        # dbc.CardLink("External link", href="https://google.com"),
                        #     dcc.Dropdown(
                        #         id='my-dropdown',
                        #         options=[
                        #             {'label': 'Coke', 'value': 'COKE'},
                        #             {'label': 'Tesla', 'value': 'TSLA'},
                        #             {'label': 'Apple', 'value': 'AAPL'}
                        #         ],
                        #         value='COKE'
                        #     ),
                        #     dcc.Graph(id='my-graph'),
                        #     dcc.Store(id='user-store'),
                    ]
                ),
                style={"width": "500", "margin": "10px", "color" : "white" ,"background-color":"black"},
            )
        ))),


                dbc.Row(
            [
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Patient Types", className="card-title"),
                                html.H6("(Alzheimers)", className="card-subtitle"),
                                html.P(
                                    "The following denotes the distribution of patients in the dataset",
                                    className="card-text",
                                ),
                                dbc.CardLink("Read more...", href="#"),
                                
                                dcc.Graph(id='plot3', figure = pieChartFig ),
                            ]
                        ),
                    style={"width": "500", "margin": "10px", "color" : "white" ,"background-color":"#323232"},
                )
                )),
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Gender Proportion", className="card-title"),
                                html.H6("(Alzheimers)", className="card-subtitle"),
                                html.P(
                                    "The following shows the gender proportion of Alzerimers patients",
                                    className="card-text",
                                ),
                                dbc.CardLink("Read more...", href="#"),
                                dcc.Graph(id='plot4', figure = pieChartFig2 ),
                            ]
                        ),
                    style={"width": "500", "margin": "10px", "color" : "white" ,"background-color":"#323232"},
                )
                )),
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Clinical Dimentia Rating", className="card-title"),
                                html.H6("(Alzheimers)", className="card-subtitle"),
                                html.P(
                                    "CDR score affect mainly to predict the alzheimers patients",
                                    className="card-text",
                                ),
                                dbc.CardLink("Read more...", href="#"),
                                dcc.Graph(id='plot5', figure = pieChartFig3 , style={"plot_bgcolor":"rgba(0,0,0,0)"}),
                            ]
                        ),
                    style={"width": "500", "margin": "10px", "color" : "white" ,"background-color":"#323232"},
                )
                )),
            ]
        )
    ]),
    html.Div(
    [
        html.H4("COVID-19", className="card-title",style={"color": "white", "margin": "10px"}), 
            dbc.Row(
            [
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Total visits", className="card-title"),
                                html.H1(covidDatalength, className="card-subtitle"),
                                # html.P(
                                #     "Some quick example text to build on the card title and make "
                                #     "up the bulk of the card's content.",
                                #     className="card-text",
                                # )
                            ]
                        ),
                    style={"width": "500", "margin": "10px","color": "white" ,"background-color":"#2a2a72", "border-radius":"20px"},
                )
                )),
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Confirmed cases", className="card-title"),
                                html.H1("1005", className="card-subtitle"),
                                # html.P(
                                #     "Some quick example text to build on the card title and make "
                                #     "up the bulk of the card's content.",
                                #     className="card-text",
                                # ),
                                # dbc.CardLink("Card link", href="#"),
                                # dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    style={"width": "500", "margin": "10px", "color": "white" ,"background-color":"red", "border-radius":"20px"},
                )
                )),
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Non- Critical", className="card-title"),
                                html.H1("1570", className="card-subtitle"),
                                # html.P(
                                #     "Some quick example text to build on the card title and make "
                                #     "up the bulk of the card's content.",
                                #     className="card-text",
                                # ),
                                # dbc.CardLink("Card link", href="#"),
                                # dbc.CardLink("External link", href="https://google.com"),
                            ]
                        ),
                    style={"width": "500", "margin": "10px", "color": "white" ,"background-color":"green", "border-radius":"20px"},
                )
                )),
            ]
        ),

                    dbc.Row(dbc.Col(html.Div(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H4("Covid 19 data analysis", className="card-title"),
                        html.H6("", className="card-subtitle"),
                        html.P(
                            "Coronavirus disease 2019 (COVID-19), also known as COVID and the coronavirus, is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December 2019.The disease has since spread worldwide, leading to an ongoing pandemic. Symptoms of COVID-19 are variable, but often include fever, cough, headache, fatigue, breathing difficulties, and loss of smell and taste. Symptoms may begin one to fourteen days after exposure to the virus. At least a third of people who are infected do not develop noticeable symptoms. Of those people who develop symptoms noticeable enough to be classed as patients, most (81%) develop mild to moderate symptoms (up to mild pneumonia), while 14% develop severe symptoms",
                            className="card-text",
                        ),
                        html.Center([
                            dcc.Graph(id='plot6', figure = figc1 , style={"plot_bgcolor":"rgba(0,0,0,0)"}),
                        ])

                        
                        # dbc.CardLink("Card link", href="#"),
                        # dbc.CardLink("External link", href="https://google.com"),
                        #     dcc.Dropdown(
                        #         id='my-dropdown',
                        #         options=[
                        #             {'label': 'Coke', 'value': 'COKE'},
                        #             {'label': 'Tesla', 'value': 'TSLA'},
                        #             {'label': 'Apple', 'value': 'AAPL'}
                        #         ],
                        #         value='COKE'
                        #     ),
                        #     dcc.Graph(id='my-graph'),
                        #     dcc.Store(id='user-store'),
                    ]
                ),
                style={"width": "500", "margin": "10px", "color" : "white" ,"background-color":"black"},
            )
        ))),

                dbc.Row(
            [
                
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Gender Variations", className="card-title"),
                                html.H6("(COVID-19)", className="card-subtitle"),
                                html.P(
                                    "The following shows the gender diversity among covid patients.",
                                    className="card-text",
                                ),
                                dbc.CardLink("Read more...", href="#"),
                                
                                dcc.Graph(id='plot7', figure = figc2 , style={"plot_bgcolor":"rgba(0,0,0,0)"}),
                            ]
                        ),
                    style={"width": "200", "margin": "10px", "color" : "white" ,"background-color":"#323232"},
                )
                )),
                dbc.Col(html.Div(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Fever level variation", className="card-title"),
                                html.H6("(COVID-19)", className="card-subtitle"),
                                html.P(
                                    "Fever level of among covid patients is displayed below with respective tho the tempurature in Farenheit",
                                    className="card-text",
                                ),
                                dbc.CardLink("Read more...", href="#"),
                                dcc.Graph(id='plot8', figure = figc3 , style={"plot_bgcolor":"rgba(0,0,0,0)"}),
                            ]
                        ),
                    style={"width": "200", "margin": "10px", "color" : "white" ,"background-color":"#323232"},
                )
                )),


            ]
        ),
    ]
)


    # html.H1(id='username'),
    # html.H1('Dashboard'),
    # dcc.Dropdown(
    #     id='my-dropdown',
    #     options=[
    #         {'label': 'Coke', 'value': 'COKE'},
    #         {'label': 'Tesla', 'value': 'TSLA'},
    #         {'label': 'Apple', 'value': 'AAPL'}
    #     ],
    #     value='COKE'
    # ),
    # dcc.Graph(id='my-graph'),
    # dcc.Store(id='user-store'),
], style={'width': '500', "background-color": "black", "padding" : "20px"})
