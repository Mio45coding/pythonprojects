import streamlit as st 

name = st.text_input('What is your name?')

steps = st.number_input('How many steps have you walked?')

if steps >= 20000:
    st.write('....')

elif steps >= 10000 and steps < 20000:
    st.write('...')