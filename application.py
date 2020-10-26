from flask import Flask, jsonify, render_template, request
import pandas as pd
import numpy as np
import json

from plotting import create_barplot1, create_barplot2, create_barplot3
import aws_controller

application = app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    df = aws_controller.get_data()
    final_plot = create_barplot1(df)
    final_plot2 = create_barplot2(df)
    final_plot3 = create_barplot3(df)
    return(render_template('index.html', plot1=final_plot, plot2=final_plot2, plot3=final_plot3))



if __name__ == '__main__':
    application.run(debug=True, use_reloader=False)

