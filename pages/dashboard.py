import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from src import filter_df_for_plot

dash.register_page(__name__, 
                   path='/dashboard',
                   title="Dashboard")

# Load your real estate dataset
df = pd.read_csv('data/real_state_data_for_dashboard.csv')

# Create the Dash app
app = dash.Dash(__name__)

title = html.H1(["Dashboard"],
                style={
                    'text-align': 'center',
                    })

introductory_paragraph = html.P(
            ["""Se presentan estadísticas y gráficos descriptivos de la 
            base de datos usada para entrenar el modelo. Además, se incluyen filtros
            para ajustar las gráficas a los rangos deseados. Para una mejor experiencia, 
            se recomienda abrir esta página en la computadora."""],
            style={'text-align': 'left',
                   'margin-left' : '5%',
                   'font-size': '18px',
                        })

#indicadores
indicators = html.Div([
    dcc.Graph(id='indicators')
    ])

#menus
dropdown_menus = html.Div([
                html.H2([
                    'Filtros:'
                ], style={
                   'text-align': 'center'
                }),
                html.P(['Seleccionar rango de precios:'], 
                        style={
                            'text-align': 'left',
                            'margin-bottom': '10px',
                            'font-size': '18px',
                               }),
                dcc.RangeSlider(
                    id="price-range",
                    marks={i: f"${i//1000}k" for i in range(0, 155000, 30000)},
                    min=0,
                    max=150000,
                    step=10000,
                    value=[20000, 130000],
                ),
                html.P(['Seleccionar el rango del número de habitaciones:'], 
                        style={
                            'text-align': 'left',
                            'margin-bottom': '10px',
                            'font-size': '18px',
                               }),
                dcc.RangeSlider(
                id="bedrooms",
                marks={i: f"{i}" for i in range(0, 11)},
                min=0,
                max=10,
                step=1,
                value=[1, 8],
            ),
                html.P(['Seleccionar el rango del número de baños:'], 
                    style={
                        'text-align': 'left',
                        'margin-bottom': '10px',
                        'font-size': '18px',
                        }),
                dcc.RangeSlider(
                id="bathrooms",
                marks={i: f"{i}" for i in range(1, 7)},
                min=0,
                max=6,
                step=1,
                value=[1, 4],
            ),
                html.P(['Seleccionar el tipo de propiedad:'], 
                        style={
                            'text-align': 'left',
                            'margin-bottom': '10px',
                            'font-size': '18px',
                               }),
                dcc.Dropdown(
                    id="property-type",
                    options=[
                        {"label": "Todos", "value": ""},
                        *[
                            {"label": prop_type, "value": prop_type} for prop_type in df['tipo_de_propiedad'].unique()
                        ]
                    ],
                    placeholder="Seleccionar el tipo de propiedad",
                    value="",
                ),
                html.P(['Seleccionar la ciudad:'], 
                        style={
                            'text-align': 'left',
                            'margin-bottom': '10px',
                            'font-size': '18px',
                               }),
                dcc.Dropdown(
                    id="city",
                    options=[
                        {"label": "Todos", "value": ""},
                        *[
                            {"label": city, "value": city} for city in df['ciudad'].unique()
                        ]
                    ],
                    placeholder="Seleccionar la ciudad",
                    value="",
                ),
                html.P(['Seleccionar la zona:'], 
                        style={
                            'text-align': 'left',
                            'margin-bottom': '10px',
                            'font-size': '18px',
                               }),
                dcc.Dropdown(
                    id="zone",
                    options=[
                        {"label": "Todos", "value": ""},
                        *[
                            {"label": zone, "value": zone} for zone in df['zona'].unique()
                        ]
                    ],
                    placeholder="Seleccionar la zona",
                    value="",
                ),
            ])

#gráficos
plots = html.Div([
        #características de las propiedades
        html.Div([
                dcc.Graph(id="price-distribution"),
                html.Div([
                    #número de habitaciones
                    html.Div([
                            dcc.Graph(id="bedroom-count"),
                        ],style={'width' : '50%'}
                    ),
                    #tipo de propiedad
                    html.Div([
                            dcc.Graph(id="property-type-distribution"),
                        ],style={'width' : '50%'}
                    ),
                    ], style={
                        'display': 'flex',
                              })
            ]
        ),
        #tamaños de terrenos
        html.Div([
                dcc.Graph(id="property-size"),
            ]
        ),
        html.Div([
            #años de construcción
            html.Div([
                    dcc.Graph(id="time-analysis"),
                ],style={'width' : '50%'}
            ),
            #mapa
            html.Div([
                    dcc.Graph(id="geospatial-analysis"),
                ],style={'width' : '50%'}
            ),
            ], 
            style={#'width' : '100%',
                    'display': 'flex'})
]
)

