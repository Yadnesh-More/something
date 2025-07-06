import streamlit as st
import joblib
model_nb = joblib.load('spam-ham')
st.title('SPAM-HAM CLASSIFIER')
ip = st.text_input('Enter the message') 
op = model_nb.predict([ip])
if st.button('Predict'):
  st.title(op[0])
