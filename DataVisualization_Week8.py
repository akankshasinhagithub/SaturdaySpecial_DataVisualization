#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DS360withAkanksha | Saturday Special:Data Visualization


# In[8]:


#Importing required packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


# In[3]:


#Getting data

df=pd.read_csv('african_crises.csv')


# In[4]:


#looking at top rows

df.head()


# In[5]:


#Getting statistics
df.describe()


# In[6]:


#Checking the datatype

df.info()


# In[7]:


#Checking unique countries

unique_countries=df.country.unique()
unique_countries


# In[10]:


# Visualizing year wise average USD exchange rate of each country

sns.set(style='whitegrid')
plt.figure(figsize=(20,20))
count=1
for country in unique_countries:
    plt.subplot(5,3,count)
    count+=1
    col="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    sns.lineplot(df[df.country==country]['year'],
                 df[df.country==country]['exch_usd'],
                 label=country,
                 color=col)
    plt.scatter(df[df.country==country]['year'],
                df[df.country==country]['exch_usd'],
                color=col,
                s=28)
    plt.plot([np.min(df[np.logical_and(df.country==country,df.independence==1)]['year']),
              np.min(df[np.logical_and(df.country==country,df.independence==1)]['year'])],
             [0,
              np.max(df[df.country==country]['exch_usd'])],
             color='black',
             linestyle='dotted',
             alpha=0.8)
    plt.text(np.min(df[np.logical_and(df.country==country,df.independence==1)]['year']),
             np.max(df[df.country==country]['exch_usd'])/2,
             'Independence',
             rotation=-90)
    plt.scatter(x=np.min(df[np.logical_and(df.country==country,df.independence==1)]['year']),
                y=0,
                s=50)
    plt.title(country)
plt.tight_layout()
plt.show()


# In[11]:


#Visualizing debt count of each country

sns.set(style='darkgrid')
cols=['systemic_crisis','domestic_debt_in_default','sovereign_external_debt_default','currency_crises','inflation_crises','banking_crisis']
plt.figure(figsize=(20,20))
count=1
for col in cols:
    plt.subplot(3,2,count)
    count+=1
    sns.countplot(y=df.country,hue=df[col],palette='rocket')
    plt.legend(loc=0)
    plt.title(col)
plt.tight_layout()
plt.show()


# In[13]:


#Visualizing year wise inflation

sns.set(style='whitegrid')
plt.figure(figsize=(20,20))
count=1
for country in unique_countries:
    plt.subplot(5,3,count)
    count+=1
    col="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    sns.lineplot(df[df.country==country]['year'],
                 df[df.country==country]['inflation_annual_cpi'],
                 label=country,
                 color=col)
    plt.scatter(df[df.country==country]['year'],
                df[df.country==country]['inflation_annual_cpi'],
                color=col,
                s=28)
    plt.plot([np.min(df[np.logical_and(df.country==country,df.independence==1)]['year']),
              np.min(df[np.logical_and(df.country==country,df.independence==1)]['year'])],
             [np.min(df[df.country==country]['inflation_annual_cpi']),
              np.max(df[df.country==country]['inflation_annual_cpi'])],
             color='black',
             linestyle='dotted',
             alpha=0.8)
    plt.text(np.min(df[np.logical_and(df.country==country,df.independence==1)]['year']),
             np.max(df[df.country==country]['inflation_annual_cpi'])/2,
             'Independence',
             rotation=-90)
    plt.scatter(x=np.min(df[np.logical_and(df.country==country,df.independence==1)]['year']),
                y=np.min(df[df.country==country]['inflation_annual_cpi']),
                s=50)
    plt.title(country)
plt.tight_layout()
plt.show()


# In[16]:


# Visualizing Data Correlation

sns.heatmap(df.corr(), cmap="coolwarm")


# Observation: We can notice in the above heatmap that inflation_crises is highly correlated with currency_crises. Additionally
#     both features are highly correlated with domestic_debt_in_default and sovereign_external_debt_default.

# In[ ]:




