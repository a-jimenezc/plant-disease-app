import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
from src import encode_image

dash.register_page(__name__, 
                   path='/data',
                   title="Datos")


image1_path = "images/distr.png"
image2_path = "images/trad.png"

image1_encoded = encode_image(image1_path)
image2_encoded = encode_image(image2_path)

layout = html.Div([
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Br(),
                    html.H2("Plantdoc Dataset"),
                    html.Br(),
                    dcc.Markdown('''PlantDoc es un conjunto de datos para la 
                                 detección visual de enfermedades en plantas. 
                                 Este conjunto de datos contiene un total de 2,598 
                                 puntos de datos en total, que abarcan 13 especies 
                                 de plantas y hasta 17 clases de enfermedades. 
                                 Para mayor información dirigirse consultar con la 
                                 fuente original: ["PlantDoc: A Dataset for Visual 
                                 Plant Disease Detection"]
                                 (https://github.com/pratikkayal/PlantDoc-Dataset)'''),
                    html.Br(),
                    html.H3("Distribución de los Datos"),
                    html.Br(),
                    html.Img(src=f"data:image/jpeg;base64,{image1_encoded}", 
                            style={"width": "80%"}),
                            html.Br(),
                    html.P('''La primeras 6 categorias estan "sobrerepresentadas" y se 
                           tiene el caso contrario para las últimas 6 categorias. Esto 
                           se verá reflejado en las predicciones del modelo, siendo este más preciso
                           con las primeras.'''),
                ],
                style={"textAlign": "center", "marginBottom": "0px"},
            ),
            html.Div(
                children=[
                    html.Br(),
                    html.H3("Traducción Utilizada"),
                    html.Br(),
                    html.Img(src=f"data:image/jpeg;base64,{image2_encoded}", 
                            style={"width": "80%"}),
                    html.P(""),
                ],
                style={"textAlign": "center"},
            ),
        ],
        style={"maxWidth": "800px", "margin": "auto"},
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P('Versión 0.1, julio del 2023 | Última actualización de datos: 2020.', 
                    style={'fontSize': 10, 'margin-left' : '10%'})
])



