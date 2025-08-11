import streamlit as st

st.header ("Build Your Dream House!")

st.subheader('Rooms')

bedroom, bathroom, livingroom, kitchen, studyroom, diningroom, gameroom,libary, guestroom, basement = st.columns(10)

Bill = 0

with bedroom:
    if st.checkbox('Bedroom: $50'):
        Bill+=50
        st.success('Ok done.')
with bathroom:
    if st.checkbox('Bathroom: $40'):
        Bill+=40
        st.success('Ok done.')
with livingroom:
    if st.checkbox('Living Room: $60'):
        Bill+=60
        st.success('Ok done.')
with kitchen:
    if st.checkbox('Kitchen: $70'):
        Bill+=70
        st.success('Ok done.')
with studyroom:
    if st.checkbox('Study Room: $45'):
        Bill+=45
        st.success('Ok done.')
with diningroom:
    if st.checkbox('Dining Room: $55'):
        Bill+=55
        st.success('Ok done.')
with gameroom:
    if st.checkbox('Game Room: $65'):
        Bill+=65
        st.success('Ok done.')
with libary:
    if st.checkbox('Libary: $60'):
        Bill+=60
        st.success('Ok done.')
with guestroom:
    if st.checkbox('Guest Room: $50'):
        Bill+=50
        st.success('Ok done.')
with basement:
     if st.checkbox('Basement: $80'):
        Bill+=80
        st.success('Ok done.')


st.header ('Furniture & Decorations')

Bed, Couch, Tv, Diningtable, desk, Curtains, Rug, Wardrobe, Bookshelf, painting = st.columns(10)

with Bed:
    if st.checkbox('Bed: $40'):
        Bill+=40
        st.success('Ok done.')
with Couch:
    if st.checkbox('Couch: $30'):
        Bill+=30
        st.success('Ok done.')
with Tv:
    if st.checkbox('Tv: $35'):
        Bill+=35
        st.success('Ok done.')
with Diningtable:
    if st.checkbox('Dining Table: $45'):
        Bill+=45
        st.success('Ok done.')
with desk:
    if st.checkbox('Desk: $25'):
        Bill+=25
        st.success('Ok done.')
with Curtains:
    if st.checkbox('Curtains: $15'):
        Bill+=15
        st.success('Ok done.')
with Rug:
    if st.checkbox('Rug: $10'):
        Bill+=10
        st.success('Ok done.')
with Wardrobe:
    if st.checkbox('Wardrobe: $30'):
        Bill+=30
        st.success('Ok done.')
with Bookshelf:
    if st.checkbox('Bookself: $25'):
        Bill+=25
        st.success('Ok done.')
with painting:
    if st.checkbox('Painting: $20'):
        Bill+=20
        st.success('Ok done.')


st.subheader('Utiliy Add-Ons')

airconditioner, heater, securitysystem,smartlighting,waterpurifier,wifirouter,generator,inverter,surveillancecamera,homeassistantdevice = st.columns(10)

with airconditioner:
    if st.checkbox('Air Conditioner: $60'):
        Bill+=60
        st.success('Ok done.')
with heater:
    if st.checkbox('Heater: $50'):
        Bill+=50
        st.success('Ok done.')
with securitysystem:
    if st.checkbox('Security System: $90'):
       Bill+=90
       st.success('Ok done.')
with smartlighting:
    if st.checkbox('Smart Lighting: $40'):
        Bill+=40
        st.success('Ok done.')
with waterpurifier:
    if st.checkbox('Water Purifier: $35'):
        Bill+=35
        st.success('Ok done.')
with wifirouter:
    if st.checkbox('Wifi Router: $20'):
         Bill+=20
         st.success('Ok done.')
with generator:
    if st.checkbox('Generator: $80'):
        Bill+=80
        st.success('Ok done.')
with inverter:
    if st.checkbox('Inverter: $70'):
        Bill+=70
        st.success('70')
with surveillancecamera:
    if st.checkbox('Surveillance Camera: $55'):
        Bill+=55
        st.success('Ok done')
with homeassistantdevice:
    if st.checkbox('Home Assistant Device: $45'):
        Bill+=45
        st.success('Ok done.')
