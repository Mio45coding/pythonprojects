import streamlit as st

firstnum = st.number_input('Enter the first number.')
secondnum = st.number_input('Enter the second number.')

total = firstnum + secondnum

multi = firstnum*secondnum


numbers = {'First number':firstnum,'Second number':secondnum,'Total added':total,'Total Multiplied':multi}

st.write(numbers)

st.table(numbers)
