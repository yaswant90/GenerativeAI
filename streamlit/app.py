import streamlit as st
import pandas as pd
import numpy as np

## Title of the Application
st.title("Hello streamlit")

## Display a simple text
st.write("This is the simple text")

## create a simple dataframe
df = pd.DataFrame({
    'first': [1,2,3,4],
    'second': [5,6,7,8]
})

## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)

## create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)