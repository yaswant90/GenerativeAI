import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name")
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}.")

options = ["python", "Java", "C++", "Javascript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"Your selected {choice}")
if name:
    st.write(f"Hello, {name}")

data = {
    "name": ["Yaswanth", "Anil", "Balaji"],
    "age": [28,27,26],
    "city": ["Newyork", "Venice", "Paris"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("choose a csv file", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    
### For more info streamlit.io