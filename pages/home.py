import dash
import base64
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
from src import object_detection


dash.register_page(__name__, path='/', title="Detector")

title = html.H2('Detector de Enfermedades de Plantas',
                        style={'textAlign': 'center'})

input = html.Div([dcc.Upload(
                        id='upload-image',
                        children=html.Div([
                            'Arrastrar y soltar o ',
                            html.A('seleccionar imagen',
                                    style={
                                        'textDecoration': 'underline', 
                                        'color': 'blue',
                                        'justifyContent': 'center',
                                        'alignItems': 'center',
                                    }
                            )
                        ]), style={
                            'width': '50%',
                            'lineHeight': '200px',
                            'borderWidth': '2px',
                            'borderStyle': 'dashed',
                            'borderRadius': '20px',
                            'margin-left': '25%',
                            },
                        multiple=False
                        )], style={
                                #'display': 'flex',
                                'text-align': 'center',
                                'width': '100%'
                            }
            )

output = html.Div([
    html.Div([
        html.Div(id='output-image-container'),
    ],style={
                'display': 'flex',
                'text-align': 'center',
                'width': '50%',
                'margin-left': '25%',
                }
    )]
)

with open("pictures/input.jpg", "rb") as f:
    image1_data = f.read()
    encoded_image1 = base64.b64encode(image1_data).decode("utf-8")

with open("pictures/detection.png", "rb") as f:
    image2_data = f.read()
    encoded_image2 = base64.b64encode(image2_data).decode("utf-8")

example = html.Div(
    children=[
        html.Div(
            children=[
                html.H3("Ejemplo:"),
                html.Div(
                    children=[
                        html.Img(
                            src="data:image/jpg;base64," + encoded_image1,
                            style={"width": "50%", "display": "inline-block"},
                        ),
                        html.Img(
                            src="data:image/jpg;base64," + encoded_image2,
                            style={"width": "50%", "display": "inline-block"},
                        ),
                    ],
                    style={"text-align": "center"},
                ),
            ],
            style={"margin": "50px"},
        )
    ]
)

note_about_output = html.Div([
    html.Div([
    html.P([
    "Notas sobre el resultado:",
    html.Br(),
    '(1) Este es un proyecto en desarrollo, se recomienda utilizar varias fotografías diferentes y "promediar" el resutado.',
    html.Br(),
    "(2) El modelo puede identificar 13 diferentes especies de plantas y hasta 17 enfermedades.",
    html.Br(),
    "(3) La calidad del resultado varía dependiendo del tipo de hoja, se recomienda ver la descripción para mayor información",
    html.Br(),
    '(4) El valor entre 0 y 1 que se entrega con el resultado es la "confianza" que el modelo tiene sobre el mismo, cuanto mayor es este valor, mayor es dicha "confianza".'
    ])
    ],style={
                'display': 'inline-block',
                'text-align': 'left',
                'margin-left': '20%',
                'width': '60%',
                'fontSize': 14}
    )]
)

footnote =  html.P('Versión 0.1, julio del 2023 | Última actualización de datos: 2020.', 
                    style={'fontSize': 10, 'margin-left' : '10%'})

layout = html.Div(children=[
    html.Br(),
    title,
    html.Div([
        html.Br(),
        input,
        html.Br(),
        output,
        html.Br(),
        note_about_output,
        #html.Br(),
        example,
        html.Br(),
        html.Br(),
        html.Br(),
        footnote
    ])

])

@callback(
    Output('output-image-container', 'children'),
    Input('upload-image', 'contents'),
    State('upload-image', 'filename')
)
def process_image(contents, filename):
    if contents is not None:
        model_path = "models/yolov7_pantdoc_100epochs.onnx"
        names = ['Hoja con sarna de manzana',
                'Hoja de manzana',
                'Hoja de oxido de manzana',
                'Hoja de pimiento',
                'Hoja con manchas de pimiento',
                'Hoja de arandano',
                'Hoja de cereza',
                'Hoja con manchas grises de maiz',
                'Hoja de mancha foliar del maiz',
                'Hoja con oxido de maiz',
                'Hoja de durazno',
                'Hoja con tizon temprano de papa',
                'Hoja con tizon temprano de papa',
                'Hoja con tizon tardio de papa',
                'Hoja de frambuesa',
                'Hoja de soja',
                'Hoja de soja',
                'Hoja con oidio de calabaza',
                'Hoja de fresa',
                'Hoja con tizon temprano de tomate',
                'Hoja con manchas de septoria de tomate',
                'Hoja de tomate',
                'Hoja con manchas bacterianas de tomate',
                'Hoja con tizon tardio de tomate',
                'Hoja con virus del mosaico de tomate',
                'Hoja con virus amarillo del tomate',
                'Hoja con moho de tomate',
                'Hoja con acaros de dos manchas de tomate',
                'Hoja de uva',
                'Hoja de uva con podredumbre negra',
        ]

        result_image = object_detection(model_path, contents, names)

        # Display the result_image
        return html.Div([html.Img(src=result_image)])
    
    return None