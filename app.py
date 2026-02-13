import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("pink_morsels_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "20px",
        "fontFamily": "Arial"
    },
    children=[

        # Header
        html.H1(
            "Pink Morsels Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }
        ),

        # Radio buttons
        html.Div(
            style={
                "width": "60%",
                "margin": "auto",
                "padding": "15px",
                "backgroundColor": "white",
                "borderRadius": "10px",
                "boxShadow": "0px 4px 10px rgba(0,0,0,0.1)",
                "marginBottom": "30px",
                "textAlign": "center"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "fontWeight": "bold",
                        "marginRight": "15px"
                    }
                ),
                dcc.RadioItems(
                    id="region-radio",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px"}
                )
            ]
        ),

        # Graph container
        html.Div(
            style={
                "width": "90%",
                "margin": "auto",
                "padding": "20px",
                "backgroundColor": "white",
                "borderRadius": "10px",
                "boxShadow": "0px 4px 10px rgba(0,0,0,0.1)"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# Callback to update graph
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
    filtered_df,
    x="Date",
    y="Sales",
    color="Region",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    },
    title="Sales Trend Over Time"
    )

# 🔥 ADD THIS STYLING
    fig.update_layout(
        plot_bgcolor="#f4f6f9",     # chart area
        paper_bgcolor="white",      # outside chart
        font=dict(color="#2c3e50"),
        title_font_size=20,
        legend_title_text="Region"
    )

    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
