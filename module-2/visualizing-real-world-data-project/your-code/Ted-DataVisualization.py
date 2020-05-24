import pandas as pd
import numpy as np
import re
import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Category20
from bokeh.transform import factor_cmap
from PIL import Image



st.title("Data Visualization using Streamlit")

st.text('The data used for this projects has been downloaded from Kaggle.')
st.text('The records on this file are related to Ted events published between')
st.text('June 2006 and May 2012.')

image = Image.open('Tedlogo.png')
st.image(image,width=560,use_column_width=False,format='PNG')

#Loads data file
ted_data=st.cache(pd.read_csv)('talks.csv')

#Changing the 'publish_date' column data type to 'datetime' as this will allow better data manipulation

ted_data['publish_date']= pd.to_datetime(ted_data['publish_date'])
ted_data['Year']= ted_data['publish_date'].dt.year
ted_data['Month']=ted_data['publish_date'].dt.month

#Dropping rows with empty related tags
ted_data.drop(ted_data[ted_data['related_tags'] == '[]'].index, inplace = True)


#Cleaning the related_tags columns to identify to get the first topic in the list. This topic
#will be used as the main reference topic for the record.

main1=[]
for i in ted_data['related_tags']:
    li = list(i.split(","))[0]
    x=re.sub('\W','',li)
    main1.append(x)
ted_data['main_tag']=main1

#Two very similar tags where identified for 'Art'/ 'Arts'. The tag 'Arts' is being replaced with
#'Art' for better analysis
ted_data=ted_data.replace(to_replace ="Arts", value ="Art") 

#DataFrame to identify how is the viewing trend for tedtalks over the years.
views_trend=ted_data.groupby('Year').sum().sort_values(by='Year',ascending=False).reset_index()
data= views_trend[['Year','views']]

#Plotting data from views_trend
st.subheader('The graph below represents the users viewing trend over the years, starting on June 2006 through May 2012')
p = figure(
title='Viewing Trend over the years ',
x_axis_label='Year',
y_axis_label= 'Views')

p.line(data['Year'], data['views'], legend_label='Trend', line_width=2)
p.left[0].formatter.use_scientific = False
st.bokeh_chart(p)

#DataFrame to select the top 20 main_tag by sum of total views.
top_topics=ted_data.groupby('main_tag')['views'].agg(['sum']).sort_values(by='sum',ascending=False).head(20).reset_index()
#top_topics['sum']=[f'{val:,}' for val in top_topics['sum'] ]

#Plotting data from top_topics
st.subheader('Between 2006 and 2012 the most watched TED events have been related to the categories on the graph.')

main_tag = top_topics['main_tag']
sum = top_topics['sum']

source = ColumnDataSource(data=dict(main_tag=main_tag, sum=sum))
pal = Category20[19]

p = figure(x_range=main_tag, plot_height=500, toolbar_location=None, title="Top20")
p.vbar(x='main_tag', top='sum', width=1, source=source,line_color='white', fill_color=factor_cmap('main_tag', palette= pal, factors=main_tag))

p.xgrid.grid_line_color = None
p.xaxis.major_label_orientation = 1
p.y_range.start = 0
p.y_range.end = 93000000
p.left[0].formatter.use_scientific = False

st.bokeh_chart(p)

#DataFrame to identify the view behavior of the top 5 topics over the years.
top5=['Business','Art','Culture','Brain','Biology']
top5_yr=ted_data.loc[ted_data['main_tag'].isin(top5)]
df_top5= top5_yr.groupby(by=['main_tag','Year'])['views'].sum()
top5_unstack=df_top5.unstack().fillna(0)

#Plotting the Data using multiple bar graphs, these data has been grouped by 'Topic'.
st.subheader('The following graph shows the popularity of the Top 5 ranked topics over the years.')


columns=[2006,2007,2008,2009,2010,2011,2012]
x=[(topic,str(val)) for topic in top5_unstack.index for val in top5_unstack.columns]
main_list=[]
ys=[main_list.extend(top5_unstack[i].values) for i in columns]



source = ColumnDataSource(data=dict(x=x, main_list=main_list))

p = figure(x_range=FactorRange(*x), plot_height=500, title="Top5 by Year",
           toolbar_location=None,tools="hover", tooltips=[("Views","@main_list")])

p.vbar(x='x', top='main_list', width=1.5,source=source,line_color="white")

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None
p.left[0].formatter.use_scientific = False

st.bokeh_chart(p)

#BoxPlot to show Distribution of views in the Dataset
st.subheader('The Box Plot shows the distribution of the data set for '"Views"' values.')
fig = go.Figure(go.Box(x=ted_data['views'],name = 'views',fillcolor="LightSeaGreen",boxmean=True))
fig.update_layout(title={
        'text': "Views Distibution from June 2006 through 2012",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},width=1090)

st.plotly_chart(fig)

#Histogram to visualize mostly viewed speaker in our dataset.
by_spk=ted_data.groupby(['speaker']).count().sort_values(by='ted_event',ascending=False).reset_index()

st.subheader('This Histogram represents the data distribution on based on the frequency that a speaker has participated in TedTalk.')

fig = go.Figure(data=[go.Histogram(x=by_spk['ted_event'], histnorm='percent')])
fig.update_layout(title_text='Speakers appeareance count at Ted', xaxis_title_text='# of appearences',yaxis_title_text='Count')

st.plotly_chart(fig)


#Scatter plot to determine relationship between the view amount of an event an the amount of comments recorded.
scatter= ted_data[ted_data['main_tag']=='Business'].groupby(['ted_event'], as_index=False)['views','comments'].sum()

st.subheader('The scatter plot represents the relationship between the amount of views that Business TedTalks gets versus the amount of comments made by viewers .')
p = figure(plot_width=400, plot_height=400,title='# of views vs. Commets for Business topic events',x_axis_label ="Comments",y_axis_label ="Views")
p.circle(scatter['comments'], scatter['views'], size=10, color="green", alpha=0.5)


p.left[0].formatter.use_scientific = False

st.bokeh_chart(p)





