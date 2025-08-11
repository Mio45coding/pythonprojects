import streamlit as st
 
#simple test
#ask for the name and -age - use a radio to ask for gender
#-use a selectbox to ask to choose best color - use a type to ask best game
#-use a type to ask to type best movie - use a type to ask best friend
#create a submit button and show this in a success bar
#Jeida (F), your best game is: Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe


name = st.text_input ('What is your name?')

age = st.number_input('How old are you?')

gender = st.radio('Select your gender.',['Male','Female'])

st.write(name,'your gender is',gender,'.')

favrioutecolour = st.selectbox('Choose your favrioute colour.',['Blue','Red','Yellow','Black','Green','White','Brown','Purple','Pink','Orange'])
st.write(name,'your favrioute colour is',favrioutecolour,'.')

bestgame = st.text_input('What is your favrioute game?')

favrioutemovie = st.text_input('What is your favrioute movie?')

bestfriend = st.text_input('Who is your best friend?')

st.success('This is the button to submit the form.')
if st.button('Submit'):
    st.write('Thank you')


st.write (name,'your favrioute game is',bestgame,',your favrioute colour is',favrioutecolour,',your favrioute movie is',favrioutemovie,',your best friend is',bestfriend,'.')



