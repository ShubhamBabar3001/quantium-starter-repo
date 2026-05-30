import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Initialize the Dash application
app = Dash(__name__)

# Load and sort the formatted data by date
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# Create the line chart with appropriate titles and axis labels
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

# Define the layout of the application
app.layout = html.Div(children=[
    html.H1(
        children="Soul Foods Sales Visualizer",
        style={"textAlign": "center", "fontFamily": "sans-serif"}
    ),

    html.P(
        children="Visualizing the impact of the Pink Morsel price increase on January 15, 2021.",
        style={"textAlign": "center", "fontFamily": "sans-serif"}
    ),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# Run the application local server
if __name__ == "__main__":
    app.run(debug=True)