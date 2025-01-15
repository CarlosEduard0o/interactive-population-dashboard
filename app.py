from dash import Dash, html, dcc, callback, Output, Input
from sqlalchemy import create_engine
import plotly.express as px
import pandas as pd

def get_data():
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
    query = "SELECT * FROM populacao;"
    df = pd.read_sql(query, engine)
    return df

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children="Title of Dash App", style={"textAlign": "center"}),
    dcc.Dropdown(id="dropdown-selection", placeholder="Selecione um país"),
    dcc.Graph(id="graph-content"),
    dcc.Interval(
        id="interval-component",
        interval=10 * 1000,
        n_intervals=0
    )
])

@callback(
    Output("dropdown-selection", "options"),
    Input("interval-component", "n_intervals")
)
def update_dropdown_options(n):
    df = get_data()
    return [{"label": country, "value": country} for country in df["country"].unique()]

@callback(
    Output("graph-content", "figure"),
    [Input("dropdown-selection", "value"),
     Input("interval-component", "n_intervals")]
)
def update_graph(value, n):
    df = get_data()
    if value:
        dff = df[df["country"] == value]
        return px.line(dff, x="year", y="pop", title=f"População de {value}")
    return px.line(title="Selecione um país para visualizar os dados.")

if __name__ == "__main__":
    app.run(debug=True)