import streamlit as st

car_name = st.text_input('What is the cars name?')

distance = st.number_input('What is the distance the car traveled in meters?')

time = st.number_input('How long did it take? Answer in seconds.')


if st.button ('Click this button to see if your driving safe.'):
    speed = distance/time 
    st.write(speed)
    if speed > 30:
        st.write ('Warning,',car_name,'! Your speed is',speed,'m/s. Drive carefully')

    elif speed > 20 and speed < 30:
        st.write ('Caution,',car_name,'! Your speed is ',speed,'m/s. Drive carefully.')

    elif speed < 20:
        st.write ('Safe,',car_name,'! Your speed is',speed,'m/s. You aare driving safely.')

    if time == 0:
        st.write('Error: TIme cannot be zero. Please check the input values for',car_name,'.')
