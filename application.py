from flask import Flask, jsonify, render_template, request
#import plotly
#import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

from plotting import create_barplot
import aws_controller

application = app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    json_data = aws_controller.get_data(items=["pm1", "pm10", "pm25"])
    df = pd.json_normalize(json_data) # dataframe of device_time #timestamp payload.pm25
    #df_pivot = df.wide_to_long(stubnames="payload", i=["time.S"], j=["pm"])
    print(df.head())
    # Normalize
    final_plot = create_barplot(df)
    return(render_template('index.html', plot=final_plot))



if __name__ == '__main__':
    application.run(debug=True, use_reloader=False)

