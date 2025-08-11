import streamlit as st 

colorsdict = {'Mio':['Blue ball'], 'Moses':['Red ball'], 'Mr.Tee':['Green ball']}


st.write(colorsdict)

st.table(colorsdict)

name = st.text_input('Please enter your name')

englishscore = st.number_input('Enter your english scores',0,100)
sciencescore = st.number_input('Enter your science scores',0,100)

totalscore = englishscore + sciencescore

if st.button('Create table'):

    studentdict = {'Name':name,'Engish Scores':englishscore,'Science Score':sciencescore,'Total Score':totalscore}
    st.write(studentdict)
    st.table(studentdict)
