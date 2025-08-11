import streamlit as st
st.title('Bus stops')
st.subheader ('Mio.s bus stop')
st.image ('https://png.pngtree.com/png-vector/20220907/ourlarge/pngtree-bus-station-png-image_6140913.png')

bus_stops = ['Market','School','Hospital']
st.write(bus_stops)

st.write('The first bus stop is',bus_stops[0])
bus_stops.append('Stadium')
st.write (bus_stops)
st.write(len(bus_stops))