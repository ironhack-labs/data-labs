import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib as plt 


df = pd.read_csv('../avocado.csv')
df.drop(df.columns[0], axis = 1, inplace = True)
df.year = df.year.astype('str')
df.Date = pd.to_datetime(df.Date)
# print(df.head())

df2 = df
df2['Year'] = df['Date'].dt.year
df2['Month'] = df['Date'].dt.month
df2['Day'] = df['Date'].dt.day


# linedf = df2[['Year', 'Month', 'AveragePrice']]

# line chart
# st.line_chart(linedf[['Year', 'Month']], linedf['AveragePrice'])


# bar chart

st.bar_chart(df2[['4046', '4225', '4770']].sum())
# st.dataframe(df.style.highlight_max(axis=0))


# scatter
# df2.plot(
#     'Year',
#     'Total Volume',
# )


plt.pyplot.scatter(
    df2['Year'],
    df2['Total Volume'],
)

# df3 = df2.groupby('Year')['Total Volume'].sum()
# plt.pyplot(
#     df3
# )

# i should be grouping by year, here
st.write("Grouped by Year")
st.pyplot()