#Importing Modules/Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import altair as alt
from scipy import stats
import plotly.express as px

#Title
st.markdown('# Visualizing Real World Data')

st.markdown('## Using Titanic data')

#Reading csv file
titanic = pd.read_csv('Data/titanic.csv')

# Creating a data frame without NaN values, in order to devide by age into quartiles in order to then fill NaN based on frequency of quartile.

titanic_age_no_nan = titanic[titanic['Age'].isna() == False]['Age'] #Series without NaN

quart_age = pd.qcut(titanic_age_no_nan, 4) #Series cut into quartiles

quart_age_top_bin_value = [titanic_age_no_nan.quantile(q = p) for p in [0.25, 0.5, 0.75, 1]] #Max value of each bin

quart_age_mean = [round(x) for x in list(stats.binned_statistic(titanic_age_no_nan, titanic_age_no_nan, bins = 4)[0])] #Mean of each bin

st.markdown("## Histogram of passenger's ages (without NaN)")

fig, ax = plt.subplots()

counts, bins, patches = ax.hist(titanic_age_no_nan, 4)

plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Frequency By Quartile (Non-NaN)')

for i in range(0,1):
    patches[i].set_facecolor('pink')
for i in range(1,2):    
    patches[i].set_facecolor('blue')
for i in range(2, 3):
    patches[i].set_facecolor('orange')
for i in range(3, len(patches)):
    patches[i].set_facecolor('red')
    
# Label the raw counts and the percentages below the x-axis...
bin_centers = 0.5 * np.diff(bins) + bins[:-1]
for count, x in zip(counts, bin_centers):

    # Label the percentages
    percent = '%0.0f%%' % (100 * float(count) / counts.sum())
    ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, -25), textcoords='offset points', va='top', ha='center')

fig.savefig('demo.png', pad_inches = 100)

st.pyplot()

#Confirming percentages per bin
percent_per_bin = list(round((titanic_age_no_nan.value_counts(bins = 4)/titanic_age_no_nan.count()).sort_index(),2))

#List of amount of Nan to be replaced with each bin mean
nan_indexes_age = list(titanic[titanic['Age'].isna() == True].index)

len_index_list = [round(x*len(nan_indexes_age)) for x in percent_per_bin]

#Filling NaN values (taking consideration of maintaining the age distribution)
for i in range(len(len_index_list)):
    titanic['Age'].fillna(value=quart_age_mean[i], inplace=True, limit=len_index_list[i])

st.markdown("## Histogram of passenger's ages (with NaN values filled)")

fig, ax = plt.subplots()

fig.set_figheight(5.5)

counts, bins, patches = ax.hist(titanic['Age'], 4)

plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Frequency By Quartile')

for i in range(0,1):
    patches[i].set_facecolor('pink')
for i in range(1,2):    
    patches[i].set_facecolor('blue')
for i in range(2, 3):
    patches[i].set_facecolor('orange')
for i in range(3, len(patches)):
    patches[i].set_facecolor('red')
    
# Label the raw counts and the percentages below the x-axis...
bin_centers = 0.5 * np.diff(bins) + bins[:-1]
for count, x in zip(counts, bin_centers):
    # Label the raw counts
    ax.annotate(str(count), xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, count*0.525), textcoords='offset points', va='top', ha='center')

    # Label the percentages
    percent = '%0.0f%%' % (100 * float(count) / counts.sum())
    ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, -30), textcoords='offset points', va='top', ha='center')

    
fig.savefig('demo1.png', pad_inches = 100)

st.pyplot()

st.markdown('## From the graph above, we can see that most passengers were in between the age of 20 to 40 years old, and very few of passengers were on the older side of the spectrum.')
st.markdown("## The insight that I can see from this, is that most people were able bodies but it does not mean that most survivors were those in that age. Now let's contrast that with the amount that survived on the same graph.")

fig, ax = plt.subplots()

fig.set_figheight(5.5)

counts, bins, patches = ax.hist(titanic['Age'], 4)
counts1, bins1, patches1 = ax.hist(titanic[titanic['Survived'] == 1]['Age'], 4)

plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Frequency By Quartile (All Passengers vs. Survivors)')

for i in range(0, 1):
    patches[i].set_facecolor('#0F9D58')
for i in range(1, 2):    
    patches[i].set_facecolor('#4285F4')
for i in range(2, 3):
    patches[i].set_facecolor('#F4B400')
for i in range(3, len(patches)):
    patches[i].set_facecolor('#DB4437')
    
for i in range(0, 1):
    patches1[i].set_facecolor('green')
for i in range(1, 2):    
    patches1[i].set_facecolor('blue')
for i in range(2, 3):
    patches1[i].set_facecolor('yellow')
for i in range(3, len(patches1)):
    patches1[i].set_facecolor('red')
    
    
# Label the raw counts and the percentages below the x-axis (For all passengers)
bin_centers = 0.5 * np.diff(bins) + bins[:-1]
for count, x in zip(counts, bin_centers):
    # Label the raw counts
    ax.annotate(str(count), xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, count*0.525), textcoords='offset points', va='top', ha='center')

    # Label the percentages
    percent = '%0.0f%%' % (100 * float(count) / counts.sum())
    ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, -20), textcoords='offset points', va='top', ha='center')
    
# Label the raw counts and the percentages below the x-axis (For all survivors)  
bin_centers = 0.5 * np.diff(bins) + bins[:-1]
for count, x in zip(counts1, bin_centers):

    # Label the percentages
    percent = '%0.0f%%' % (100 * float(count) / counts1.sum())
    ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, -30), textcoords='offset points', va='top', ha='center')

fig.savefig('demo2.png', pad_inches = 100)

st.pyplot()



st.markdown("## From the graph above, one can see that the distribution % did not remain the same. Out of the survivors, there was a dicrease in distribution % for most but mostly for those between the age of 60 to 80 and an increase in distribution % for those between the age of 0 to 20.")

st.markdown("## I would interpret this as passengers were prioritizing saving kids and young adults as they are the future. Although since elderly passengers make up less of in % of the survivors (which means the group had the least amount of surivors as a percentage of its on group), one can tell that the majority of the casualties were of those between the age of 20 to 30.")

#Creating an interactive version with Box Plot

fig_2 = px.histogram(
    titanic[titanic['Survived'] == 1], 
    x="Age", 
    # y="tip",
    color="Sex", marginal="box",
    hover_data=titanic[titanic['Survived'] == 1].columns,
    nbins = 4
    )

fig_3 = px.histogram(
    titanic[titanic['Survived'] == 0], 
    x="Age", 
    # y="tip",
    color="Sex", marginal="box",
    hover_data=titanic[titanic['Survived'] == 1].columns,
    nbins = 4
    )

fig_2.update_layout(
    title="Distribution Of Survivors By Sex",
    # xaxis_title="x Axis Title",
    # yaxis_title="y Axis Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

fig_3.update_layout(
    title="Distribution Of Non-Survivors By Sex",
    # xaxis_title="x Axis Title",
    # yaxis_title="y Axis Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

st.plotly_chart(fig_2)
st.plotly_chart(fig_3)

st.markdown("## In the graphs above, one can see the difference between the distribution of survivors vs. non-survivors. Additionally, these graphs can be filtered by sex.")

st.markdown("## We can clearly see that, most survivors are females, but the age distribution remains. We can notice with the help of the box plot correlated to the histogram, that the mean and quartiles are similar between females and males.")

st.markdown("## Now if we take a look at the non-survivors, the story is different. Most non-survivorswere male, and the distribution is not similar. We can see the difference with help of the box plot where most female non-survivors were younger compared to male non-survivors.")



st.markdown("# Now for something ~~completely~~ different...")
st.markdown("## We will now look the age vs. fare of passengers divided by passenger class, and sex.")

age_by_pc_sex_sur = round(pd.pivot_table(titanic, values = 'Age', index = ['Pclass','Sex', 'Survived']))

fig_4 = px.scatter(
    titanic, 
    x="Age", 
    y="Fare", 
    color="Sex", 
    facet_col="Pclass")

fig_4.update_layout(
    title="Age vs. Fare",
    # xaxis_title="x Axis Title",
    # yaxis_title="y Axis Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

st.plotly_chart(fig_4)

st.markdown("## We can clearly see thanks to the scatter plot that passenger classes were divided as passenger class 1 being the luxury one since it is more expensive, and the rest were usually much cheaper.")

st.markdown("## Let's see if passenger class affected the chances of survival.")

age_by_pc_sex_sur = round(pd.pivot_table(titanic, values = 'Age', index = ['Pclass','Sex', 'Survived'], aggfunc = ['mean', 'count']))

age_by_pc_sex_sur.columns = ['_'.join(col) for col in age_by_pc_sex_sur.columns]

age_by_pc_sex_sur.reset_index(inplace = True)

age_by_pc_sex_sur["Survived"] = age_by_pc_sex_sur["Survived"].replace([0, 1], ['No', 'Yes'])

fig_5 = px.bar(
    age_by_pc_sex_sur,
    x='Pclass',
    y='count_Age',
    hover_data=['Sex'],
    color='Survived',
    labels={
        'Pclass':'Passenger Class',
        'count_Age' : 'Count of Passengers'
        }
) 

fig_4.update_layout(
    title="Passenger Class divded primarily by Survival, and secondly by Sex",
    # xaxis_title="x Axis Title",
    # yaxis_title="y Axis Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

st.plotly_chart(fig_5)

st.markdown("## This last graph shows us a lot of information. The first insight that jumps out is that most of the ones that did not survive were part of class 3, although class 2 and class 3 fare was relatively similar.")

st.markdown("## The second insight that we can see is that a larger percentage of males in class 1 survived, compared to those in class 2 and 3. This is even more pronounced when one can see that almost the same amount of males survived in class 1 and 3, but there was substatially more males in class 3 compared to any of the classes at the beginning of the trip.")