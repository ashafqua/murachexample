#!/usr/bin/env python
# coding: utf-8

# # Module 10: Data Analysis in Python Exercise
# ## Submit this (completed) file as a .py script for credit 
# ## Part 1
# Pandas:
# - data structures and tools designed to work with table-like data (similar to Series and Data Frames in R)
# 
# - provides tools for data manipulation: reshaping, merging, sorting, slicing, aggregation etc.
# 
# - allows handling missing data
# 

# In[1]:


#Import Python Libraries
import pandas as pd


# ## Reading data using pandas

# In[2]:


#Read csv file
df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")

# Note: The above command has many optional arguments to fine-tune the data import process.


# There is a number of pandas commands to read other data formats:
# 
# - pd.read_excel('myfile.xlsx',sheet_name='Sheet1', index_col=None, na_values=['NA'])
# - pd.read_stata('myfile.dta')
# - pd.read_sas('myfile.sas7bdat')
# - pd.read_hdf('myfile.h5','df')
# 

# ## Exploring data frames

# In[3]:


#List first 5 records (5 is the default, but can specify the # of records in ())
df.head()


# ## Hands-on exercises
# - Read the first 10, 20, 50 records
#          

# In[4]:


## INSERT ANSWER
df.head(10)


# In[5]:


## INSERT ANSWER
df.head(20)


# In[6]:


## INSERT ANSWER
df.head(50)


# ## Data Frame data types
# - object (python string)
# - int64 (python integer)
# - float64 (python float)
# - datetime64, timedelta[ns] (no python type, but see the datetime module in Python’s standard library)
# 
# ** 64 refers to the memory allocated to hold this character.

# In[7]:


#Check a particular column type
df['salary'].dtype


# In[8]:


#Check types for all the columns
df.dtypes


# ## Data Frames attributes
# Python objects have *attributes* and *methods*.
# 
# - dtypes: list the types of the columns
# - columns: list the column names
# - axes: list the row labels and column names
# - ndim: number of dimensions
# - size: number of elements 
# - shape: return a tuple representing the dimensionality 
# - values: numpy representation of the data
# 

# ## Hands-on exercises
# - Find how many records this data frame has;
# - How many variables are there?     
# - What are the column names?
# - What types of columns do we have in this data frame?
# 

# In[9]:


## INSERT ANSWER
# nrows and ncolumns
df.shape


# In[10]:


## INSERT ANSWER


# In[11]:


## INSERT ANSWER
df.columns


# In[12]:


## INSERT ANSWER
df.dtypes


# ## Data Frames methods
# Unlike attributes, python methods have parenthesis.
# All attributes and methods can be listed with a dir() function: dir(df)
# - head([n]), tail( [n] ):	first/last n rows
# - describe():	generate descriptive statistics (for numeric columns only)
# - max(), min():	return max/min values for all numeric columns
# - mean(), median():	return mean/median values for all numeric columns
# - std():	standard deviation
# - sample([n]):	returns a random sample of the data frame
# - dropna():	drop all the records with missing values
# - value_counts(): gives frequencies
# 
# 

# ## Hands-on exercises
# - Give the summary for the numeric columns in the dataset
# - Calculate standard deviation for all numeric columns;
# - What are the mean values of the first 50 records in the dataset? Hint: use head() method to subset the first 50 records and then calculate the mean
# - Find the frequency of males and females in this dataset
# 

# In[13]:


## INSERT ANSWER
df.describe()


# In[14]:


## INSERT ANSWER
df.std()


# In[15]:


## INSERT ANSWER
df.head(50).mean()


# In[16]:


## INSERT ANSWER
df.sex.value_counts()


# ## Selecting a column in a Data Frame
# 
# Method 1:   Subset the data frame using column name:
#                       df['sex']
# 
# Method 2:   Use the column name as an attribute:
#                       df.sex
# 
# Note: there is an attribute rank for pandas data frames, so to select a column with a name "rank" we should use method 1.
# 

# ##       Hands-on exercises
# - Calculate the basic statistics for the salary column
# - Find how many values in the salary column (use count method)
# - Calculate the average salary
# 

# In[17]:


## INSERT ANSWER
df.salary.describe()


# In[18]:


## INSERT ANSWER
df.salary.count()


# In[19]:


## INSERT ANSWER
df.salary.mean()


# ## Data Frames groupby method

# Using "group by" method we can:
# - Split the data into groups based on some criteria
# - Calculate statistics (or apply a function) to each group
# - Similar to dplyr() function in R
# 

# In[20]:


#Group data using rank
df_rank = df.groupby(['rank'])


# In[21]:


#Calculate mean value for each numeric column per each group
df_rank.mean()


# Once groupby object is created we can calculate various statistics for each group:
# 

# In[22]:


#Calculate mean salary for each professor rank:
df.groupby('rank')[['salary']].mean()


# Note: If single brackets are used to specify the column (e.g. salary), then the output is Pandas Series object. When double brackets are used the output is a Data Frame
# 

# groupby performance notes:
# - no grouping/splitting occurs until it's needed. Creating the groupby object only verifies that you have passed a valid mapping
# - by default the group keys are sorted during the groupby operation. You may want to pass sort=False for potential speedup:
# 

# In[23]:


#Calculate mean salary for each professor rank:
df.groupby(['rank'], sort=False)[['salary']].mean()


# ## Data Frame: filtering
# To subset the data we can apply Boolean indexing. This indexing is commonly known as a filter.  For example if we want to subset the rows in which the salary value is greater than $120K: 
# 

# In[24]:


#Calculate mean salary for each professor rank:
df_sub = df[ df['salary'] > 120000 ]


# In[25]:


print(df_sub)


# Any Boolean operator can be used to subset the data: 
# - '>' greater   
# - '>=' greater or equal
# - '<'   less
# - '<=' less or equal
# - '==' equal   
# - '!=' not equal
# 

# In[26]:


#Select only those rows that contain female professors:
df_f = df[ df['sex'] == 'Female' ]


# In[27]:


print(df_f)


# ## Data Frames: Slicing
# There are a number of ways to subset the Data Frame:
# - one or more columns
# - one or more rows
# - a subset of rows and columns
# 
# Rows and columns can be selected by their position or label 

# When selecting one column, it is possible to use single set of brackets, but the resulting object will be  a Series (not a DataFrame): 
# 

# In[28]:


#Select column salary:
df['salary']


# When we need to select more than one column and/or make the output to be a DataFrame, we should use double brackets:
# 

# In[29]:


#Select column salary:
df[['rank','salary']]


# ## Data Frames: Selecting rows
# If we need to select a range of rows, we can specify the range using ":" 
# 

# In[30]:


#Select rows by their position:
df[10:20]


# Notice that the first row has a position 0, and the last value in the range is omitted:
# So for 0:10 range the first 10 rows are returned with the positions starting with 0 and ending with 9
# 

# ## Data Frames: method loc
# If we need to select a range of rows, using their labels we can use method loc:
# 

# In[31]:


#Select rows by their labels:
df_sub.loc[10:20,['rank','sex','salary']]


# ## Data Frames: Sorting
# We can sort the data by a value in the column. By default the sorting will occur in ascending order and a new data frame is return. 
# 

# In[32]:


# Create a new data frame from the original sorted by the column Salary
df_sorted = df.sort_values( by ='service')
df_sorted.head()


# We can sort the data using 2 or more columns:
# 

# In[33]:


df_sorted = df.sort_values( by =['service', 'salary'], ascending = [True, False])
df_sorted.head(10)


# In[ ]:




