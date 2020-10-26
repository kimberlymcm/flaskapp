import json

import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np


def create_barplot1(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time"], y=df["payload.pm1"], name="pm1"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["payload.pm10"], name="pm10"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["payload.pm25"], name="pm25"))
    fig.update_layout(title="PM", xaxis_title="time", yaxis_title="ug/m^3", legend_title="particles")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON 


def create_barplot2(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time"], y=df["payload.temperature"], name="temperature (C)"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["payload.humidity"], name="humidity"))
    fig.update_layout(title="Temp / Humidity", xaxis_title="time", yaxis_title="", legend_title="More things")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def create_barplot3(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time"], y=df["payload.oxidised"], name="oxidised"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["payload.reduced"], name="reduced"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["payload.nh3"], name="nh3"))
    fig.update_layout(title="Gases", xaxis_title="time", yaxis_title="", legend_title="More things")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
