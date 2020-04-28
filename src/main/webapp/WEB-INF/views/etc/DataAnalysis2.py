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

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.metrics import mean_squared_error

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

connDB = pymysql.connect(host='localhost', user='root', password='shguswls12',db='SpringTest', charset='utf8')
 
connDB.query("set character_set_connection=utf8;")
connDB.query("set character_set_server=utf8;")
connDB.query("set character_set_client=utf8;")
connDB.query("set character_set_results=utf8;")
connDB.query("set character_set_database=utf8;")

curs = connDB.cursor()
SQL = "select * from airbnb_assets" # 기본 data + 업로드 data

normalized_listings=pd.read_sql(SQL,connDB)


connDB.close()

print("-1")
output=normalized_listings


min_max_scaler = MinMaxScaler()
fitted = min_max_scaler.fit(output)
print(fitted.data_max_)

output = min_max_scaler.transform(output)
output = pd.DataFrame(output, columns=normalized_listings.columns, index=list(normalized_listings.index.values))
print(output.head())

std_scaler = StandardScaler()
output.head()

fitted = std_scaler.fit(output)
print(fitted.mean_)

output = std_scaler.transform(output)
output = pd.DataFrame(output, columns=normalized_listings.columns, index=list(normalized_listings.index.values))
print(output.head())


normalized_listings=output

print("***************")
print(normalized_listings.shape)
normalized_listings=normalized_listings.sample(frac=1,random_state=0) 

print("0")
train_num=round(len(normalized_listings)*0.2)


print("1")
norm_train_df=normalized_listings.ix[:train_num]
print(normalized_listings.ix[:train_num])
print(len(norm_train_df))

print("2")
norm_test_df=normalized_listings.ix[train_num:]
#print(normalized_listings.ix[train_num:])
print(len(norm_test_df))
print("***********88")

# cols=['minimum_nights','maximum_nights','number_of_reviews','accommodates','bedrooms','bathrooms','beds']
cols=['accommodates','bedrooms','bathrooms']
# 
print("2.5")
knn=KNeighborsRegressor(algorithm='brute',n_neighbors=5)

# 
print("3")
knn.fit(norm_train_df[cols], norm_train_df['price']) #모델제작

four_features_predictions=knn.predict(norm_test_df[cols]) #예측
# 
print("4")
four_features_mse = mean_squared_error(norm_test_df['price'], four_features_predictions)
print('four_features_mse : ',four_features_mse)

four_features_rmse=four_features_mse ** (1/2)

print('four_features_rmse : ',four_features_rmse)

