
# coding: utf-8

# In[1]:

import pandas as pd
get_ipython().magic('pylab inline')


# In[2]:

df = pd.read_csv("train.csv")


# In[3]:

df


# In[10]:

df.describe()


# **PassengerId**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is categorical
# <li> There are no missing values
# <li> Min, Max, Mean, and Standard Deviation not available for PassengerId
# <li> Histograms describing the distribution of the variable not available
# 

# In[4]:

df.PassengerId.value_counts()


# In[73]:

df.PassengerId.describe()


# In[5]:

df[df.PassengerId.isnull()]


# **Survived**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is categorical since it is binary
# <li> There are no missing values
# <li> Min = 0 (not survived), Max = 1 (survived), Mean = 0.383838 survived, and Standard Deviation = 0.486592
# <li> See below for Histogram describing the distribution of the variable

# In[6]:

df.Survived.value_counts()


# In[7]:

df[df.Survived.isnull()]


# In[9]:

df.Survived.describe()


# In[115]:

df.Survived.hist(bins=2)


# **Pclass**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is categorical
# <li> There are no missing values
# <li> Min = 1 (low class), Max = 3 (highest class), Mean = 2.308642, and Standard Deviation = 0.836071 (These values irrelevant)
# <li> See below for Histogram describing the distribution of the variable

# In[18]:

df.Pclass.value_counts()


# In[19]:

df[df.Survived.isnull()]


# In[20]:

df.Pclass.describe()


# In[23]:

df.Pclass.hist(bins=8)


# **Sex**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is categorical
# <li> There are no missing values
# <li> Min, Max, Mean, and Standard Deviation not available for this variable
# <li> Histogram describing the distribution available for this variable below

# In[24]:

df.Sex.value_counts()


# In[25]:

df[df.Sex.isnull()]


# In[38]:

fig, axs = plt.subplots(1,2)
df[df.Sex=='male'].Sex.value_counts().plot(kind='bar', ax=axs[0])
df[df.Sex=='female'].Sex.value_counts().plot(kind='bar', ax=axs[1])


# **Age**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is continuous
# <li> There are 177 missing values
# <li> Min = 0.420000 (youngest age ), Max = 80.000000 (oldest age), Mean = 29.699118, and Standard Deviation = 14.526497
# <li> See below for Histogram describing the distribution of the variable

# In[39]:

df.Age.value_counts()


# In[40]:

df[df.Age.isnull()]


# In[50]:

df[df.Age !=NaN].Age.describe()


# In[57]:

df.Age.hist(bins=80)


# **SibSp**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is continuous
# <li> There are no missing values
# <li> Min = 0.000000, Max = 5.000000, Mean = 0.512605, and Standard Deviation = 0.929783
# <li> See below for Histogram describing the distribution of the variable

# In[58]:

df.SibSp.value_counts()


# In[59]:

df[df.SibSp.isnull()]


# In[60]:

df.SibSp.describe()


# In[63]:

df.SibSp.hist(bins=5)


# **Parch**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is continuous
# <li> There are no missing values
# <li> Min = 0.000000, Max = 6.000000, Mean = 0.431373, and Standard Deviation = 0.853289
# <li> See below for Histogram describing the distribution of the variable

# In[66]:

df.Parch.value_counts()


# In[67]:

df[df.Parch.isnull()]


# In[68]:

df.Parch.describe()


# In[69]:

df.Parch.hist(bins=6)


# **Ticket**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is categorical
# <li> There are no missing values
# <li> Min, Max, Mean, and Standard Deviation not available for this variable
# <li> Histogram describing the distribution not available for this variable

# df.Ticket.value_counts()

# In[71]:

df[df.Ticket.isnull()]


# In[72]:

df.Ticket.describe()


# **Fare**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is continuous
# <li> There are no missing values
# <li> Min = 0.000000, Max = 512.329200, Mean = 34.694514, and Standard Deviation = 52.918930
# <li> See below for Histogram describing the distribution of the variable

# In[74]:

df.Fare.value_counts()


# In[75]:

df[df.Fare.isnull()]


# In[76]:

df.Fare.describe()


# In[81]:

df.Fare.hist(bins=513)


# **Cabin**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is categorical
# <li> There are 529 missing values
# <li> Min, Max, Mean, and Standard Deviation not available for this variable
# <li> Histogram describing the distribution not available for this variable

# In[82]:

df.Cabin.value_counts()


# In[84]:

df[df.Cabin.isnull()]


# In[85]:

df.Cabin.describe()


# **Embarked**
# *(See below code for more information regarding variable)*
# 
# <li> Variable is categorical
# <li> There are 2 missing values
# <li> Min, Max, Mean, and Standard Deviation not available for this variable
# <li> Histogram describing the distribution available for this variable below

# In[89]:

df.Embarked.value_counts()


# In[90]:

df[df.Embarked.isnull()]


# In[91]:

df.Embarked.describe()


# In[114]:

fig, axs = plt.subplots(1,3)
df[df.Embarked=='S'].Embarked.value_counts().plot(kind='bar', ax=axs[0])
df[df.Embarked=='Q'].Embarked.value_counts().plot(kind='bar', ax=axs[1])
df[df.Embarked=='C'].Embarked.value_counts().plot(kind='bar', ax=axs[2])


# In[ ]:



