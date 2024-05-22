import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

#membuat header dan teks
st.write("""
# Iris Prediksi

 prediksi saja
""")
st.sidebar.header('User Input Parameters'
)

#membuat fungsi user input
def user_input():
    sepal_length=st.sidebar.slider('Separ Length',4.2,8.0,5.5)
    separ_width=st.sidebar.slider('Sepal Width',2.0,4.0,3.3)#start,stop,step
    petal_length=st.sidebar.slider('Petal Length',1.0,2.5,0.4)
    petal_width=st.sidebar.slider('Petal Width',0.1,2.5,1.5)
    data={'sepal_length':sepal_length,
          'sepal_width':separ_width,
          'petal_length':petal_length,
          'petal_width':petal_width}
    fetures=pd.DataFrame(data,index=[0])
    return fetures

df=user_input()
st.subheader('User Inputan')
st.write(df)

iris=datasets.load_iris()
X=iris.data
Y=iris.target

clf=RandomForestClassifier()
clf.fit(X,Y)


prediction=clf.predict(df)
prediction_proba=clf.predict_proba(df)


st.write('### Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)


