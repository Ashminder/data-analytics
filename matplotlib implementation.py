#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[18]:


day =[1,2,3,4,5,6,7]
temperature_min =[20,25,26,22,25,26,23]
temperature_max =[35,34,37,36,33,31,32]
temperature_avg =[24,25,26,27,21,23,24]


# In[36]:


plt.xlabel('weekday')
plt.ylabel('temperature')
plt.title('temeprature of week')


plt.plot(day, temperature_max,color ='Red', marker = '.', linestyle = 'dashed', alpha = 0.8,label ='max')
plt.plot(day, temperature_min,color ='Green', marker = '.', linestyle = 'dashed', alpha = 0.8, label ='min')
plt.plot(day, temperature_avg,color ='Blue', marker = '.', linestyle = 'dashed', alpha = 0.8, label = 'average')

plt.grid()
plt.legend(loc= 'best', shadow = "True") # legend( ) will be after declaration of label property only


# In[41]:


#plotting bar and histograms 
import numpy as np


# In[48]:


company = ['google', 'amazon', 'meta', 'tesla', 'netflix'] 
funds = [90,80,56,48,46]
profits = [60,52,33,40,34]


# In[61]:


xpos = np.arange(len(company))
xpos


# In[65]:


plt.xticks(xpos, company)
plt.xlabel('Companies')
plt.ylabel('Funds')
plt.title('revenues')
plt.bar(xpos-0.2, funds, label = 'Revenue')
plt.bar(xpos+0.2, profits, label = 'Profit')
plt.legend()


# In[67]:


# horizontal bar charts
plt.yticks(xpos, company)
plt.xlabel('Companies')
plt.ylabel('Funds')
plt.title('revenues')
plt.barh(xpos-0.2, funds, label = 'Revenue')
plt.barh(xpos+0.2, profits, label = 'Profit')
plt.legend()


# In[81]:


# plotting historgram
blodd_pressure_men = [82,84,86,120,150,165,89,135,126,145,150,100,110,115,116,95,90]
blood_pressure_women=[85,86,78,79,95,96,124,135,145,102,145,133,135,150,162,141,142]


# In[113]:


plt.xlabel('Blood Pressure Level')
plt.ylabel('No of Patients')
plt.title('Blood Pressure Analysis')
plt.hist([blodd_pressure_men, blood_pressure_women], bins = [80,120,130,200],rwidth = 0.98, color =['orange', 'blue'], 
         label=['Men', 'Women'], orientation ='horizontal')
plt.legend()
plt.savefig('C:\\Users\\Ashminder Singh\\OneDrive\\Desktop\\ashminder\\datasets', bbox_inches ='tight', pad_inches='0.2')


# In[103]:


# pei chart
expenses_value = [1000,2000,2500,7400,6500,6600,700]
expenses_category =['metro','internet','petrol','ration','rent','education', 'others']


# In[121]:


plt.pie(expenses_value, labels = expenses_category, radius = 1.5, autopct ='%0.1f%%', shadow ='True', explode=[0,0,0,0,0.2,0,0])
plt.show()
plt.savefig('C:\\Users\\Ashminder Singh\\OneDrive\\Desktop\\ashminder\\datasets\\fig2.pdf',bbox_inches = 'tight',pad_inches =2
           ,transparent = True)


# In[105]:


# to get rid of extra data alongwith piechart, we will use 
plt.show()


# In[ ]:




