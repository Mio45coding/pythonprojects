import streamlit as st

st.write("This is a fresh new code")

st.header('Age Calculator')

name = st.text_input("Please enter your name")

yob = st.number_input('Please enter your year of birth',0)

current = st.number_input("Please enter your current year",0)

age = current - yob

if st.button('Click this button to see your age.'):
    st.write('Dear',name,'your age is',age,"in year",current,".")
     