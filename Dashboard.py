from graphs import figs
import streamlit.components.v1 as components
# import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Climate Change Impact on Food", layout="wide")
st.title('Climate Change Impact on Food')


# Average Temperature Graph
fig = figs.avg_temp_scatter()
st.plotly_chart(fig)
