import streamlit as st

book_list = st.selectbox ('Select a book:',['Harry Potter 1', 'Harry Potter 2', 'Harry Potter 3', 'Harry Potter 4', 'Harry Potter 5' ])
st.write ('The book you chose is',book_list,'.')