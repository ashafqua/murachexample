#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Name: Ayesha Shafquat
#Directory ID: 113931864
#Date: November 26, 2019  
#Assignment: Homework 4 


# In[9]:


#import the necessary python libraries 
import pandas
import seaborn as sns


# In[10]:


#read/open csv file 
fh = pandas.read_csv("housingdata.csv")
fh.head()


# In[11]:


#1. What is the median home age in years?
print(fh['Age'].median())


# In[12]:


#2. What is the average square footage (house) among two-story homes?
df=fh[fh['Architecture_Type'] == 1]
df['Square_Ft_House'].mean()


# In[13]:


#3. What is the average age of homes that sold for > $350,000?
df = fh[fh['Selling_Price'] > 350000 ] #select homes sold for >$350,000
df.Age.mean() #calculate mean


# In[14]:


#4. Provide summary satistics for square_ft_lot, num_bedrooms, and selling price. 
fh[['Square_Ft_Lot','Num_Bedrooms','Selling_Price']].describe()


# In[15]:


#5. Run a frequency on the construction_type variable to show the number of observations for each category.
fh['Construction_Type'].value_counts()


# In[16]:


#6. Run a frequency on the architecture_type variable to show the number of observations for each category.
fh['Architecture_Type'].value_counts()


# In[17]:


#7. What is the average selling price for each architecture type?
fh.groupby(['Architecture_Type'],as_index=False)['Selling_Price'].mean()


# In[18]:


#8. What is the lowest selling home older than 40 years old? 
df=fh[fh['Age'] > 40 ]
df['Selling_Price'].min()


# In[19]:


#9. Create a scatter plot that shows the relationship between selling price (Y) and the area of the site (X).
sns.jointplot(x='Square_Ft_Lot', y='Selling_Price', data=fh)


# In[20]:


#10. Run a linear regression model to show the relationship between selling price (dependent variable) and area of the site (independent variable). 

import statsmodels.formula.api as smf
lm = smf.ols(formula='Selling_Price ~ Square_Ft_Lot', data=fh).fit()
print(lm.summary())
lm.params


# In[ ]:




