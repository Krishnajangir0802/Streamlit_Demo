import streamlit as st
import pandas as pd

data = {
    "Series_1": [1, 2, 3, 4, 5, 6, 7],
    "Series_2": [100, 250, 125, 45, 32, 56, 98],
}

df = pd.DataFrame(data)

st.title("My First Streamlit App")
st.subheader("Introducing Streamlit in Automate Everything with Python!!")
st.write("""This is our first web app!!
Enjoy it!!""")

st.write(df)