import streamlit as st

name = st.text_input('Enter your name')

weeklyscores = st.write('Enter your weekly scores.')

left, right = st.columns(2)

with left:
    pythonscores = st.number_input('Enter your python scores.',0,100)
    webdevelopmentscores = st.number_input('Enter your web development scores.',0,100)
    mobileappsscores = st.number_input('Enter your mobile app scores.',0,100)
    graphicsdesignscores = st.number_input('Enter your graphics design scores.',0,100)

with right:
    roboticscores = st.number_input('Enter your robotics scores.',0,100)
    problemsolvingscores = st.number_input('Enter your problem solving scores.',0,100)
    codingpuzzlescores = st.number_input('Enter your coding puzzels score.',0,100)
    uiuxdesignscores = st.number_input('Enter your UI/UX design scores',0,100)

if st.button('Check student scores'):
    totalscore = pythonscores+webdevelopmentscores+mobileappsscores+graphicsdesignscores+roboticscores+problemsolvingscores+codingpuzzlescores+uiuxdesignscores
    average = totalscore/8

    if average>=90:
        grade='Platinum'
    elif average>=80:
        grade='Gold'
    elif average>=70:
        grade='Silver'
    elif average>=60:
        grade='Bronze'
    elif average<60:
        grade='Participant'
    st.write(name,'your total score is',totalscore,'and your average is ',average,'. Your achievement badge is ',grade)
