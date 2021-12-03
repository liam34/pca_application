from _plotly_utils.basevalidators import ColorlistValidator
import streamlit as st
import pandas as pd
import plotly.express as px
from application_functions import pca_maker



st.set_page_config(layout="wide")


#navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#navbar
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="#" target="_blank">Car Maker Data</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.youtube.com/watch?v=_b2KXL0wHQg" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/home" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

scatter_column, settings_column = st.columns((4, 1))

scatter_column.title("Multi-Dimensional Analysis")

settings_column.title("Settings")

uploaded_file = settings_column.file_uploader("Choose File")

if uploaded_file is not None:
    data_import = pd.read_csv(uploaded_file)
    pca_data, cat_cols, pca_cols = pca_maker(data_import)

    categorical_variable = settings_column.selectbox("Variable Select", options = cat_cols)
    categorical_variable_2 = settings_column.selectbox("Second Variable Select", options = cat_cols)

    pca_1 = settings_column.selectbox("First Principle Component", options=pca_cols, index=0)
    pca_cols.remove(pca_1)
    pca_2 = settings_column.selectbox("Second Principle Component", options=pca_cols)

    
    scatter_column.plotly_chart(px.scatter(data_frame=pca_data, x=pca_1, y=pca_2, color=categorical_variable, template="simple_white", height=800, hover_data = [categorical_variable_2]), use_container_width=True)

else:
    scatter_column.header("Please Choose a file")


#hide mainmenu and footer
hide_streamlit_style = """
<style>
#mainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)