import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Initialize the Dash application
app = Dash(__name__)

# Load and sort the formatted data by date
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# Define component styling
COLORS = {
    "background": "#f9f9f9",
    "card_background": "#ffffff",
    "text": "#2c3e50",
    "primary": "#16a085"
}

# Define the layout of the application
app.layout = html.Div(
    style={
        "backgroundColor": COLORS["background"],
        "fontFamily": "Segoe UI, Tahoma, Geneva, Verdana, sans-serif",
        "padding": "40px",
        "minHeight": "100vh"
    },
    children=[
        html.Div(
            style={
                "backgroundColor": COLORS["card_background"],
                "padding": "30px",
                "borderRadius": "8px",
                "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                "maxWidth": "1000px",
                "margin": "0 auto"
            },
            children=[
                html.H1(
                    children="Soul Foods Sales Visualizer",
                    style={
                        "textAlign": "center",
                        "color": COLORS["text"],
                        "marginBottom": "10px"
                    }
                ),

                html.P(
                    children="Visualizing the impact of the Pink Morsel price increase on January 15, 2021.",
                    style={
                        "textAlign": "center",
                        "color": "#7f8c8d",
                        "marginBottom": "30px"
                    }
                ),

                html.Div(
                    style={
                        "textAlign": "center",
                        "marginBottom": "25px",
                        "padding": "10px",
                        "border": f"1px solid {COLORS['background']}",
                        "borderRadius": "4px"
                    },
                    children=[
                        html.Label(
                            "Filter by Region:",
                            style={
                                "fontWeight": "bold",
                                "marginRight": "15px",
                                "color": COLORS["text"]
                            }
                        ),
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"}
                            ],
                            value="all",
                            inline=True,
                            labelStyle={
                                "marginRight": "15px",
                                "color": COLORS["text"],
                                "cursor": "pointer"
                            }
                        )
                    ]
                ),

                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)


# Callback to update the graph based on the selected region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
        title_suffix = "All Regions"
    else:
        filtered_df = df[df["region"] == selected_region]
        title_suffix = f"{selected_region.capitalize()} Region"

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time — {title_suffix}",
        labels={"date": "Date", "sales": "Total Sales ($)"}
    )

    fig.update_layout(
        plot_bgcolor=COLORS["card_background"],
        paper_bgcolor=COLORS["card_background"],
        font_color=COLORS["text"]
    )

    return fig


# Run the application local server
if __name__ == "__main__":
    app.run(debug=True)