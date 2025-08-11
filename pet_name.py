import streamlit as st

st.title('Pet names')

pet_names = ['Peanut', 'fluffy','Bugs']
st.write(pet_names)
st.write('The cats name will be', pet_names[1])

pet_names.append("Parrot")
st.write(pet_names)
st.write(len(pet_names))
st.write('You have 4 pets in total.')
