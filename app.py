import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
st.title('Medical Diagnostic WebApp ')

#post streamlit action

#Step 1: Load the model

model = open('rfc.pickle','rb')
clf = pickle.load(model)
model.close()

#step2: Get the front end user input
pregs = st.number_input('Pregnancies',1,20,step=1)
glucose= st.slider('Glucose',40.0,200.0,40.0)
bp= st.slider('BloodPressure',24,122,24)
skin= st.slider('SkinThickness',7,99,7)
Insulin= st.slider('Insulin',18.0,850.0,18.0)
bmi= st.slider('BMI',18.0,67.0,18.0)
dpf= st.slider('DiabetesPedigreeFunction',0.05,2.5,0.05)
age= st.slider('Age',21,81,21)

#step3: converting user input to model input

data={'Pregnancies':pregs, 'Glucose':glucose, 'BloodPressure':bp, 'SkinThickness':skin, 'Insulin':Insulin,
       'BMI':bmi, 'DiabetesPedigreeFunction':dpf, 'Age':age}

input_data = pd.DataFrame([data])


#step4: Get the predictions

preds = clf.predict(input_data)[0]
if st.button('Predict'):
       if preds==1:
              st.error('The person has Diabetes')
       if preds==0:
              st.success('The person is Diabetes Free')
