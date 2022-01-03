from flask import Flask, jsonify, render_template, request
import pandas as pd
import numpy as np
import json

import plotting
import aws_controller

application = app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    df = aws_controller.get_data()
    final_plot = plotting.create_barplot1(df)
    final_plot2 = plotting.create_barplot2(df)
    final_plot3 = plotting.create_barplot3(df)
    final_plot4 = plotting.create_barplot4(df)
    return(render_template('index.html', plot1=final_plot, plot2=final_plot2,
        plot3=final_plot3, plot4=final_plot4))



if __name__ == '__main__':
    application.run(debug=True, use_reloader=False)