#layout
layout = html.Div([
        title,
        introductory_paragraph,
        html.Div([
            html.Div([
                indicators,
                dropdown_menus
                ],style={
                    'width' : '20%'
                 }),
            html.Div([
                plots
                ],style={
                    #'flex' : '1',
                    'width' : '80%'
                    })
        ],style={
            'display': 'flex',
            'margin' : '5%'
            #'font-size': '14px', 
            }),
        html.Br(),
        html.Br(),
        html.P('''Versión 1.0 | Última actualización de datos: mayo 2023.''', 
               style={'fontSize': 10,
                      'margin-left' : '10%'},),
        html.Br(),
        html.Br(),
])


#Callbacks para actualizar las visualizaciones
#indicadores
@callback(
    dash.dependencies.Output("indicators", "figure"),
    [
        dash.dependencies.Input("price-range", "value"),
        dash.dependencies.Input("bedrooms", "value"),
        dash.dependencies.Input("bathrooms", "value"),
        dash.dependencies.Input("property-type", "value"),
        dash.dependencies.Input("city", "value"),
        dash.dependencies.Input("zone", "value"),
        ])
def indicator(precios, dormitorios, baños, tipo, ciudad, zona):
    
    df_f = filter_df_for_plot(df.copy(), 
                              precios, dormitorios, baños, tipo, ciudad, zona)
    #gráfico conteo de dormintorios
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "number",
        value = len(df_f),
        number = {
            'font_size': 40,
            'valueformat' : 'text'
            },
        title = {
            'text': "Total de propiedades",
            'font_size' : 24
            },
    domain = {'row': 0, 'column': 0}
        ))

    fig.add_trace(go.Indicator(
        mode = "number",
        value = round(df_f['precio'].mean()),
        number = {
            'font_size': 40,
            'valueformat' : 'text',
            'prefix' : '$ '
            },
        title = {
            'text': "Precio promedio",
            'font_size' : 24
            },
        domain = {'row': 1, 'column': 0}
        ))

    fig.add_trace(go.Indicator(
        mode = "number",
        value = round(df_f['no_dormitorios'].mean()),
        number = {
            'font_size': 40,
            'valueformat' : 'text',
            },
        title = {
            'text': "Promedio de habitaciones",
            'font_size' : 24
            },
        domain = {'row': 2, 'column': 0}
        ))

    fig.add_trace(go.Indicator(
        mode = "number",
        value = round(df_f['no_baños'].mean()),
        number = {
            'font_size': 40,
            'valueformat' : 'text',
            },
        title = {
            'text': "Promedio de baños",
            'font_size' : 24
            },
        domain = {'row': 3, 'column': 0}
        ))

    fig.update_layout(
        grid = {
            'rows': 4, 
            'columns': 1, 
            'pattern': "independent",
            'ygap': 1
            })
    return fig


#precio_histograma
@callback(
    dash.dependencies.Output("price-distribution", "figure"),
    [
        dash.dependencies.Input("price-range", "value"),
        dash.dependencies.Input("bedrooms", "value"),
        dash.dependencies.Input("bathrooms", "value"),
        dash.dependencies.Input("property-type", "value"),
        dash.dependencies.Input("city", "value"),
        dash.dependencies.Input("zone", "value"),
        ])
def update_histogram_count(precios, dormitorios, baños, tipo, ciudad, zona):
    
    df_f = filter_df_for_plot(df.copy(), 
                              precios, dormitorios, baños, tipo, ciudad, zona)
    #gráfico conteo de dormintorios
    df_f.rename(columns={'precio': 'Precios'}, 
                        inplace=True)
    fig = px.histogram(df_f, x='Precios', 
                    title="Distribución de los precios",
                    nbins=50,
                    color_discrete_sequence=[px.colors.qualitative.Dark2[0]],
                       )
    fig.update_layout(
        xaxis_title="Precios",
        yaxis_title="Cantidad de propiedades",
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(size=25)
        })
    return fig


#dormitorios: gráfico de barras
@callback(
    dash.dependencies.Output("bedroom-count", "figure"),
    [
        dash.dependencies.Input("price-range", "value"),
        dash.dependencies.Input("bedrooms", "value"),
        dash.dependencies.Input("bathrooms", "value"),
        dash.dependencies.Input("property-type", "value"),
        dash.dependencies.Input("city", "value"),
        dash.dependencies.Input("zone", "value"),
        ])
