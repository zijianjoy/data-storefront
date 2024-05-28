
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


# Calculate the years which are x-axis numbers.
x = [start_year + i for i in range(mortgage_length)]
y = [original_debt]

# Calculate new year mortgage balance based on last year data
for i in range(1, mortgage_length):
    last_year_index = i - 1
    base = y[last_year_index]
    balance = base * (1 + (interest_rate * 0.01)) - payment * 12
    y.append(balance)

import pandas as pd
df = pd.DataFrame({
    "year": x,
    "balance": y,
})

import plotly.express as px
fig = px.bar(df, x="year", y="balance", color='balance')
st.plotly_chart(fig, use_container_width=True)
