'''
Trending YouTube Video Statistics - US Videos
https://www.kaggle.com/datasnaek/youtube-new/data
'''

import streamlit as st
import altair as alt
import plotly_express as px
import pandas as pd


st.title("Data Visualization Project")
st.write("Trending YouTube Video Statistics - US Videos")
st.write("Dataframe:")

data = pd.read_csv('../Downloads/USvideos.csv')

st.write(data)

st.write("10 Top Trending Channels (# of views of videos)")

top_ten = data.groupby('channel_title')['views'].sum().nlargest(10).reset_index()
st.bar_chart(top_ten)


st.write("Correlation between views and likes")
c = alt.Chart(data).mark_circle().encode(x='views', y='likes', size='channel_title', color='channel_title')
st.write(c)

st.write("Summary statistics of views")
#data.boxplot(column='views')
# tips = px.data.tips()
# fig = px.box(tips, y="total_bill")
# fig.show()


st.write("Distribution of dislikes by categories  -- Histogram")
by_category = data.groupby('category_id')['dislikes'].sum()
st.bar_chart(by_category)

