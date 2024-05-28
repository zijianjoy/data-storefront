
import streamlit as st

st.title("Mortgage Balance Projection")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    start_year = st.number_input("Mortgage start year", value=2019)
    st.write("The Mortgage start year is ", start_year)

with col2:
    interest_rate = st.number_input("Interest Rate", value=3.25)
    st.write("Interest Rate is ", interest_rate, "%")

with col3:
    payment = st.number_input("monthly payment", value=4030)
    st.write("Monthly payment ", payment, "dollars")

with col4:
    original_debt = st.number_input("original_debt", value=900000)
    st.write("The starting debt is ", original_debt, "dollars")

with col5:
    mortgage_length = st.number_input("mortgage in year", value=30)
    st.write("The mortgage length ", mortgage_length, " years")


# Calculate the years which are x-axis numbers.
x = [start_year + i for i in range(mortgage_length)]
y = [original_debt]
accumulated_payments = [0]

# Calculate new year mortgage balance based on last year data
for i in range(1, mortgage_length):
    last_year_index = i - 1
    base = y[last_year_index]
    balance = base * (1 + (interest_rate * 0.01)) - payment * 12
    y.append(balance)
    accumulated_payments.append(accumulated_payments[last_year_index] + payment * 12)

import pandas as pd
df = pd.DataFrame({
    "year": x,
    "balance": y,
    "total_payments": accumulated_payments,
})

import plotly.express as px
fig = px.bar(df, x="year", y="balance", color='balance', title="Year-over-year mortgage balance")
st.plotly_chart(fig, use_container_width=True)

import plotly.graph_objects as go

fig_payment = go.Figure()
fig_payment.add_trace(go.Bar(x=df["year"], y=df["total_payments"], marker=dict(
            color=df["total_payments"] / 3,
            colorscale="Bluered",
            showscale=False,
        ), name="total payments"))
fig_payment.add_trace(go.Bar(x=df["year"], y=df["balance"], 
                             marker=dict(color='#F4E4BA'), name="remaing balances"))

# Change the bar mode
fig_payment.update_layout(title="Accumulated payments over years", barmode='group')

st.plotly_chart(fig_payment, use_container_width=True)