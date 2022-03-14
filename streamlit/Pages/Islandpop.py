import streamlit as st
from data.get_data import islandpop, avculmen, avdepth, avflipper, avbody,islands,species
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

list_island = [islandpop(i) for i in range (1)]

st.write(list_island)