import streamlit as st

supplies = ['notebook','pen','eraser']
st.write(supplies)
st.write('The last item in the list is', supplies[2])
supplies.append('Ruler')
st.write(supplies)
st.write(len(supplies))