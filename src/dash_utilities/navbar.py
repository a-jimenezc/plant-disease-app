import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Inicio", href="/")),
        dbc.NavItem(dbc.NavLink("Datos", href="/data")),
        dbc.NavItem(dbc.NavLink("Acerca de", href="/about")),
    ],
    brand="Detector de Plantas",
    brand_style={"whiteSpace": "pre-wrap"},
    brand_href="/",
    color="primary",
    dark=True,
)
   
