import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
from src import object_detection, encode_image

dash.register_page(__name__, path='/', title="Detector")

# Encoding images for later use
image1_path = "images/input.jpg"
image2_path = "images/detection.png"
image3_path = "images/trad.png"

image1_encoded = encode_image(image1_path)
image2_encoded = encode_image(image2_path)
image3_encoded = encode_image(image3_path)

# Building the parts for the layout
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
        html.Br()
    ],style={
                'display': 'flex',
                'text-align': 'center',
                'width': '50%',
                'margin-left': '25%',
                }
    )]
)

output_text = html.Div([
    html.Div([
        html.H4('Detección:'),
        html.Div(id='output-text-container'),
    ],style={
                'font-size': '20px',
                'text-align': 'left',
                'width': '50%',
                'margin-left': '25%',
                }
    )]
)

example = html.Div(
    children=[
        html.Div(
            children=[
                html.H3("Ejemplo:"),
                html.Div(
                    children=[
                        html.Img(
                            src="data:image/jpg;base64," + image1_encoded,
                            style={"width": "50%", "display": "inline-block"},
                        ),
                        html.Img(
                            src="data:image/jpg;base64," + image2_encoded,
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

species = html.Div(
    children=[
        html.Div(
            children=[
                html.H3("Especies y enfermedades admitidas:"),
                html.Div(
                    children=[
                        html.Img(
                            src="data:image/jpg;base64," + image3_encoded,
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
    "Notas:",
    html.Br(),
    '(1) Este es un proyecto en desarrollo, se recomienda utilizar varias fotografías diferentes y "promediar" el resutado.',
    html.Br(),
    "(2) El modelo puede identificar 13 diferentes especies de plantas y hasta 17 enfermedades. ",
    html.Span("Abajo se encuentra la lista de las especies admitidas.", style={'font-weight': 'bold'}),
    html.Br(),
    "(3) La calidad del resultado varía dependiendo del tipo de hoja, se recomienda ver la ",
    html.Span("pestaña Datos ", style={'font-weight': 'bold'}),
    "para mayor información.",
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
        output_text,
        html.Br(),
        note_about_output,
        #html.Br(),
        example,
        html.Br(),
        species,
        html.Br(),
        html.Br(),
        footnote
    ])

])

@callback(
    Output('output-image-container', 'children'),
    Output('output-text-container', 'children'),
    Input('upload-image', 'contents'),
)
def process_image(contents):
    model_path = "models/yolov7_pantdoc_100epochs.onnx"
    names = ['Hoja con sarna de manzana',
            'Hoja de manzana',
            'Hoja de oxido de manzana',
            'Hoja de pimiento',
            'Hoja con manchas de pimiento',
            'Hoja de arandano',
            'Hoja de cereza',
            'Hoja con manchas grises de maiz',
            'Hoja con mancha foliar del maiz',
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
    if contents is not None:
        result_image, list_output = object_detection(model_path, contents, names)
        # Display the result_image
        return html.Img(src=result_image), dcc.Markdown("\n \n".join(list_output))
    
    return None, dcc.Markdown("")