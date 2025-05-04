import streamlit as st
import pandas as pd

st.title("First Streamlit App")
st.write("This is a simple Streamlit app to demonstrate the basics.")

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Postion": ["Data Scientist", "Software Engineer", "Product Manager"]
})

st.write("Here is a simple DataFrame:")
st.dataframe(df)