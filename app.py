import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk

model=pk.load(open("house.pkl",'rb'))
st.header('R² House Price Predictor')
df=pd.read_csv(r"C:\Users\ranji\OneDrive\Desktop\House price prediction\House_clean.csv")

Year = st.slider('Select a Year',1900,2024)
Sqft=st.slider('Select a SQFT',100,100000)
Bedrooms=st.slider('Number of Bedrooms',0,5)
Bathrooms=st.slider("Number of Bathrooms",0,5)
Floors=st.slider("Number of Floors",0,5)

inputmodel=pd.DataFrame([[Year,Sqft,Bedrooms,Bathrooms,Floors]],columns=['Year','Sqft','Bedrooms','Bathrooms','Floors'])

if st.button("Predict Price"):
    output=model.predict(inputmodel)
    st.markdown('House price is going to be'+str(output))