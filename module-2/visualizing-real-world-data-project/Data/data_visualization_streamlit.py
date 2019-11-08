import streamlit as st
from bokeh.plotting import figure
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import altair as alt
import chart_studio.plotly as py
import cufflinks as cf
from PIL import Image

image = Image.open('../data/Variety.jpg')

st.image(image, caption="Red Red Wine... Stay close to me, Don't let me be alone", use_column_width=True)

audio_file = open('RedRedWine.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

st.title('WINE WORLWIDE REVIEWS')


st.subheader('Real World Data Visualization Project')

data = st.cache(pd.read_csv)('../data/winemag-data_first150k.csv')

data = data.drop(['Unnamed: 0', 'region_2'], axis = 1)

st.write(data[:1000])


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)



st.subheader("Mean of Prices")

mean_prices = data.groupby('price')['points'].mean().reset_index()

st.bar_chart(mean_prices)

st.subheader("Best Wines and their variety by Country")
    
best_wines = alt.Chart(data[:1000]).mark_circle().encode(x='country', y='points', size='variety', color='variety')

st.write(best_wines)

st.subheader("Best Wines and their variety by Province")
    
province = alt.Chart(data[:1000]).mark_bar(opacity=0.2).encode(x='province', y='points', size='variety', color='variety')

st.write(province)

# st.subheader("Best Wineries")

# def main():
#     df = data
#     wineries = df['winery'].value_counts()
#     total_wineries = pd.DataFrame({'winery': wineries.index.tolist(), 'number': wineries.values.tolist()})
#     wineries = alt.Chart(total_wineries).mark_bar().encode(alt.X('winery:N'), alt.Y('number:Q'))
#     st.write(wineries)
# main()
# data['top_ten'] = pd.get_dummies(data['winery'])

# # .value_counts().nlargest(10).reset_index()

# top_ten = data.groupby('province')['top_ten'].sum().nlargest(10).reset_index()

# st.bar_chart(top_ten)

# st.write("Correlation between views and likes")





