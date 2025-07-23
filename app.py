from flask import Flask,request,render_template
import numpy as np 
import pandas as pd 

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from src.pipeline.train_pipeline import TrainPipeline, check_artifacts_exist

application = Flask(__name__)
app=application

def ensure_artifacts_exist():
    """
    Check if model artifacts exist, if not, run the training pipeline
    """
    if not check_artifacts_exist():
        print("Artifacts not found. Running training pipeline...")
        try:
            train_pipeline = TrainPipeline()
            r2_score = train_pipeline.initiate_training()
            print(f"Training pipeline completed successfully! R² Score: {r2_score}")
        except Exception as e:
            print(f"Error in training pipeline: {str(e)}")
            raise e
    else:
        print("Artifacts found. Skipping training pipeline.")

# Run the training pipeline check when the app starts
ensure_artifacts_exist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method== 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    
if __name__=="__main__":
        app.run(host="0.0.0.0")