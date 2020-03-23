#-*-coding: utf-8-*-

import csv
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import string
from sqlalchemy import create_engine
from sklearn.neighbors import KNeighborsRegressor
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


### 정규화 시작      
loans_2007 = pd.read_csv('/Users/hyunjin/Documents/dataAnalysis/airbnb/us/0_Cambridge(200222).csv',header=0,thousands = ',', low_memory=False)
df=loans_2007.sample(n=100)

print(df.shape)
print(df.head())

# half_count = len(loans_2007) / 2
# loans_2007 = loans_2007.dropna(thresh=half_count,axis=1) # Drop any column with more than 50% missing values
#     
# print(loans_2007.shape)
#     
# loans_2007.head()
#     
# null_counts = loans_2007.isnull().sum()
# print("Number of null values in each column:\n{}".format(null_counts))    
# loans_2007_filtered=loans_2007.fillna(1)
#     
# print(loans_2007_filtered.isnull().sum())
# loans_2007_filtered.shape
#     
# object_columns_df = loans_2007_filtered.select_dtypes(include=['object'])
# print(object_columns_df.iloc[0])
#     
# #loans_2007_filtered['price'] = loans_2007_filtered['price'].str.lstrip('$').str.replace(',', '').astype('float')
#     
# int_columns_df = loans_2007_filtered.select_dtypes(include=['int'])
# print(int_columns_df.iloc[0])
#     
# loans_2007_filtered= loans_2007_filtered.astype('float')
# print("Data types and their frequency\n{}".format(loans_2007_filtered.dtypes.value_counts()))
# print(loans_2007_filtered.dtypes)