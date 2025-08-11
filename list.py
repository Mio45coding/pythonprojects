import streamlit as st

packing_list = st.selectbox ('Input an item that is essentiall for the  trip',['toothbrush', 'Electronic devices', 'USB ports', 'Clothes', 'Money', 'Passports', 'Food'])


st.write ('The packing essential is',packing_list,'.')