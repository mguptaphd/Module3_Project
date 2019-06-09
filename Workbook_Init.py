#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3        # for importing the .db file
import pandas as pd   # for dataframe viewing
import numpy as np    # for arrays
import statsmodels.api as sm  # for proportion z-tests
from scipy.stats import chisquare  # for chi-squared tests
from scipy.stats import chi2_contingency
import warnings

from scipy.stats import ttest_ind_from_stats  # for overall t-test

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns

sns.set_style("whitegrid")

pd.set_option("display.max_columns", 500)
pd.options.display.max_colwidth = 100


# In[ ]:


def sample_from_traffic(n_sample, connection, race=None, gender=None, show_SQL=True):
    """Returns a random sample from the specified sqlite db connection, from the table called traffic.
    Order is randomized.
    Can specify a race and gender to filter on.
    Prints the equivalent SQL query.
    Returns the dataframe result of the SQL query"""
    var_count = 0
    if race:
        condition = "WHERE race ='{}'".format(race.upper())
        var_count += 1
    else:
        condition = "--"
    if gender:
        if var_count > 0:
            condition = condition + """
            AND Gender = '{}'""".format(gender.upper()[0])
        else:
            condition = "WHERE gender ='{}'".format(gender.upper()[0])
    sql_str = '''
        SELECT * FROM traffic
        {0}
        ORDER BY RANDOM() 
        LIMIT {1}
        '''.format(condition, n_sample)
    if show_SQL: print(sql_str)
    df = pd.read_sql_query(sql_str, connection)
    return df


# In[ ]:


def sample_from_traffic_2(n_sample, connection, filters={}, show_SQL=True):
    """Returns a random sample from the specified sqlite db connection, from the table called traffic.
    Order is randomized.
    
    Can input a filter dictionary of key, value paris of "column name":[list of possible values]
    or "column name":"single value"
    
    Prints the equivalent SQL query.
    Returns the dataframe result of the SQL query"""
    var_count = 0
    condition = "--"
    for k, v in filters.items():
        if var_count==0:
            if type(v)!=str:
                condition = "WHERE {0} in {1}".format(k, tuple(v))
            else:
                condition = "WHERE {0} = '{1}'".format(k, v)
        else:
            if type(v)!=str:
                condition = condition + """
                AND {0} in {1}""".format(k, tuple(v))
            else:
                condition = condition + """
                AND {0} = '{1}'""".format(k, v)
        
        var_count += 1

    sql_str = '''
        SELECT * FROM traffic
        {0}
        ORDER BY RANDOM() 
        LIMIT {1}
        '''.format(condition, n_sample)
    if show_SQL: print(sql_str)
    df = pd.read_sql_query(sql_str, connection)
    return df


# In[5]:


def sample_from_traffic_3(n_sample, connection, filters={}, show_SQL=True):
    """Returns a random sample from the specified sqlite db connection, from the table called traffic.
    Fields are first aggregated on unique SeqID
    
    Order is randomized.
    
    Can input a filter dictionary of key, value paris of "column name":[list of possible values]
    or "column name":"single value"
    
    Prints the equivalent SQL query.
    Returns the dataframe result of the SQL query"""
    var_count = 0
    condition = "--"
    for k, v in filters.items():
        if var_count==0:
            if k.title() == 'Description':
                condition = "WHERE {0} LIKE '%{1}%'".format(k, v)
            elif type(v)!=str:
                condition = "WHERE {0} in {1}".format(k, tuple(v))
            else:
                condition = "WHERE {0} = '{1}'".format(k, v)
        else:
            if k.title() == 'Description':
                condition = condition + """
                AND {0} LIKE '%{1}%'""".format(k, v)
            elif type(v)!=str:
                condition = condition + """
                AND {0} in {1}""".format(k, tuple(v))
            else:
                condition = condition + """
                AND {0} = '{1}'""".format(k, v)
        
        var_count += 1

    sql_str = '''
        SELECT * FROM traffic_unique
        {0}
        ORDER BY RANDOM() 
        LIMIT {1}
        '''.format(condition, n_sample)
    if show_SQL: print(sql_str)
    df = pd.read_sql_query(sql_str, connection)
    return df


# In[6]:


def print_repeated_test_results(p_list, null_hyp, alpha=0.05):
    num_reject = sum(np.array(p_list) < alpha)
    n = len(p_list)
    print("H0: {}\n".format(null_hyp))
    print("Out of {0} repeated tests, the null hypothesis was rejected {1} times ({2:.1%}) at an alpha level of {3}.".format(n, num_reject, num_reject/n, alpha))


# In[3]:


def sampleprops_to_ttest(mu_list_1, mu_list_2, equal_var=False):
    mu_1 = np.mean(mu_list_1)
    mu_2 = np.mean(mu_list_2)

    n_1 = len(mu_list_1)
    n_2 = len(mu_list_2)

    std_1 = np.sqrt(mu_1 * (1-mu_1) / n_1)
    std_2 = np.sqrt(mu_2 * (1-mu_2) / n_2)

    return ttest_ind_from_stats(mu_1, std_1, n_1, mu_2, std_2, n_2, equal_var=equal_var)


# In[5]:


def print_test_results(p_value, null_hyp, alpha=0.05):
    print("H0: {}\n".format(null_hyp))
    print("Results: p-value = {}\n".format(p_value))
    if p_value < alpha:
        print("Null hypothesis rejected at alpha = {} level.".format(alpha))
    else:
        print("Fail to reject null hypothesis at alpha = {} level.".format(alpha))


# In[ ]:




