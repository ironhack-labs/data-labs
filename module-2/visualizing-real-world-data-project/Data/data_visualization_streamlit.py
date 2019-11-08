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

image = Image.open('../Data/Variety.jpg')

st.image(image, caption="Red Red Wine... Stay close to me, Don't let me be alone", use_column_width=True)


st.title('WINE WORLWIDE REVIEWS')


st.subheader('Real World Data Visualization Project')

data = st.cache(pd.read_csv)('../Data/winemag-data_first150k.csv')

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

st.subheader("Best Wineries")

# wineries = data.groupby('winery')

# data[''] = data

data['top_ten'] = pd.get_dummies(data['winery'])

# .value_counts().nlargest(10).reset_index()

top_ten = data.groupby('province')['top_ten'].sum().nlargest(10).reset_index()

st.bar_chart(top_ten)

# wineries = data[["points", "winery", "province"]].groupby(["winery", "province"]).agg("mean").reset_index()

# st.bar_chart(wineries)



# df2 = data.pivot_table(
#     index = ['country'],
#     values = 'points',
#     aggfunc = 'sum'
#     ).iplot(kind = 'bar')

# st.line_chart(df2)

# group_labels = list(data['variety'])

# Create distplot with custom bin_size
# fig = ff.create_distplot( data, group_labels, bin_size=[.1, .25, .5])

# st.plotly_chart(fig)




# x = data['state'].unique()
# y = data['job_values'].count()

# p = figure(
#      title='Jobs per month in each State',
#      x_axis_label='x',
#      y_axis_label='y')

# p.line(x, y, legend='Trend', line_width=2)

# st.bokeh_chart(p)


# jobs = st.sidebar.multiselect("Enter city", data['city'].unique())
# st.write("Your area jobs", jobs) #not returning the jobs in area, gotta review
# st.subheader('Number of jobs by month')
# hist_values = np.histogram(df[post_date].dt.day, bins=31, range=(0,31))[0]
# st.bar_chart(hist_values)


#  import streamlit as st
# import plotly.figure_factory as ff
# # import numpy as np
# >>>
# >>> # Add histogram data
# >>> x1 = np.random.randn(200) - 2
# >>> x2 = np.random.randn(200)
# >>> x3 = np.random.randn(200) + 2
# >>>
# >>> # Group data together
# >>> hist_data = [x1, x2, x3]
# >>>
# >>> group_labels = ['Group 1', 'Group 2', 'Group 3']
# >>>
# >>> # Create distplot with custom bin_size
# >>> fig = ff.create_distplot(
# ...         hist_data, group_labels, bin_size=[.1, .25, .5])
# >>>
# >>> # Plot!
# >>> st.plotly_chart(fig)

