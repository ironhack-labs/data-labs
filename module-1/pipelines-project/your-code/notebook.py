
# coding: utf-8

# In[20]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


data = pd.read_csv('Final_paper.csv')
data.head(5)


# In[22]:


def acquire():
    data = pd.read_csv('Final_paper.csv')
    return data


# In[25]:


year=int(input('Please enter the year: '))


# In[26]:


def wrangle(data, year):
    filtered = data[data['year']==year]
    return filtered


# In[27]:


filtered = wrangle(data,year)


# In[28]:


def analyze(filtered):
    grouped = filtered.groupby('BINS').agg({'Happiness Score':'mean'}).reset_index()
    results = grouped.sort_values('Happiness Score', ascending=False).head(10)
    return results


# In[29]:


data = analyze(filtered)


# In[30]:



grouped = data.groupby('BINS').agg({'Happiness Score':'mean'}).reset_index()
results = grouped.sort_values('Happiness Score', ascending=False).head(10)


# In[31]:


display(grouped)


# In[32]:


def visualize(df):
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=results, x='BINS', y='Happiness Score')
    plt.title(title + "\n", fontsize=16)
    return barchart


# In[33]:


fig, ax = plt.subplots(figsize=(15,8))
barchart = sns.barplot(data=results, x='BINS', y='Happiness Score')


# In[41]:


def save_viz(Happiness):
    title="chart"
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=data, x='BINS', y='Happiness Score')
    plt.title(title + "\n", fontsize=16)
    fig = barchart.get_figure()
    fig.savefig(title + '.png')


# In[42]:


if __name__ == '__main__':
    data = acquire()
    filtered = wrangle(data,year)
    results = analyze(filtered)
    barchart = visualize(results)
    save_viz(results)

