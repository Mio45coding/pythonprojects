import streamlit as st 
st.divider()
MENU = st.sidebar.selectbox('Menu',['Home','Registration','Contact us'])

if MENU == 'Home':
    st.write('SCHOOL DESIGN APP')
    st.write('Welcome to Mio School')
    st.image ('https://img.freepik.com/premium-vector/school-building-illustration_638438-385.jpg?semt=ais_hybrid&w=740')

if MENU == 'Registration':
    st.write('Bio Data')
    st.divider()
    fullname = st.text_input('Enter your full name', placeholder= 'Full Name')
    Parentname = st.text_input('Enter your parent name', placeholder= 'Parent Name')
    Age = st.number_input('Enter your age', min_value=6, max_value=14)
    Address = st.text_input('Enter your address', placeholder= 'Address')
    if st.button('Submit',type='primary'):
        if 6 <= Age <= 14:
            st.write(fullname, 'you are eligable for registration.')

    st.write('Call our school secetary for enquiries.')

if MENU == 'Contact us':
    st.write('Contact us')
    st.write('For more info call +85296860404')
    st.write('Email us at Mioschool@gmail.com.')

