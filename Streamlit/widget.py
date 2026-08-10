import streamlit as st
import pandas as pd

st.title("-------welcome everyone-------")
name = st.text_input("enter your name : ")
st.write(f"hello ! {name}")

age = st.slider("enter your age : ", 0, 100, 18)
st.write(f"your age is {age}")

options = ['python', 'java', 'c++', 'web.dev', 'aiml']
choice = st.selectbox("Choose a language:", options=options)
st.write(f"Yeah {choice} is an interesting language!")

data = {
    'name': ['shiva', 'prasad', 'reddy', 'kathi'],
    'age': [18, 23, 19, 20],
    'city': ['hyd', 'mumbai', 'delhi', 'bangalore']
}
df = pd.DataFrame(data)
st.write("Sample dataframe:")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file:", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded CSV data:")
    st.write(df)
