import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
from src import object_detection


dash.register_page(__name__, path='/', title="Estimador")

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
    ]
    ,style={
                'display': 'flex',
                'text-align': 'center',
                'width': '50%'
                }
    )]
)

note_about_output = html.Div([
    html.Div([
    html.P([
    "Notas sobre el resultado:",
    "(5) Para el año de construcción, los valores aceptados varían desde el año 2000 hasta el año 2025."
    ])
    ],style={
                'display': 'inline-block',
                'text-align': 'left',
                'margin-left': '20%',
                'width': '60%',
                'fontSize': 14}
    )]
)

footnote =  html.P('Versión 1.0 | Última actualización de datos: mayo 2023.', 
                    style={'fontSize': 10,
                        'margin-left' : '10%'})

layout = html.Div(children=[
    html.Br(),
    title,
    html.Div([
        html.Br(),
        input,
        output,
        html.Br(),
        html.Br(),
        note_about_output,
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
        img_path = '3.jpg'
        names = ['Hoja de sarna de manzana', 'Hoja de manzana', 'Hoja de oxido de manzana', 'Mancha en hoja de pimiento',
            'Hoja de pimiento', 'Hoja de arandano', 'Hoja de cereza', 'Mancha gris en hoja de maiz',
            'Marchitez en hoja de maiz', 'Hoja de roya de maiz', 'Hoja de durazno', 'Tizon temprano en hoja de papa',
            'Tizon tardio en hoja de papa', 'Hoja de papa', 'Hoja de frambuesa', 'Hoja de soja',
            'Hoja de frijol de soja', 'Oidio en hoja de calabaza', 'Hoja de fresa', 'Tizon temprano en hoja de tomate',
            'Mancha de Septoria en hoja de tomate', 'Mancha bacteriana en hoja de tomate',
            'Tizon tardio en hoja de tomate', 'Virus del mosaico en hoja de tomate', 'Virus de la hoja amarilla en tomate',
            'Hoja de tomate', 'Moho en hoja de tomate', 'Araña roja en hoja de tomate',
            'Podredumbre negra en hoja de vid', 'Hoja de vid']

        result_image = object_detection(model_path, contents, names)

        # Display the grayscale image
        return html.Div([
            html.H5(filename),
            html.Img(src=result_image)
        ])

    return None