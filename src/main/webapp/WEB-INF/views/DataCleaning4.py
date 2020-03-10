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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


conn = pymysql.connect(host='localhost', user='root', password='shguswls12',db='SpringTest', charset='utf8')
 
conn.query("set character_set_connection=utf8;")
conn.query("set character_set_server=utf8;")
conn.query("set character_set_client=utf8;")
conn.query("set character_set_results=utf8;")
conn.query("set character_set_database=utf8;")

curs = conn.cursor()

SQL = "select * from airbnb_assets" # 기본data + 업로드 data

dc_listings=pd.read_sql(SQL,conn)
print(dc_listings.shape)
print(dc_listings.head())

our_acc_value=3
first_living_space_value=dc_listings.loc[0,'accommodates']

first_distance=np.abs(first_living_space_value - our_acc_value)

print(first_distance)

dc_listings['distance']=np.abs(dc_listings.accommodates- our_acc_value)
dc_listings.distance.value_counts().sort_index()

dc_listings=dc_listings.sample(frac=1,random_state=0)
dc_listings=dc_listings.sort_values('distance')
dc_listings.price.head()

mean_price=dc_listings.price.iloc[:5].mean()
print(mean_price) #최적가격


dc_listings.drop('distance',axis=1)

train_df=dc_listings.copy().iloc[:2792]
test_df=dc_listings.copy().iloc[2792:]

def predict_price(new_listing_value,feature_column):
    temp_df=train_df
    temp_df['distance']=np.abs(dc_listings[feature_column]-new_listing_value)
    temp_df=temp_df.sort_values('distance')
    knn_5=temp_df.price.iloc[:5]
    predicted_price=knn_5.mean()
    return(predicted_price)

test_df['predicted_price']=test_df.accommodates.apply(predict_price,feature_column='accommodates')
print(test_df['predicted_price'])




# 
# 
# curs.execute("set names utf8")
# result = curs.execute(sql)
# conn.commit()
# curs.execute(sql)
# rows = curs.fetchall()
# curs.close()
# conn.close()




# def normalizatioUploadFile(z):
#     # skip row 1 so pandas can parse the data properly.
#     uploadFilePath='/Users/hyunjin/Desktop/'+z
#     
#     #'/Users/hyunjin/Documents/dataAnalysis/airbnb/airbnb_listings.csv'  
#        
#     loans_2007 = pd.read_csv(uploadFilePath,header=0,thousands = ',', low_memory=False)
#     half_count = len(loans_2007) / 2
#     loans_2007 = loans_2007.dropna(thresh=half_count,axis=1) # Drop any column with more than 50% missing values
#     
#     print(loans_2007.shape)
#     
#     loans_2007.head()
#     
#     null_counts = loans_2007.isnull().sum()
#     print("Number of null values in each column:\n{}".format(null_counts))
#     
#     loans_2007_filtered=loans_2007.fillna(1)
#     
#     print(loans_2007_filtered.isnull().sum())
#     loans_2007_filtered.shape
#     
#     object_columns_df = loans_2007_filtered.select_dtypes(include=['object'])
#     print(object_columns_df.iloc[0])
#     
#     loans_2007_filtered['price'] = loans_2007_filtered['price'].str.lstrip('$').str.replace(',', '').astype('float')
#     
#     int_columns_df = loans_2007_filtered.select_dtypes(include=['int'])
#     print(int_columns_df.iloc[0])
#     
#     loans_2007_filtered= loans_2007_filtered.astype('float')
#     print("Data types and their frequency\n{}".format(loans_2007_filtered.dtypes.value_counts()))
#     print(loans_2007_filtered.dtypes)
# 
#     engine = create_engine("mysql+pymysql://root:"+"shguswls12"+"@localhost:3306/SpringTest",encoding="utf8")
# 
#     dataframe=pd.DataFrame(loans_2007_filtered)
#     dataframe.to_csv(uploadFilePath,index=False)
#     
#     conn = engine.connect()   
#     
#     df=pd.DataFrame(loans_2007)
#     df=df.set_index("id") #index해줘야 자동으로 만든 index 삭제함
#     df.to_sql(name='airbnb_assets', con=engine, if_exists='append')
#     print("끝!!!!!!!!!!!!!")
# 
# normalizatioUploadFile(X)


