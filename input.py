# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:25:40 2021

@author: dell
"""

from pydantic import BaseModel

class Loan(BaseModel):
   Gender: int
   Married: int
   Education: int
   Self_Employed: int
   ApplicantIncome: int
   CoapplicantIncome: float
   LoanAmount: float
   Loan_Amount_Term: float
   Credit_History: float
   Property_Area: int
   Dependents: int



