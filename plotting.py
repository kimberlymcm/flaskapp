import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json


def create_barplot(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time.S"], y=df["payload.M.pm1.N"], name="pm1"))
    fig.add_trace(go.Scatter(x=df["time.S"], y=df["payload.M.pm10.N"], name="pm10"))
    fig.add_trace(go.Scatter(x=df["time.S"], y=df["payload.M.pm25.N"], name="pm25"))
    fig.update_layout(title="PM", xaxis_title="time", yaxis_title="ug/m^3", legend_title="particles")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    #data = [go.Bar(x=df["time.S"], y=df["payload.M.pm1.N"]),
    #        go.Bar(x=df["time.S"], y=df["payload.M.pm10.N"]),
    #        go.Bar(x=df["time.S"], y=df["payload.M.pm25.N"])]
    #graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON 


def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
