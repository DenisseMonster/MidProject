import streamlit as st
from data.get_data import islandpop, avculmen, avdepth, avflipper, avbody,islands,species
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def compare_species():
    st.title("Compare the Species average!")
    Species = species()
    especie1 = st.selectbox("Please chose an specie",Species)
    especie2 = st.selectbox("Please chose a second specie",Species)

    first = []
    second = []
    speciesdata = ["avculmen", "avflipper","avlenght"]
    for especie in species():
        if especie == "Species":
            continue
        first.append(especie1[especie])

    for especie in species():
        if especie == "Species":
            continue
        second.append(especie2[especie])


