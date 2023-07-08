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
            En esta se pone a disposición una herramienta que permite estimar
            el precio de una vivienda en la ciudad de Santa Cruz de la Sierra.
            Tener una aproximación del valor de una propiedad es muy útil si se desea,
            por ejemplo, vender, comprar o comparar viviendas.

            El modelo fue entrenado con datos de viviendas de Santa Cruz de la Sierra,
            principalmente casas y departamentos. Para obtener una descripción detallada
            de los aspectos técnicos visitar el repositorio en GitHub del
            proyecto. Allí se explica en detalle el proceso de recolección de datos y la
            selección del algoritmo utilizado para la estimación, *Gradient Boosting*.
            """,
            style={'text-align': 'justify'}
        ),
        html.Br(),

        html.Div([
                html.A(
                    href="https://github.com/a-jimenezc/bienes_raices_scz",
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
            """Esta página web fue creada por Antonio Jimenez Caballero, un
            ingeniero eletromecánico y docente universitario. 
            Tiene un fuerte interés por la Ciencia de Datos y
            su potencial para resolver necesidades cotidianas.
            
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