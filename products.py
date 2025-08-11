import streamlit as st
products = {'Product name':['Furniture','Stationary','Toys','Computers','Food'],'Product price':['$200','$12','$10','$1000','30'],
            'Product discount':['5%','0%','10%','15%','30%'],'Product sold':['10 sold','100 sold','50 sold','20 sold','200 sold']}

st.write(products)
st.table(products)
#products = {'First product':product1,'Second product':product2,'Third product':product3,'Fourth product':product4,'Fifth product':product5}