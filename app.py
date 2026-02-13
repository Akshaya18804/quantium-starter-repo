import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv("pink_morsels_sales.csv")

# Convert Date to datetime and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsels Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsels Sales Visualiser",
        style={"textAlign": "center"}
    ),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
