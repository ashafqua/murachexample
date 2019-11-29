#!/usr/bin/env python
# coding: utf-8

# # Module 10: Data Analysis in Python
# ## Part 2

# In[1]:


#Import Python Libraries
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Missing Values
# - Missing values are marked as NaN
# - When summing the data, missing values will be treated as zero
# - If all values are missing, the sum will be equal to NaN
# - cumsum() and cumprod() methods ignore missing values but preserve them in the resulting arrays
# - Missing values in GroupBy method are excluded (just like in R)
# - Many descriptive statistics methods have skipna option to control if missing data should be excluded . This value is set to True by default (unlike R)
# 
# There are a number of methods to deal with missing values in the data frame:
# 
# - dropna() -	Drop missing observations
# - dropna(how='all')	- Drop observations where all cells is NA
# - dropna(axis=1, how='all') -	Drop column if all the values are missing
# - dropna(thresh = 5) -	Drop rows that contain less than 5 non-missing values
# - fillna(0)	- Replace missing values with zeros
# - isnull()	- Returns True if the value is missing
# - notnull() -	Returns True for non-missing values
# 
# 
# 

# In[2]:


# Read a dataset with missing values
flights = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/flights.csv")
flights.head()


# In[3]:


# Select the rows that have at least one missing value for dep_time
flights[flights['dep_time'].isnull()].head()


# In[4]:


# Get a count of the missings in each column
flights.isnull().sum()


# In[5]:


# Filter all the rows where arr_delay value is missing:
flights1 = flights[ flights['arr_delay'].notnull( )]
flights1.head()


# In[6]:


# Check to see the number missing
flights1['arr_delay'].isnull().sum()


# In[7]:


# Remove all the observations with missing values
flights2 = flights.dropna()


# ### Handons-on Exercise
# - Check the flights2 dataset to see if all missing values have been dropped
# 

# In[8]:


# Answer
flights2['arr_delay'].isnull().sum()


# ---
# ### Aggregation Functions in Pandas
# Aggregation - computing a summary statistic about each group, i.e.
# - compute group sums or means
# - compute group sizes/counts
# 
# 
# ### Common Aggregation Functions:
# 
# |Function|Description
# |-------|--------
# |min   | minimum
# |max   | maximum
# |count   | number of non-null observations
# |sum   | sum of values
# |mean  | arithmetic mean of values
# |median | median
# |mad | mean absolute deviation
# |mode | mode
# |prod   | product of values
# |std  | standard deviation
# |var | unbiased variance
# 
# 

# In[9]:


# Let's compute summary statistic per a group':
flights.groupby('carrier')['dep_delay'].mean()


# agg() method is useful when multiple statistics are computed per column:
# 

# In[10]:


# We can use agg() methods for aggregation:
flights[['dep_delay','arr_delay']].agg(['min','mean','max'])


# In[11]:


# An example of computing different statistics for different columns
flights.agg({'dep_delay':['min','mean',max], 'carrier':['nunique']})


# ### Hands-On Exercise
# - Use agg() & group by to find the mean, median, min, and max air_time, distance, arr_delay & dep_delay for each airline

# In[12]:


# Answer
flights.groupby('carrier')[['air_time', 'distance', 'dep_delay', 'arr_delay']].agg(['mean','median','min',max])


# ### Explore data using graphics
# Seaborn package is built on matplotlib but provides high level interface for drawing attractive statistical graphics, similar to ggplot2 library in R. It specifically targets statistical data visualization
#   
# 

# In[13]:


#Show graphs within Python notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


# Read in csv file
df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")


# In[15]:


# Use seaborn package to draw a histogram
sns.distplot(df['salary'])


# In[16]:


# Use seaborn package to display a bar chart. Can change style as desired
sns.set_style("whitegrid")

ax = sns.countplot(x='rank', data=df)


# In[17]:


# View count by sex
ax = sns.countplot(x='rank', hue='sex', data=df)


# In[18]:


#Scatterplot in seaborn
# Years of service * salary
sns.jointplot(x='service', y='salary', data=df)


# In[19]:


#If we are interested in linear regression plot for 2 numeric variables we can use regplot
sns.regplot(x='service', y='salary', data=df)


# In[20]:


# box plot
sns.boxplot(x='rank',y='salary', data=df)


# In[21]:


# side-by-side box plot
sns.boxplot(x='rank',y='salary', data=df, hue='sex')


# ---
# ### Hands-On Exercise
# Using seaborn package, explore the realtionship between dep_delay (x) on arr_delay (y) using the flights dataset
# 

# In[22]:


# ANSWER
sns.regplot(x='dep_delay', y='arr_delay', data=flights)


# ---
# ## Basic statistical Analysis

# ### Linear Regression

# In[23]:


# Import Statsmodel functions:
import statsmodels.formula.api as smf


# In[24]:


# create a fitted model
lm = smf.ols(formula='salary ~ service', data=df).fit()

#print model summary
print(lm.summary())


# In[25]:


# print the coefficients
lm.params


# ---
# ### Hands-On Exercise
# - Build a linear model for arr_delay ~ dep_delay
# - Print model summary
# 

# In[26]:


# ANSWER
lm = smf.ols(formula='arr_delay ~ dep_delay', data=flights).fit()

#print model summary
print(lm.summary())


# ---
# ### Student T-test

# In[27]:


# Using scipy package:
from scipy import stats
df_w = df[ df['sex'] == 'Female']['salary']
df_m = df[ df['sex'] == 'Male']['salary']
stats.ttest_ind(df_w, df_m)   


# In[28]:


# This result shows a significant difference in salary


# ### Hands-on Exercise
# - Create a plot/chart that can visualize the result from the t-test above

# In[29]:


# Answer
sns.boxplot(x='sex', y='salary', data=df)


# ### Final Exercise - Putting things together
# - Limit the flights dataset to AA (American Airlines) and UA (United Airlines)
# - Find the descriptive stats for the numeric variables
# - Create a scatter plot that shows the relationship between distance & airtime
# - Run a t-test to find out if there is a significant difference in years of service between males & females
# 

# In[30]:


# Answer
#limit the flights to AA and UA 
fs = flights[(flights['carrier'] == 'UA')|(flights['carrier'] == 'AA')]
#frequency
fs.carrier.value_counts()


# In[31]:


# descriptive stats for the numeric variables
fs.describe()


# In[32]:


# scatter plot that shows the relationship between distance & airtime
sns.jointplot(x='distance', y='air_time', data=fs)


# In[33]:


# T-test using scripy
from scipy import stats
df_w = df[ df['sex'] == 'Female']['service']
df_m = df[ df['sex'] == 'Male']['service']
stats.ttest_ind(df_w, df_m)   


# In[ ]:




