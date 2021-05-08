# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:37:41 2021

@author: dell
"""

import uvicorn   #  ASGI Request
from fastapi import FastAPI
from input import Loan
import numpy as np
import pickle
import pandas as pd
import os

app = FastAPI()
pickle_in = open("random_forest_classifier_model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def base_route():
  return {'message': 'Welcome to Praxis'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

@app.post('/predict')
def predict_Loan(data: Loan):
  data = data.dict()
  Gender = data['Gender']
  Married = data['Married']
  Education = data['Education']
  Self_Employed = data['Self_Employed']
  ApplicantIncome = data['ApplicantIncome']
  CoapplicantIncome = data['CoapplicantIncome']
  LoanAmount = data['LoanAmount']
  Loan_Amount_Term= data['Loan_Amount_Term']
  Credit_History = data['Credit_History']
  Property_Area = data['Property_Area']
  Dependents = data['Dependents']
  prediction = classifier.predict([[Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
                                    LoanAmount,Loan_Amount_Term,Credit_History ,Property_Area,
                                    Dependents]])
  if(prediction==1):
    prediction="Loan Approved"
  else:
    prediction="Loan Not Approved"
  return {'Prediction': prediction}

if __name__=="__main__": 
  port = int(os.environ.get("PORT",8000))
  uvicorn.run(app, host='127.0.0.1', port=port)
  #uvicorn main:app --reload

