import streamlit as st

st.header('Mio Meal Store')

st.image('https://img.freepik.com/free-vector/flat-design-fast-food-sale-banner_23-2149165450.jpg?semt=ais_hybrid&w=740')

st.subheader('Meal Category')

meal1, meal2, meal3 = st.columns(3)

Bill = 0

with meal1:
    if st.checkbox('Burgers: $10'):
        Bill += 10
        st.success('Ok Done')

with meal2:
    if st.checkbox("Fries: $ 8"):
        Bill += 8
        st.success('OK Done')

with meal3:
    if st.checkbox('Fried Chicken 9pcs: $15'):
        Bill +=15
        st.success("Ok Done")


st.subheader('Drinks Category')

st.image('https://media.istockphoto.com/id/1145763223/vector/refreshing-soft-drink-banner-ads.jpg?s=170667a&w=0&k=20&c=bc7C5hpQQusm5CfU-PlNqx_gS0OJv479LWwv6QtdB6M=')

drinks1, drinks2, drinks3 = st.columns(3)

with drinks1:
    if st.checkbox("Cold Water: $5"):
        Bill +=5
        st.success("Ok Done")

with drinks2:
    if st.checkbox("Fizzy Drinks: $8"):
        Bill +=8
        st.success("Ok Done")

with drinks3:
    if st.checkbox("Apple Juice: $9"):
        Bill +=9
        st.success("Ok Done")

st.subheader('Fruit Category')

st.image('https://i.ytimg.com/vi/EU4Amhj-0JI/maxresdefault.jpg')

fruit1, fruit2, fruit3 = st.columns(3)

with fruit1:
    if st.checkbox("Watermelon: $10"):
        Bill+=10
        st.success("Ok Done")
with fruit2:
    if st.checkbox("Strawberries $8"):
        Bill+=8
        st.success("Ok Done")
with fruit3:
    if st.checkbox("Apple: $7"):
        Bill+=7
        st.success("Ok Done")




if st.button('Check my bill'):
    st.write('Your bill is $',Bill,'.')