from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import psycopg2 as pc

# Configuração de conexão com o banco de dados
def get_data():
    conn = pc.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    query = "SELECT * FROM populacao;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Inicializa o Dash
app = Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1(children="Title of Dash App", style={"textAlign": "center"}),
    dcc.Dropdown(id="dropdown-selection", placeholder="Selecione um país"),
    dcc.Graph(id="graph-content"),
    dcc.Interval(
        id="interval-component",
        interval=10 * 1000,  # Atualiza a cada 10 segundos
        n_intervals=0
    )
])

# Callback para atualizar as opções do dropdown com os países disponíveis
@callback(
    Output("dropdown-selection", "options"),
    Input("interval-component", "n_intervals")
)
def update_dropdown_options(n):
    df = get_data()
    return [{"label": country, "value": country} for country in df["country"].unique()]

# Callback para atualizar o gráfico com base no país selecionado
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

# Executa a aplicação
if __name__ == "__main__":
    app.run(debug=True)