#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Data Source: https://fbref.com/en/players/dea698d9/goallogs/all_comps/Cristiano-Ronaldo-Goal-Log

# Packages for data processing
import pandas as pd
import numpy as np


# In[14]:


# Helpful Dictionary for Column Headers
info = {'Date':'Date of match in local time','Competition':'League or National Competiton Type',
        'Round':'Round or Phase of Competition','Venue':'Location of football/soccer match',
        'Squad':'Team Ronaldo is playing for','Opponent':'Opposing Team','Start':'Did Ronaldo play the match or not',
        'xG':'Expected Goals','PSxG':'How likely the goalkeeper is to save the shot','Body Part':'Part of body used to score the goal',
        'Distance':'Distance from goal post for goal scored','Minute':'Time spent by Ronaldo on pitch','Score':'Final Score at match end','Goalkeeper':'Goalkeeper for specific match',
        'Assist':'Player who assisted goal','GCA1':'Goal Scoring Event 1','Type1':'Type of Goal-scoring event for GCA1','GCA2':'Goal Scoring Event 2','Type2':'Type of Goal-scoring event for GCA2'}


# In[15]:


# Store Ronaldo Stats data 
df = pd.read_csv("Ronaldo_stats .csv",index_col = False)
df.set_index('ID', inplace=True) #set original ID column from csv as unique ID
df.rename(columns={'Comp':'Competition'}, inplace=True) # rename for user readabilitydf.rename(columns={'Comp':'Competition'}, inplace=True) # rename for user readability
df.rename(columns={'Type':'Type1'}, inplace=True) # rename for user readability ***check these titles
df.rename(columns={'Type1':'Type2'}, inplace=True) # rename for user readability


# In[16]:


df.head(10)  # view first 5 rows


# In[17]:


# View snapshot of data
df.describe() # important stats about data and columns


# In[18]:


def ret_df(): #store dataframe in function to be used in Analysis_functions file
    return df
def ret_info(): # function for GUI
    return info
    


# In[23]:


# Store Ronaldo Stats 2 data
df2 = pd.read_csv("Ronaldo_stats_2.csv", index_col = False)
df2.set_index('Season', inplace=True)
df2


# In[24]:


def ret_df2():
    return df2


# In[ ]:





# In[ ]:




