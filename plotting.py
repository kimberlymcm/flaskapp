import json

import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np


def create_barplot1(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time"], y=df["pm1"], name="pm1"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["pm10"], name="pm10"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["pm25"], name="pm25"))
    fig.update_layout(title="Particulate Matter", xaxis_title="Time", yaxis_title="ug/m^3",
        legend_title="Particulate Size", font=dict(family="Open Sans", size=10),
        margin=dict(l=35, r=15, b=30, t=30))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON 


def create_barplot2(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time"], y=df["temperature"], name="temperature (C)"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["humidity"], name="humidity"))
    fig.update_layout(title="Temperature and Humidity", xaxis_title="Time", yaxis_title="",
        font=dict(family="Open Sans", size=10),
        margin=dict(l=35, r=15, b=30, t=30))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def create_barplot3(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time"], y=df["oxidised"], name="oxidised"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["reduced"], name="reduced"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["nh3"], name="nh3"))
    fig.update_layout(title="Gases", xaxis_title="Time", yaxis_title="", legend_title="Gases",
        font=dict(family="Open Sans", size=10),
        margin=dict(l=35, r=15, b=30, t=30))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
