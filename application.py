#libraries
from flask import Flask, request,render_template
'''
Flask → Creates the web application / API server.
request → Handles incoming HTTP request data (like JSON, form inputs).
render_template → Renders HTML templates and sends them to the browser.
'''
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

#*************************
application = Flask(__name__)

app = application

#creating route for homepage of app
@app.route('/')
def index():
    return render_template('index.html') # render_template will search the templates folder 
#routte for predicting and method which it support
@app.route('/prediction',methods = ['GET','POST'])
def predict_datapoint():
    # here we will do everything from gething the data make prediction
    if request.method =='GET':
        return render_template('home.html')
    # in post part we do bring the data, scaling and all
    else :
        # creat the data for that we make own customeData[the CustomeData class is created in prediction_pipline.py]
        data= CustomData(
            # we will try to read all the values 
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            math_score=float(request.form.get('math_score')),
            reading_score=float(request.form.get('reading_score'))
            
        )
        # using function from customdata class to convert the data into datafram
        pred_df = data.get_data_as_data_frame()
        # if u want how your df look like print it 
        print(pred_df)

        # making object of PredictPipeline class present in prediction_pipline
        predict_pipline = PredictPipeline()
        # now give the i/p data and predict and store into results
        results = predict_pipline.predict(pred_df)
        return render_template('home.html', results = results[0]) #because it returning into list format and we read this result value in html to return the final prediction in frontend 
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)