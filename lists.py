import streamlit as st 

st.title ('Things to bring')

packing_list = []
item = st.text_input('Add an item to bring for  the trip:')
packing_list.append(item)
st.write(packing_list)

packing_list = st.selectbox ('Input an item that is essentiall for the  trip',['toothbrush', 'Electronic devices', 'USB ports', 'Clothes', 'Money', 'Passports', 'Food'])


st.write ('The packing essential is',packing_list,'.')