import streamlit as st

initial_savings = 500

phone_cost = st.number_input ('How much did you spend on the new phone Sarah?')
clothes_cost = st.number_input ('How much did you spend on the new clothes Sarah?')
book_cost = st.number_input ('How much did you spend on the new books Sarah?')
decoration_cost = st.number_input ('How much did you spend on the decoration Sarah?')
dinner_cost = st.number_input ('How much did you spend on the special dinner Sarah?')

remaining_balance = initial_savings - phone_cost - book_cost - decoration_cost - dinner_cost

personal_shopping = st.number_input ('Sarah how much do you want to allocate for personal shopping?')

final_amount = remaining_balance - personal_shopping

if st.button ('Check balance.'):
    if personal_shopping > remaining_balance:
        st.text ('You need to reduce your shopping amount.')

    else:
     st.text ('The final amount you spent is',final_amount,'.')