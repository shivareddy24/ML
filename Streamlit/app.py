import streamlit as st
import pandas as pd
import numpy as np

st.title("HELLO WORLD")
st.write("This is a sample message...!")

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

st.write("Here is the dataframe:")
st.write(df)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
