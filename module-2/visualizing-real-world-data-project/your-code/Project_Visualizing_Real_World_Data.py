#Importing Modules/Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import altair as alt
from scipy import stats

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

st.markdown("# Now for something ~~completely~~ different...")
st.markdown("## I will now show the average age of passengers divided by pclass, sex, and survival")

age_by_pc_sex_sur = round(pd.pivot_table(titanic, values = 'Age', index = ['Pclass','Sex', 'Survived']))

c = alt.Chart(age_by_pc_sex_sur).mark_circle().encode(x='Pclass', y='Age')

st.altair_chart(c, width=-1)

#  , size=[''], color='c'