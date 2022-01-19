# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:50:44 2022

@author: siddh
"""

#Topic ---- Case Study - Denco - Manufacturing Firm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%case details
#%%Objective
#Expand Business by encouraging loyal customers to Improve repeated sales
#Maximise revenue from high value parts
#%%Information Required
#Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
#Which customers contribute the most to their revenue - How do I retain these customers & target incentives
#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts
#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
#%%%
#see all columns
pd.set_option('display.max_columns',15)
#others - max_rows, width, precision, height, date_dayfirst, date_yearfirst
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format
#read data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
#df = pd.read_csv('data/denco.csv')
df = pd.read_csv(url)
#see properties of data
df
#print(df)
df.shape
df.columns
df.dtypes
df['region']=df['region'].astype('category') # converted to category
#%%%%
# find loyal customers
df["custname"].value_counts().head(5) #most loyal customers are those whose frequency is more than 100
df["custname"].value_counts().sort_values(ascending=True)[0:5]
df["custname"].value_counts().sort_values(ascending=False)[0:5]

df["custname"].value_counts().tail(100)
#%%
# customers who contribute more to their revenue
df.groupby(['custname']).sum().sort_values(by="revenue")

df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue',ascending=False).head(5).plot(kind='bar')
#%%
#part numbers based on revenue
df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue',ascending=False).head(5).plot(kind='bar')

df[['partnum','revenue']].groupby('partnum').aggregate([np.sum,'size','min','max']).sort_values(by='size') #error
df[df['partnum'] == 715000000]
 
#%%
#parts numbers based on margins
df[['partnum','margin']].groupby('partnum').aggregate([np.sum,'size','min','max'])
df[['partnum','margin']]
df[['partnum','margin']].groupby('partnum')
df[['partnum','margin','revenue','region']].groupby(['partnum','region']).aggregate([np.sum,'size']) # gr

#%%
# region giving max revenue
df[['margin','revenue','region']].groupby(['region']).aggregate([np.sum,'size'])
df[['margin','region']].groupby(['region']).sum().sort_values(by='margin',ascending=False)

df.groupby('region').aggregate({'margin':np.sum}).sort_values(by='margin',ascending=False).plot(kind='bar')
