import dash
from dash import Dash, html, dcc
from src import navbar
import dash_bootstrap_components as dbc

faw = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True,
	   external_stylesheets=[dbc.themes.MINTY, faw])

app.title = "my title"

app.layout = html.Div([
    dcc.Loading(
	    children=[navbar,
	       dash.page_container],
	   fullscreen=True)
])

if __name__ == '__main__':
	app.run_server(debug=True)#host="0.0.0.0", port=8080)






