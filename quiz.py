import streamlit as st

name = st.text_input('Please enter your name')

q1 = st.text_input ('What color is the sky on a sunny day?')

q2 = st.text_input ('How many legs does a spider have?')

q3 = st.text_input ('What do we use to brush our teeth?')

q4 = st.text_input ('What animal says “meow”?')

q5 = st.text_input ('What is the name of the shape with three sides?')

q6 = st.text_input ('What do you call a baby dog?')

q7 = st.text_input ('How many days are in a week?')

q8 = st.text_input ('What do we drink when we are thirsty?')

q9 = st.text_input ("What is the opposite of “hot”?")

q10 = st.text_input ('What do we use to write on paper?')

st.write ('Great job!',name,'you answered all the fun questions. Keep learning and having fun!')