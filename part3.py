#import library
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Predict Penguin

Ini adalah **Palmer Penguins**
""")

st.sidebar.header('User Input Fetures')


#upload file 
upload_file=st.sidebar.file_uploader('Masukan file',type=['csv'])
if upload_file is not None:
    input=pd.read_csv(upload_file)
else:
    def user_input():
        islan=st.sidebar.selectbox('Islan',('Biscoe','Dream','Torgersen'))
        sex=st.sidebar.selectbox('Sex',('Male','Female'))
        bill_length_mm=st.sidebar.slider('Bill Length(mm)',32.1,59.6,45.0)
        bill_depth_mm=st.sidebar.slider('Bill Depth(mm)',13.0,22.0,15.0)
        flipper_length_mm=st.sidebar.slider('Flipper Length(mm)',172.0,230.0,201.0)
        body_mass_g=st.sidebar.slider('Body mass (g)',2700.0,6300.0,4207.0)
        data= {'island':islan,
               'bill length':bill_length_mm,
               'bill depth':bill_depth_mm,
               'fliper':flipper_length_mm,
               'bodyy':body_mass_g,
               'sex':sex}
        features=pd.DataFrame(data,index=[0])
        return features
    input=user_input()

penguins=pd.read_csv('penguins_cleaned.csv')
penguins=penguins.drop(columns=['species'])
df=pd.concat([input,penguins],axis=0)
encode=['sex','islan']
for col in encode:
    dummy=pd.get_dummies(df[col],prefik=col)
    df=pd.concat([df,dummy],axis=1)
    del df[col]

df=df[:1]

st.subheader('User Input Features')

if upload_file is not None:
    st.write(df)

else:
    st.write('Awaiting Csv to be uploaded')
    st.write(df)
st.subheader('Prediction')
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)