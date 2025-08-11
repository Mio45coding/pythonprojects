import streamlit as st



studentdict = {'Name':name,'Subjects':subjects,'total':total,'average':average,'grade':grade}


st.write(studentdict)
st.table(studentdict)