import streamlit as st
from data3.get_data import islandpop

st.title("Project about Penguins")
island = [islandpop]
st.text(island)