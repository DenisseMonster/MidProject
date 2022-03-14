import streamlit as st
from data.get_data import islandpop, avculmen, avdepth, avflipper, avbody,islands,species
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sland = [islands(i) for i in range (1)]

st.text(sland)