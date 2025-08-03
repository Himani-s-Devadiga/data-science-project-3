#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[10]:


df=pd.read_csv('spotify_tracks.csv')
df


# In[11]:


df.head()


# In[12]:


df.columns


# In[14]:


df.info()
df.describe()


# In[17]:


#Clean the data(basic)
df.isnull().sum()
df.drop_duplicates(inplace=True)


# In[19]:


#ANALYSIS TASKS
#Top 10 most popular songs
top_songs = df.sort_values(by='popularity', ascending=False)[['name', 'artists', 'popularity']].head(10)
print(top_songs)


# In[20]:


#Top 5 most popular artist
top_artists = df.groupby('name')['popularity'].mean().sort_values(ascending=False).head(5)
print(top_artists)


# In[24]:


#Average popularity by genre
genre_popularity = df.groupby('genre')['popularity'].mean().sort_values(ascending=False).head(10)
print(genre_popularity)


# In[25]:


#Explicit vs Non-Explicit songs count
df['explicit'].value_counts()


# In[27]:


#Convert duration into minutes
df['duration_min'] = df['duration_ms'] / 60000
df[['name', 'duration_min']].head()


# In[28]:


#To get the longest songs
df[['name', 'artists', 'duration_min']].sort_values(by='duration_min', ascending=False).head(10)


# In[ ]:




