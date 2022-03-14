import streamlit as st
from data.get_data import islandpop, avculmen, avdepth, avflipper, avbody,islands,species
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def compare_island():
    st.title("Compare the Species average!")
    Islands = islands()
    isla1 = st.selectbox("Please chose an specie",Islands)
    isla2 = st.selectbox("Please chose a second specie",Islands)

    first = []
    second = []
    speciesdata = ["avculmen", "avflipper","avle"]
    for especie in species():
        if especie == "Islands":
            continue
        first.append(isla1[especie])

    for especie in species():
        if especie == "Species":
            continue
        second.append(isla2[especie])