import io
import base64
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import PIL.Image
import numpy as np
from src import object_detection

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Image')
        ]),
        style={
            'width': '50%',
            'height': '200px',
            'lineHeight': '200px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-image-container')
])


@app.callback(
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

        result_image = object_detection(model_path, img_path, names)

        # Display the grayscale image
        return html.Div([
            html.H5(filename),
            html.Img(src=result_image)
        ])

    return None


if __name__ == '__main__':
    app.run_server(debug=True)