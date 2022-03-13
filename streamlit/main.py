import streamlit as st
from Pages.Speciesb2b import compare_species
from data.get_data import islandpop, avculmen, avdepth, avflipper, avbody,islands,species





select = st.sidebar.selectbox("Select page", ["Home", "Compare Species", "Compare Islands"])


if select == "Home":
    st.title("Project about Penguins")
    st.image("https://blogs.agu.org/wildwildscience/files/2010/02/IMG_19731.jpg")




if select == "Compare Species":
    compare_species()



