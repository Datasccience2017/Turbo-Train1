
# coding: utf-8

# In[1]:


#import pandas, numpy, matplotlib, pickle and math


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
from math import pi


# In[3]:


#import file by using pandas


# In[4]:


data = pd.read_csv('E:\R\credit.csv')


# In[5]:


#look at the information


# In[6]:


data.head(5)


# In[7]:


data.isnull().all()  # Checking if any Null in features


# In[8]:


# So with  result of above command, Result reflects no Null in any features.


# In[10]:


data.describe()  #summary of the data


# In[11]:


# Change the data to dataframe


# In[12]:


dataf = pd.DataFrame(data)


# In[13]:


dataf.shape # Look at Dimensions of complete  data


# In[14]:


dataf.isnull().any()


# In[15]:


# Still there is no any Null 


# In[16]:


dataf.head(5)


# In[17]:


dataf['count'] = 1 # add a counter to the Dataframe for future Grouping


# In[18]:


dataf.head()  # Counter was added to Back of DataFrame


# In[18]:


dataf['count'] # Look at data column


# In[19]:


dataf.columns  # Look at all columns


# In[20]:


datame = dataf[['checking_status', 'duration', 'credit_history', 'purpose',
       'credit_amount', 'savings_status', 'employment',
       'installment_commitment', 'personal_status', 'other_parties',
       'residence_since', 'property_magnitude', 'age', 'other_payment_plans',
       'housing', 'existing_credits', 'job', 'num_dependents', 'own_telephone',
       'foreign_worker', 'class', 'count']]


# In[21]:


datame.head(100)  #Look at dataframe


# In[22]:


checkacct = []  # Adding new column checkacct with respect to existing column "checking_status".if no checking then "No" else "yes"

for row in datame.checking_status:
    if row in ['no checking']:
        checkacct.append('no')
    else:
        checkacct.append('yes')
            
datame['checkacct'] = checkacct


# In[23]:


datame.head()


# In[24]:


saveacct = []    # Adding new column saveacct with respect to existing column savings_status.if "no known savings" then "No" else "yes"


for row in datame.savings_status:
    if row in ['no known savings']:
        saveacct.append('no')
    else:
        saveacct.append('yes')
        
datame['saveacct'] = saveacct


# In[25]:


datame.head(100)


# In[26]:


datame.columns


# In[27]:


datause = datame[['count','checkacct', 'saveacct',  'credit_history', 'purpose',
       'credit_amount',  'employment',
       'installment_commitment', 'personal_status', 'residence_since', 'age',
       'housing', 'existing_credits', 'job', 'num_dependents',
       'foreign_worker', 'class']]


# In[28]:


datause.head()


# In[30]:


datause['personal_status'].unique     #look at all the data in a column


# In[31]:


gender = []

for row in datause.personal_status:
    if row in ['male single', 'male mar/wid', 'male div/sep']:
        gender.append('male')
    else:
        gender.append('female')
        
datause['gender'] = gender


# In[32]:


datause.head(100)


# In[33]:


datause = datause[['count','class','age','gender','credit_history','checkacct', 'saveacct', 'num_dependents', 'housing', 'foreign_worker',  'employment','job', 'residence_since',
       'credit_amount', 'existing_credits']]


# In[34]:


datause.head(100)


# In[35]:


datause['employment'].unique


# In[36]:


employment = []

for row in datause.employment:
    if row in ['unemployed']:
        employment.append('unemployed')
    else:
        employment.append('employed')
        
datause['employment'] = employment


# In[36]:


datause.head(15)


# In[61]:


datause['age'].unique


# In[37]:


datause['age_bins'] = pd.cut(datause['age'], 6)  #to create bins


# In[39]:


datause['agerange'] = pd.cut(x=datause['age'], bins=[20, 30, 40, 50, 60, 70, 80], labels=['20', '30', '40','50', '60','70'])

#set bins in a range


# In[40]:


datause.columns


# In[41]:


datanew= datause[['count','class','agerange','age','gender','credit_history','checkacct', 'saveacct', 'num_dependents', 'housing', 'foreign_worker',  'employment','job', 'residence_since',
       'credit_amount', 'existing_credits']]


# In[42]:


datanew.head(100)


# In[43]:


datanew['job'].unique()


# In[44]:


jobskill = []

for row in datanew.job:
    if row in ['skilled']:
        jobskill.append('skill')
    elif row in ['unskilled resident']:
        jobskill.append('unskill')
    elif row in ['high qualif/self emp/mgmt']:
        jobskill.append('high skill')        
        
    else:
        jobskill.append('unemployed')
        
datanew['jobskill'] = jobskill


# In[45]:


datanew['jobskill'].unique()


# In[46]:


datanew = datanew[['count', 'class','agerange','age','gender', 'credit_history', 'checkacct','saveacct', 'num_dependents', 'housing', 'foreign_worker', 'employment',
       'jobskill', 'residence_since', 'credit_amount', 'existing_credits']]


# In[47]:


datanew.head(100)


# In[48]:


datanew['credit_amount'].unique()


# In[49]:


datanew['credit_amount_bins'] = pd.cut(x=datanew['credit_amount'], bins=[250, 3972, 8000, 10424, 18424 ])

#datanew.describe()


# In[50]:


datanew.head(6)


# In[51]:


datanew['credit_amount_bins'].unique()


# In[52]:


datanew['credit_amount_range'] = pd.cut(x=datanew['credit_amount'], bins=[250, 3972, 8000, 10424, 18424], labels=['low', 'mid', 'high', 'very-high'])


# In[53]:


datanew['credit_amount_range'].unique()


# In[54]:


datanew = datanew[['count', 'class','agerange','age','gender', 'credit_history', 'checkacct','saveacct', 'num_dependents', 'housing', 'foreign_worker', 'employment',
       'jobskill', 'residence_since', 'credit_amount', 'credit_amount_range', 'existing_credits']]


# In[55]:


datanew.head(10)


# In[56]:


datanew['num_dependents'].unique()


# In[57]:



datanew = datanew[['count', 'class', 'agerange', 'age', 'gender', 'credit_history', 'checkacct','saveacct', 'housing', 'foreign_worker', 'employment',
       'jobskill', 'residence_since', 'credit_amount_range', 'existing_credits']]


# In[58]:


datanew.head(10)


# In[59]:


datanew['credit_history'].unique()


# In[62]:


datanew.isnull().any()  #we have nulls -- need to fix


# In[63]:


datanew.isnull().sum()  #how many nulls per column


# In[64]:


dfage = datanew.groupby(['agerange'])


# In[65]:


dfage.head(2)


# In[66]:


#datanew['agerange'] = pd.to_numeric(datanew['agerange'])


# In[67]:


datanew['agerange'].isnull().any()


# In[68]:



#fix the nulls by copy one column to another

def fx(x):
    if pd.isnull(x['agerange']):
        return x['age']
    else:
        return x['agerange']

    print(datanew) 


datanew['agerange'] = datanew.apply(lambda x : fx(x), axis = 1)

print(datanew)


# In[69]:


datanew['agerange'].isnull().any()  #now fixed


# In[70]:


datanew.head()


# In[71]:


datanew['credit_amount_range'].isnull().any()


# In[72]:


datanew = datanew.dropna(axis=0)  #since it is one record, just delete


# In[73]:


datanew['credit_amount_range'].isnull().any()


# In[74]:


data.isnull().sum()


# In[75]:


datanew['agerange'].unique()  #float - no good


# In[76]:


datanew.info(['agerange'])  #looking at the information


# In[77]:


datanew['agerange'] = np.int64(datanew['agerange'])  #change float to int64


# In[78]:


datanew.info()


# In[79]:


datanew['target'] = ''  #for machine learning


# In[80]:


datanew.columns


# In[81]:


main = datanew[['count', 'class', 'agerange',  'gender', 'credit_history',
       'checkacct', 'saveacct', 'housing', 'foreign_worker', 'employment',
       'jobskill', 'residence_since', 'credit_amount_range',
       'existing_credits', 'target']]


# In[82]:


main.columns


# In[83]:


main.groupby('class').sum()  

#grouping -- remember the counter 
#bad credit is 300
#good credit is 699


# In[84]:


main.describe()

