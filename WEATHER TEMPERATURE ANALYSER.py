#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# Rows = Days, Columns = Cities [City A, City B, City C]
temps = np.array([
    [32, 30, 35],  # Day 1
    [33, 29, 36],  # Day 2
    [35, 31, 38],  # Day 3
    [36, 33, 37],  # Day 4
    [34, 30, 36],  # Day 5
    [32, 28, 35],  # Day 6
    [31, 27, 34]   # Day 7
])


# In[3]:


#to calculate average
avg_city=np.mean(temps,axis=0)
print("The average of each city is",avg_city)


# In[5]:


#To calculate hottest day of the city
hottest_days=np.argmax(temps,axis=0)
print("Hottest day for each day",hottest_days)


# In[9]:


#Add total temperatures column
total_temp = np.sum(temps, axis=1).reshape(-1, 1)
new_data = np.append(temps, total_temp, axis=1)
print("Data with total temp per day:\n", new_data)


# In[13]:


#Sort days by total heat
sort_indices=np.argsort(total_temp.flatten())
print("Days sorted by total heat:",sort_indices+1)


# In[15]:


#Find the day with sudden temperature drop
temp_diff = np.diff(np.mean(temps, axis=1))
sudden_drop_day = np.argmin(temp_diff) + 2  # +2 because diff skips first day
print("Day with sudden temperature drop:", sudden_drop_day)


# In[ ]:




