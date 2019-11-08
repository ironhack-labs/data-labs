'''
Trending YouTube Video Statistics - US Videos
https://www.kaggle.com/datasnaek/youtube-new/data
'''

import streamlit as statistics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import chart_studio.plotly as py
import cufflinks as cf
from ipywidgets import interact
warnings.filterwarnings('ignore')


st.title("Data Visualization Project")
st.write("Trending YouTube Video Statistics - US Videos")
st.write("Dataframe:")

data = pd.read_csv('USvideos.csv')

st.write(data)

top_ten = data.groupby('channel_title')['views'].sum().nlargest(10).reset_index()
st.bar_chart(top_ten)
#top_ten
# top_ten.sort_values(by = "views", ascending = True).plot.barh()

# st.line_chart(df)

# if st.sidebar.checkbox('Show histogram'):
#     st.bar_chart(df)