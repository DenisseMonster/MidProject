import streamlit as st
from data.get_data import islandpop, avculmen, avdepth, avflipper, avbody,islands,species
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gdf

gdf.plot("area", legend=True)