def update_bedroom_count(precios, dormitorios, baños, tipo, ciudad, zona):

    df_f = filter_df_for_plot(df.copy(), 
                              precios, dormitorios, baños, tipo, ciudad, zona)
    #gráfico conteo de dormitorios
    df_plot = df_f["no_dormitorios"].value_counts().to_frame().reset_index()
    df_plot.rename(columns={'no_dormitorios': 'Habitaciones',
                            'count' : 'Cantidad de propiedades'}, 
                            inplace=True)
    fig = px.bar(df_plot, y="Habitaciones", 
                 x="Cantidad de propiedades", 
                 title="Cantidad de propiedades según<br>el número de habitaciones",
                 color_discrete_sequence=[px.colors.qualitative.Dark2[1]],
                 orientation='h')
    # Update x and y labels
    fig.update_layout(
        xaxis_title="Cantidad de propiedades",
        yaxis_title="Habitaciones",
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(size=25)}
    )
    return fig

#gráfico de torta
@callback(
    dash.dependencies.Output("property-type-distribution", "figure"),
    [
        dash.dependencies.Input("price-range", "value"),
        dash.dependencies.Input("bedrooms", "value"),
        dash.dependencies.Input("bathrooms", "value"),
        dash.dependencies.Input("property-type", "value"),
        dash.dependencies.Input("city", "value"),
        dash.dependencies.Input("zone", "value"),
        ])
def update_piechart(precios, dormitorios, baños, tipo, ciudad, zona):

    df_f = filter_df_for_plot(df.copy(), 
                              precios, dormitorios, baños, tipo, ciudad, zona)
    #piechart
    df_f.rename(columns={'tipo_de_propiedad': 'Tipo de propiedad'}, 
                        inplace=True)
    fig = px.pie(df_f, names="Tipo de propiedad", title="Tipos de propiedades",
                 color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(size=25)}
    )
    return fig

#mapa
@callback(
    dash.dependencies.Output("geospatial-analysis", "figure"),
    [
        dash.dependencies.Input("price-range", "value"),
        dash.dependencies.Input("bedrooms", "value"),
        dash.dependencies.Input("bathrooms", "value"),
        dash.dependencies.Input("property-type", "value"),
        dash.dependencies.Input("city", "value"),
        dash.dependencies.Input("zone", "value"),
        ])
def update_map(precios, dormitorios, baños, tipo, ciudad, zona):

    df_f = filter_df_for_plot(df.copy(), 
                              precios, dormitorios, baños, tipo, ciudad, zona)
    #mapa
    df_f.latitud = df_f.latitud.round(decimals=3) + 0.002
    df_f.longitud = df_f.longitud.round(decimals=3) + 0.002
    fig = px.scatter_mapbox(
        df_f,
        lat="latitud",
        lon="longitud",
        hover_name="tipo_de_propiedad",
        mapbox_style="open-street-map",
        title="Análisis Geoespacial",
    )
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(size=25)}
    )
    return fig

#scatterplot
@callback(
    dash.dependencies.Output("property-size", "figure"),
    [
        dash.dependencies.Input("price-range", "value"),
        dash.dependencies.Input("bedrooms", "value"),
        dash.dependencies.Input("bathrooms", "value"),
        dash.dependencies.Input("property-type", "value"),
        dash.dependencies.Input("city", "value"),
        dash.dependencies.Input("zone", "value"),
        ])
def update_scatter(precios, dormitorios, baños, tipo, ciudad, zona):

    df_f = filter_df_for_plot(df.copy(), 
                              precios, dormitorios, baños, tipo, ciudad, zona)
    #scatter plot
    df_f.rename(columns={'area_constr_m2': 'Área construida (m2)',
                            'terreno_m2' : 'Terreno (m2)'}, 
                            inplace=True)
    fig = fig = px.scatter(df_f, x="Área construida (m2)", y="Terreno (m2)",
                           color = "precio",
                           title="Área construida vs Terreno",
                           color_discrete_sequence=px.colors.qualitative.Dark2)
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(size=25)}
    )
    return fig

#años de construcción
@callback(
    dash.dependencies.Output("time-analysis", "figure"),
    [
        dash.dependencies.Input("price-range", "value"),
        dash.dependencies.Input("bedrooms", "value"),
        dash.dependencies.Input("bathrooms", "value"),
        dash.dependencies.Input("property-type", "value"),
        dash.dependencies.Input("city", "value"),
        dash.dependencies.Input("zone", "value"),
        ])
def update_line(precios, dormitorios, baños, tipo, ciudad, zona):

    df_f = filter_df_for_plot(df.copy(), 
                              precios, dormitorios, baños, tipo, ciudad, zona)

    df_f = df.año_constr.value_counts().to_frame().reset_index()
    df_f = df_f.sort_values('año_constr')
    df_f.rename(columns={'año_constr' : 'Año de construcción',
                    'count' : 'Cantidad de propiedades'}, inplace=True)

    fig = px.line(
        df_f,
        x="Año de construcción",
        y="Cantidad de propiedades",
        title="Propiedades construidas según el año",
        color_discrete_sequence=[px.colors.qualitative.Dark2[3]]
    )
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font' : dict(size=25)}
    )
    return fig
