import streamlit as st

expense = st.title ('EXPENSE PLANNER')

name = st.text_input ('What is your name?')
monthly_income = st.number_input ('What is your total monthly income?')
rent = st.number_input ('What is your monthy rent?')
groceries = st.number_input ('What is your monthy groceries expense?')
transportation = st.number_input ('What is your monthly transportation codt?')
other_expenses = st.number_input ('Is there any other monthly expense?')

total_expenses = monthly_income + rent + groceries + transportation + other_expenses

remaining_balance = total_expenses - monthly_income

if remaining_balance >=500:
    st.write ('Great job',name,'! You have',remaining_balance,'left. Consider saving or iinvesting some of it!')

elif 0<= remaining_balance <=500:
    st.write ('Nice work',name,'! You have $',remaining_balance,'left. This is a good amount for savings or leisure.')

else: 
    st.write('Oops',name,'! You are over budget by $',remaining_balance,'. Consider cutting bsck on expenses')