import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, 
                   path='/about',
                   title="Acerca de")

layout = html.Div(
    children=[
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div([
            html.H3("Sobre el Proyecto")
        ], style={'text-align': 'center'}),
        dcc.Markdown(
            """
            Esta página fue creada con [Dash Open Source](https://dash.plotly.com).
            En esta se pone a disposición una herramienta identificar enfermedades
            en hojas de plantas de cultivo comunes: 13 especies de plantas diferentes 
            y hasta 17 enfermedades diferentes. El modelo de Deep Learning usado
            fue [YOLOv7](https://arxiv.org/abs/2207.02696) con la implementación "open-source"
            de [Wong Kin Yiu](https://github.com/WongKinYiu/yolov7). La 
            base de datos que se utilizó se puede encontrar en: ["PlantDoc: A Dataset for 
            Visual Plant Disease Detection"](https://github.com/pratikkayal/PlantDoc-Dataset). 
            
            Para obtener una descripción detallada
            de los aspectos técnicos visitar el repositorio en GitHub del
            proyecto. 
            """,
            style={'text-align': 'justify'}
        ),
        html.Br(),

        html.Div([
                html.A(
                    href="https://github.com/a-jimenezc/plant-disease-app",
                    target="_blank",
                    children=[
                        html.I(className="fab fa-github"),
                        " GitHub repo",
                    ],
                    className="m-2",
                ),
            ], style={
                'display': 'flex',
                'justify-content': 'center',
            }
        ),
        html.Br(),
        html.Br(),
        html.Div([
            html.H3("Sobre el Autor")
        ], style={'text-align': 'center'}),
        dcc.Markdown(
            """Hola, soy Antonio Jimenez y 
            tengo un fuerte interés por la Ciencia de Datos y
            su potencial para resolver necesidades cotidianas. En mi github encontrarás 
            otros proyectos en los que trabajé. Estoy atento a cualquier comentario.
            """,
            style={'text-align': 'justify'}
        ),
        html.Br(),
        html.Div([
            html.H4("Contacto")
        ], style={'text-align': 'center'}),
        html.Br(),

        html.Div([
                html.A(
                    href="https://github.com/a-jimenezc",
                    target="_blank",
                    children=[
                        html.I(className="fab fa-github"),
                        " GitHub",
                    ],
                    className="m-2",
                ),
                html.A(
                    href="https://www.linkedin.com/in/antonio-jimnzc",
                    target="_blank",
                    children=[
                        html.I(className="fab fa-linkedin"),
                        " LinkedIn",
                    ],
                    className="m-2",
                ),
                html.A(
                    href="mailto:antonio.jimzC@gmail.com",
                    target="_blank",
                    children=[
                        html.I(className="fab fa-google"),
                        " Gmail",
                    ],
                    className="m-2",
                ),
            ], style={
                'display': 'flex', 
                'justify-content': 'center'
                },
        ),
        html.Br(),
        html.Br(),
    ],
    className="container mt-4",
)