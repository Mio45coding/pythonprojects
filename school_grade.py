import streamlit as st 
import pandas as pd

try:
    studentfile = pd.read_csv('school_grade.csv')
except:
    studentfile= pd.DataFrame()


st.subheader('Welcome to the Mio International School.')

menu = st.sidebar.selectbox('Menu',['Input Student Scores','View Student Table'])

if menu == 'Input Student Scores':
    st.table(studentfile)

if menu == 'View Student Table':
    name = st.text_input('Enter student name.')


    
    left, right = st.columns(2)

    with left:
        mathscores = st.number_input('Enter student math scores',0,100)
        englishscores = st.number_input('Enter student english scores',0,100)
        chinesescores = st.number_input('Enter student chinese scores',0,100)

    with right:
     sciencescores = st.number_input('Enter student science scores',0,100)
     historyscores = st.number_input('Enter student history scores',0,100)
     codingscores = st.number_input('Enter student coding scores',0,100)


    if st.button('Check student scores'):
        totalscore = mathscores+chinesescores+englishscores+sciencescores+historyscores+codingscores
        average = totalscore/6

        if average>=90:
            grade = 'A'
        elif average>=80:
            grade = 'B'
        elif average>=70:
            grade = 'B-'
        elif average>=60:
            grade = 'C'
        elif average>=50:
            grade = 'D'
        elif average<50:
            grade = 'F'
        st.write(name,'your total score is',totalscore,'and your average is',average,'your grade is',grade)


        studentdict = {'Name':[name],'total':[totalscore],'average':[average],'grade':[grade]}


        st.write(studentdict)
        st.table(studentdict)
        student_table = pd.DataFrame(studentdict)
        join_tables = pd.concat([studentfile,student_table],ignore_index=True)
        join_tables.to_csv('school_grade.csv',index=False)
        st.success('Saved Successfully')


 