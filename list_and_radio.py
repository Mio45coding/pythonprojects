import streamlit as st

name = st.text_input('Enter your name')

bestF1driver = st.selectbox('Choose your best driver',['Hamilton','Michael Schumacher','Verstappen','Senna','Leclerc'])

st.write(name,'your best driver is',bestF1driver)


fruits = st.radio('Select your fruit',['Watermelon','Strawberry'])

st.write(name,'you chose a ',fruits)