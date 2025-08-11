import streamlit as st

st.title ('PIZZA ORDER FORM')

name = st.text_input ('Enter your name.')

Size= st.radio('Select your size',['Small','Medium', 'Large'])

toppings  = st.selectbox ('Please select a topping.',['Pepperoni','Mushrooms','Extra Cheese','Olives'])

display_message = st.write ('Thank you',name,'! You have ordered a ',Size,'piizza with',toppings,'.')