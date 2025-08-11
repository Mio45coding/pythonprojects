import streamlit as st #page for your python app

#to run your project, click + and type; streamlit run projectname.py

st.title('This is a title')

st.header('This is a header')

st.subheader('This is a subheader')

st.write('THis is a normal text')

if st.button('Click to view'):
    st.write('Thank you')