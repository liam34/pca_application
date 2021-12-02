import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

scatter_column, settings_column = st.beta_columns((4, 1))

scatter_column.title("Multi-Dimensional Analysis")

settings_column.title("Settings")