### DB 연결 & 읽어오기 시작
# conn = pymysql.connect(host='localhost', user='root', password='shguswls12',db='SpringTest', charset='utf8')
#   
# conn.query("set character_set_connection=utf8;")
# conn.query("set character_set_server=utf8;")
# conn.query("set character_set_client=utf8;")
# conn.query("set character_set_results=utf8;")
# conn.query("set character_set_database=utf8;")
# 
# curs = conn.cursor()
# ### DB �곌껐 ��
# 
# ### DB �곌껐 & �쎌�댁�ㅺ린 ����
# # 
# # curs = conn.cursor()
# # 
# # sql = "select * from airbnb_asset"
# # #query = "SQL Sentence"
# # curs.execute("set names utf8")
# # 
# # result = curs.execute(sql)
# # conn.commit()
# # curs.execute(sql)
# # 
# # rows = curs.fetchall()
# # 
# # curs.close()
# # conn.close()
# # 
# # print(rows)
# 
# ### DB �곌껐 & �쎌�댁�ㅺ린 ��
# dc_listings = pd.read_csv('/Users/hyunjin/Documents/dataAnalysis/airbnb/airbnb_listings.csv', low_memory=False)
# print(dc_listings.shape)
# dc_listings.head()
# our_acc_value=3
# first_living_space_value=dc_listings.loc[0,'accommodates']
# 
# first_distance=np.abs(first_living_space_value - our_acc_value)
# 
# print(first_distance)
# 
# dc_listings['distance']=np.abs(dc_listings.accommodates- our_acc_value)
# dc_listings.distance.value_counts().sort_index()
# 
# dc_listings=dc_listings.sample(frac=1,random_state=0)
# dc_listings=dc_listings.sort_values('distance')
# dc_listings.price.head()
# 
# dc_listings['price']=dc_listings.price.str.replace("\$|,",'').astype(float)
# 
# mean_price=dc_listings.price.iloc[:5].mean()
# mean_price
# 
# dc_listings.drop('distance',axis=1)
# 
# train_df=dc_listings.copy().iloc[:2792]
# test_df=dc_listings.copy().iloc[2792:]
# 
# def predict_price(new_listing_value,feature_column):
#     temp_df=train_df
#     temp_df['distance']=np.abs(dc_listings[feature_column]-new_listing_value)
#     temp_df=temp_df.sort_values('distance')
#     knn_5=temp_df.price.iloc[:5]
#     predicted_price=knn_5.mean()
#     return(predicted_price)
# 
# test_df['predicted_price']=test_df.accommodates.apply(predict_price,feature_column='accommodates')
# print(test_df['predicted_price'])
# 
# test_df['squared_error']=(test_df['predicted_price']-test_df['price'])**(2)
# mse=test_df['squared_error'].mean()
# rmse=mse**(1/2)
# rmse
# 
# for feature in ['accommodates','bedrooms','bathrooms','number_of_reviews']:
#     test_df['predicted_price'] = test_df.accommodates.apply(predict_price,feature_column=feature)
# 
#     test_df['squared_error'] = (test_df['predicted_price'] - test_df['price'])**(2)
#     mse = test_df['squared_error'].mean()
#     rmse = mse ** (1/2)
#     print("RMSE for the {} column: {}".format(feature,rmse))
#     
#     
# # skip row 1 so pandas can parse the data properly.
# loans_2007 = pd.read_csv('/Users/hyunjin/Documents/dataAnalysis/airbnb/airbnb_listings.csv',thousands = ',', low_memory=False)
# half_count = len(loans_2007) / 2
# loans_2007 = loans_2007.dropna(thresh=half_count,axis=1) # Drop any column with more than 50% missing values
# 
# print(loans_2007.shape)
# 
# loans_2007.head()
# 
# null_counts = loans_2007.isnull().sum()
# print("Number of null values in each column:\n{}".format(null_counts))
# 
# loans_2007_filtered=loans_2007.fillna(1)
# 
# print(loans_2007_filtered.isnull().sum())
# loans_2007_filtered.shape
# 
# object_columns_df = loans_2007_filtered.select_dtypes(include=['object'])
# print(object_columns_df.iloc[0])
# 
# loans_2007_filtered['price'] = loans_2007_filtered['price'].str.lstrip('$').str.replace(',', '').astype('float')
# 
# int_columns_df = loans_2007_filtered.select_dtypes(include=['int'])
# print(int_columns_df.iloc[0])
# 
# loans_2007_filtered= loans_2007_filtered.astype('float')
# print("Data types and their frequency\n{}".format(loans_2007_filtered.dtypes.value_counts()))
# 
# from sklearn.preprocessing import MinMaxScaler
# 
# output=loans_2007_filtered
# print(output.head())
# 
# min_max_scaler = MinMaxScaler()
# fitted = min_max_scaler.fit(output)
# print(fitted.data_max_)
# 
# output = min_max_scaler.transform(output)
# output = pd.DataFrame(output, columns=loans_2007_filtered.columns, index=list(loans_2007_filtered.index.values))
# print(output.head())
# 
# from sklearn.preprocessing import StandardScaler
# std_scaler = StandardScaler()
# output.head()
# 
# fitted = std_scaler.fit(output)
# print(fitted.mean_)
# 
# output = std_scaler.transform(output)
# output = pd.DataFrame(output, columns=loans_2007_filtered.columns, index=list(loans_2007_filtered.index.values))
# print(output.head())
# 
# normalized_listings=output
# print(normalized_listings.shape)
# normalized_listings.head()
# 
# normalized_listings = normalized_listings.sample(frac=1,random_state=0)
# 
# norm_train_df = normalized_listings.copy().iloc[0:2792]
# norm_test_df = normalized_listings.copy().iloc[2792:]
# 
# from scipy.spatial import distance
# 
# first_listing = normalized_listings.iloc[0][['accommodates', 'bathrooms']]
# fifth_listing = normalized_listings.iloc[20][['accommodates', 'bathrooms']]
# first_fifth_distance = distance.euclidean(first_listing, fifth_listing)
# first_fifth_distance
# 
# def predict_price_multivariate(new_listing_value,feature_columns):
#     temp_df = norm_train_df
#     temp_df['distance'] = distance.cdist(temp_df[feature_columns],[new_listing_value[feature_columns]])
#     temp_df = temp_df.sort_values('distance')
#     knn_5 = temp_df.price.iloc[:5]
#     predicted_price = knn_5.mean()
#     return(predicted_price)
# 
# cols = ['accommodates', 'bathrooms']
# norm_test_df['predicted_price'] = norm_test_df[cols].apply(predict_price_multivariate,feature_columns=cols,axis=1)    
# norm_test_df['squared_error'] = (norm_test_df['predicted_price'] - norm_test_df['price'])**(2)
# mse = norm_test_df['squared_error'].mean()
# rmse = mse ** (1/2)
# print(rmse)


