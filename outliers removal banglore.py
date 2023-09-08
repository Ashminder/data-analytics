#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sb


# In[2]:


file =  "C:\\Users\\Ashminder Singh\\OneDrive\\Desktop\\ashminder\\datasets\\bhp.csv"


# In[4]:


df =pd.read_csv(file)


# In[5]:


df.head()


# In[11]:


df.price_per_sqft.describe()  #analysing max and min price


# In[14]:


sb.histplot('price_per_sqft',kde=True)


# Using PErcentile mEthod to remove ouliers

# In[16]:


lower_limit, upper_limit = df.price_per_sqft.quantile([0.001,0.999])
lower_limit,upper_limit


# In[25]:


df2=df[(df.price_per_sqft>lower_limit) & (df.price_per_sqft<upper_limit)]


# In[28]:


df.shape, df2.shape


# In[30]:


df.shape[0]-df2.shape[0]


# SO finally we ommited 28 outliers entries from csv file...removing more outliers entries using 4 standard deviation method
# 

# In[32]:


df2.price_per_sqft.describe()


# in df2 we can analyse  min and max price sepctrum to be  1380 approx and 50000  approx

# In[33]:


df2.price_per_sqft.mean(), df2.price_per_sqft.std()


# In[34]:


max_price = df2.price_per_sqft.mean() + 4*df2.price_per_sqft.std()
min_price = df2.price_per_sqft.mean() - 4*df2.price_per_sqft.std()
max_price,min_price


# In[39]:


df3=df2[(df2.price_per_sqft > min_price) & (df2.price_per_sqft < max_price)]
df3.shape


# In[40]:


df2.shape[0] - df3.shape[0]


# so again we have removed 125  ouliers entries from dataframe 2

# In[43]:


sb.histplot(df2.price_per_sqft)


# removing outliers using z score method... zscore basically is defined as mean price subtarcting from price  divided by std deviation...we will take a zscore of 4 and -4...for our refrence we will take dataframe 2

# In[51]:


df2['z_score'] = (df2.price_per_sqft - df2.price_per_sqft.mean())/df2.price_per_sqft.std()


# In[56]:


df2.sample(5)


# In[58]:


outliers = df2[(df2.z_score < -4) | (df2.z_score > 4)]
outliers


# In[64]:


df4 = df2[(df2.z_score > -4) & (df2.z_score < 4)]


# In[65]:


df4.shape


# In[66]:


df2.shape[0] - df4.shape[0]


# So using z distribution method we omiited same no of rows as we did using standrad deviation method 

# In[ ]:




