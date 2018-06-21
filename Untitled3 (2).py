
# coding: utf-8

# # ANALYSIS OF EDUCATION DATA FROM DATA.GOV.IN

# NAME-SHUBHAM BANSAL                                          
# EMAIL-Shubham.bansal795@gmail.com                                 
# PHONE-9650335264

# # In this project, I have taken the education data from data.gov.in of number of enrollments done in different classes, different genders, different states and in URBAN AND RURAL AREA.
# # The techniques and libraries i have used in this analysis can be used to analyse Big-Datas, but for the conveneince, here i have chosen relatively smaller datasets.
# # Throughout the analysis I will be comparing the education statistics of rural and urban areas.
# 

# Let's start by importing libraries and data file

# In[1]:


import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt


# I HAVE DIVIDED THE DATASET IN TWO DIFFERENT FILES OF URBAN AND RURAL SO AS TO REDUCE THE CONFUSION.

# In[2]:


df=pd.read_csv("C:/Users/shubham bansal/Desktop/urban910.csv")
df2=pd.read_csv("C:/Users/shubham bansal/Desktop/2.csv")


# Now we can begin to take a wide look of the dataset present

# In[3]:


df.head()


# In[33]:


df.tail()


# In[41]:


df.reset_index


# In[4]:


df2.head()


# In[5]:


df.count()


# In[6]:


print(len(df))


# In[7]:


print(len(df2))


# In[8]:


df.dtypes


# In[9]:


df.columns


# In[10]:


df2.columns


# # Let's begin with data cleaning and wrangling wherever required!!

# In[11]:


df.isnull()


# In[12]:


df2.isnull()


# SO, NO NULL VALUES ARE PRESENT IN THE DATASET

# 
# 
# 
# After getting an overviewof the data it is somewhat clear to us that the data is cleaned here and no missing value is present, so we jump into analytics.
# 

# # Now comes the most important part, the data analytics.
#  # In this dataset, as number of states are more, so we have to use many visualisation algorithms and libraries to properly analyse the data patterns.

# In[13]:


df['STATE/U.T.'][df['Enrolment in Class Total (I to X) - Boys']>df['Enrolment in Class Total (I to X) - Girls']].count()


# In[14]:


df2['STATE/U.T.'][df2['Enrolment in Class Total (I to X)  - Boys']>df2['Enrolment in Class Total (I to X) - Girls']].count()


# # SO OUT OF 35 STATES, 34 HAVE MORE NUMBER OF ENROLLMENTS OF BOYS IN URBAN AREAS.
# # OUT OF 35 STATES, 31 HAVE MORE NUMBER OF ENROLLMENTS OF BOYS IN RURAL AREAS.

# In[15]:


plain_features = [ 'Enrolment in Class IX - Total',
       
       'Enrolment in Class X - Total',
       'Enrolment in Class IX & X - Total',
      
       'Enrolment in Class Total (I to X) - Total']
fig, ax = plt.subplots(nrows = 2, ncols = 2 ,figsize=(20,20))
start = 0
for j in range(2):
    for i in range(2):
        if start == len(plain_features):
            break
        sns.barplot(x=plain_features[start], y='STATE/U.T.', data=df, ax=ax[j,i])
        start += 1


# In urban areas it is clear that the states
# ANDHRA PRADESH, DELHI,KARNATAKA,MADHYAPRADESH, MAHARASHTRA, TAMIL NADU, UP,WEST BENGAL
# have a clear advantage

# # I will be using the same algorithms for both the rural and urban areas to get a clear insight.

# In[16]:


plain_features = [ 'Enrolment in Class IX - Total',
       
       'Enrolment in Class X - Total',
       'Enrolment in Class IX & X - Total',
      
       'Enrolment in Class Total (I to X) - Total']
fig, ax = plt.subplots(nrows = 2, ncols = 2 ,figsize=(20,20))
start = 0
for j in range(2):
    for i in range(2):
        if start == len(plain_features):
            break
        sns.barplot(x=plain_features[start], y='STATE/U.T.', data=df2, ax=ax[j,i])
        start += 1


# In Rural areas it is clear that the states:
# ANDHRA PRADESH, BIHAR, MAHARASHTRA, UP,WEST BENGAL 
# have a clear edge in both boys and girls enrollments.

# In[17]:


fig, ax = plt.subplots(figsize=(15,10))
ax = sns.distplot(df['Enrolment in Class Total (I to X) - Boys'], bins=20, label = 'Boys', ax = ax)
ax = sns.distplot(df['Enrolment in Class Total (I to X) - Girls'], bins=20, label = 'Girls', ax = ax)
ax.legend()
_ = ax.set_ylabel('Number')


# In[18]:


fig, ax = plt.subplots(figsize=(15,10))
ax = sns.distplot(df2['Enrolment in Class Total (I to X)  - Boys'], bins=20, label = 'Boys', ax = ax)
ax = sns.distplot(df2['Enrolment in Class Total (I to X) - Girls'], bins=20, label = 'Girls', ax = ax)
ax.legend()
_ = ax.set_ylabel('Number')


# From above two plots it was found that the number of enrollments of girls is more than double in urban areas than in rural areas.

# In[19]:


fig, ax = plt.subplots(figsize=(15,10))
ax = sns.distplot(df['Enrolment in Class X - Boys'], bins=20, label = 'Boys', ax = ax)
ax = sns.distplot(df['Enrolment in Class X - Girls'], bins=20, label = 'Girls', ax = ax)
ax.legend()
_ = ax.set_ylabel('Number')


# In[20]:


fig, ax = plt.subplots(figsize=(15,10))
ax = sns.distplot(df2['Enrolment in Class X - Boys'], bins=20, label = 'Boys', ax = ax)
ax = sns.distplot(df2['Enrolment in Class X - Girls'], bins=20, label = 'Girls', ax = ax)
ax.legend()
_ = ax.set_ylabel('Number')


# Again the number of enrollment of girls is way more in urban areas.

# In[21]:


fig, ax = plt.subplots(figsize=(15,10))
ax = sns.factorplot('Enrolment in Class Total (I to X) - Total', 'STATE/U.T.',  data=df, ax=ax)


# In[22]:


fig,ax = plt.subplots(figsize=(15,10))
ax = sns.factorplot('Enrolment in Class Total (I to X) - Total', 'STATE/U.T.',  data=df2, ax=ax)


# # From above two plots one of the most important insight can be derived.
# # That is the highest number of enrollment factor in rural areas is 0.4 which is even less than the average of urban areas.
# # So, significant amount of resources are needed to be used in improving rural education stadards.

# In[23]:


fig, ax = plt.subplots(figsize=(15,10))
ax = sns.boxplot( x="Enrolment in Class IX & X - Total",y="STATE/U.T.", data=df)
ax.set_xscale('log')


# In[24]:


fig, ax = plt.subplots(figsize=(15,10))
ax = sns.boxplot( x="Enrolment in Class IX & X - Total",y="STATE/U.T.", data=df2)
ax.set_xscale('log')


# In[25]:


plt.figure(figsize=(15, 15))
corrmap = sns.heatmap(df.corr(),square=True, annot=True)


# # LOOKING AT THE HEAT MAP OF URBAN EDUCATION:
# 1- THE NUMBER OF BOYS ENROLLMENT IN 10 CLASS DOESNOT EFFECT TOTAL BOYS ENROLLMENT MUCH.IT SHOWS THAT IN URBAN AREAS BOYS GET EDUCATION FROM SMALL AGE ITSELF.                          
# 2- THE NUMBER OF GIRLS ENROLLMENT IN 10 CLASS DOESNOT EFFECT TOTAL GIRLS ENROLLMENT MUCH.IT SHOWS THAT IN URBAN AREAS GIRLS ALSO GET EDUCATION FROM SMALL AGE ITSELF.                                                    
# 3-THE NUMBER OF ENROLLMENTS IN 9 CLASS IS VERY HIGH COMPARE TO 10 ENROLLMENTS.

# In[26]:


plt.figure(figsize=(15, 15))
corrmap = sns.heatmap(df2.corr(),square=True, annot=True)


# # THE RESULTS FROM THE HEATMAP PF RURAL AREA IS REALLY SURPRISING

# # 1-THE NUMBER OF ENROLLMENTS OF GIRLS IN CLASS 10 DOES NOT EFFECT THE TOTAL GIRLS ENROLLMENT AT ALL.
# # IT MEANS THAT THE NUMBER OF ENROLLMENTS IN CLASS 10 ARE SIGNIFICANTLY LOW

# # 2- THE NUMBER OF ENROLLMENTS OF GIRLS IN CLASS 9,10, AND (9+10) DOES NOT EFFECT THE TOTAL ENROLLMENTS(BOYS+GIRLS) AT ALL.
# # IT MEANS THAT THE NUMBER OF ENROLLMENTS OF GIRLS IN ALL THE CLASSES ARE SIGNIFICANTLY LOW AS COMPARED TO BOYS.

# # ------------------------------------------------------------------------------------------------------

# # ------------------------------------------------------------------------------------------------------

# # AFTER PERFORMING THIS RIGROUS ANALYSIS ON THE DATA, FEW CONCLUSIONS CAN BE MADE WHICH CAN BE USED FOR MAKING FURTHER GOVERNMENT POLICIES:
# # 1-IN URBAN CITIES, THE CONDITION OF EDUCATION IS AT PAR FOR THE GIRLS. IT NEEDS TO BE IMPROVED BUT OVERALL. NO SPECIFIC RESOURCE ALLOCATION FOR GIRL EDUCATION IS REQUIRED.
# 
# # 2-IN RURAL AREAS/VILLAGES, THE OVERALL EDUCATION IS NOT AT PAR WITH URABAN.. BUT THE MOST DISASTEROUS POINT IS THAT THERE IS A STRONG DISCRIMINATION IN GIRLS AND BOYS WITH REGARDS TO EDUCATION. HENCE GOVERNMENT POLICIES IN VILLAGES SHOULD FOCUS MORE ON GIRLS EDUCATION PRIOR TO OVERALL EDUCATION.
