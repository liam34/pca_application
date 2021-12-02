import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import preprocessing

scatter_column, settings_column = st.beta_columns((4, 1))
