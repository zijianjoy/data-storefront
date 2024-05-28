
import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    start_year = st.number_input("Mortgage start year", value=2019)
    st.write("The Mortgage start year is ", start_year)

with col2:
    interest_rate = st.number_input("Interest Rate", value=3.25)
    st.write("Interest Rate is ", interest_rate, "%")

with col3:
    payment = st.number_input("monthly payment", value=4000)
    st.write("Monthly payment ", payment, "dollars")

with col4:
    original_debt = st.number_input("original_debt", value=900000)
    st.write("The original_debt is ", original_debt, "dollars")

with col5:
    mortgage_length = st.number_input("mortgage in year", value=30)
    st.write("The mortgage year ", mortgage_length, " years")