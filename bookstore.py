import streamlit as st

st.title('Mios Bookstore')

products = {'Stocks':['Comic Books, 10 On Stock','History Books, 5 On Stock','Story Books, 7 On Stock'],
            'Product price':['$20','$30','$15',],'Product discout':['2%','%5','4%'],'Copies sold':['15 sold','20 sold','10 sold']}

st.write(products)
st.table(products)

