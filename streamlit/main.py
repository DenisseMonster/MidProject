import streamlit as st
from Pages.Speciesb2b import compare_species
from Pages.Islandpop import list_island
from Pages.Islands import sland
from data.get_data import islandpop, avculmen, avdepth, avflipper, avbody,islands,species

header = st.container()
dataset = st.container()

select = st.sidebar.selectbox("Select page", ["Home", "Compare Species", "Compare Islands", "Island Population", "Islands"])


if select == "Home":
    with header:
        st.title("Welcome to the wanderfull world of Penguins!")
        st.text("In this project we will look into the specifics of the Antartica Penguins and getting in depth with their features.")
        st.image("https://blogs.agu.org/wildwildscience/files/2010/02/IMG_19731.jpg")
    with dataset:
        st.title("Palmer Archipelago Penguins Dataset")
        st.text("I downloaded this dataset from kaggle.com, cleaned some of the data al added lat/long using wikipedia")




if select == "Compare Species":
    compare_species()

