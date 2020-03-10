#-*-coding: utf-8-*-

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
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

### 매개변수 받기
### 업로드한 파일 이름 (장소는 임의로 지정)
parser = argparse.ArgumentParser()
parser.add_argument('X', type=str,
            help="fileName")
parser.add_argument('Y', type=str,
            help="tableName")

args = parser.parse_args()
    
X = args.X # upload file name
Y = args.Y # table name


# skip row 1 so pandas can parse the data properly.
uploadFilePath='/Users/hyunjin/Desktop/'+X
    
#'/Users/hyunjin/Documents/dataAnalysis/airbnb/airbnb_listings.csv'  
 
 
### 정규화 시작      
loans_2007 = pd.read_csv(uploadFilePath,header=0,thousands = ',', low_memory=False)
half_count = len(loans_2007) / 2
loans_2007 = loans_2007.dropna(thresh=half_count,axis=1) # Drop any column with more than 50% missing values
    
print(loans_2007.shape)
    
loans_2007.head()
    
null_counts = loans_2007.isnull().sum()
print("Number of null values in each column:\n{}".format(null_counts))    
loans_2007_filtered=loans_2007.fillna(1)
    
print(loans_2007_filtered.isnull().sum())
loans_2007_filtered.shape
    
object_columns_df = loans_2007_filtered.select_dtypes(include=['object'])
print(object_columns_df.iloc[0])
    
loans_2007_filtered['price'] = loans_2007_filtered['price'].str.lstrip('$').str.replace(',', '').astype('float')
    
int_columns_df = loans_2007_filtered.select_dtypes(include=['int'])
print(int_columns_df.iloc[0])
    
loans_2007_filtered= loans_2007_filtered.astype('float')
print("Data types and their frequency\n{}".format(loans_2007_filtered.dtypes.value_counts()))
print(loans_2007_filtered.dtypes)

output=loans_2007_filtered
print(output.head())

min_max_scaler = MinMaxScaler()
fitted = min_max_scaler.fit(output)
print(fitted.data_max_)

output = min_max_scaler.transform(output)
output = pd.DataFrame(output, columns=loans_2007_filtered.columns, index=list(loans_2007_filtered.index.values))
print(output.head())

std_scaler = StandardScaler()
output.head()

fitted = std_scaler.fit(output)
print(fitted.mean_)

output = std_scaler.transform(output)
output = pd.DataFrame(output, columns=loans_2007_filtered.columns, index=list(loans_2007_filtered.index.values))
print(output.head())

engine = create_engine("mysql+pymysql://root:"+"shguswls12"+"@localhost:3306/SpringTest",encoding="utf8")

dataframe=pd.DataFrame(loans_2007_filtered)
dataframe.to_csv(uploadFilePath,index=False)
print("끝!!!!!!!!!!!!!1")

conn = engine.connect()   

df=dataframe.set_index("id") #index해줘야 자동으로 만든 index 삭제함
df.to_sql(name='airbnb_assets', con=engine, if_exists='append')

print("끝!!!!!!!!!!!!!2")

conn.close()

### 정규화 완료

### 에어비앤비 가격 예측 시작
connDB = pymysql.connect(host='localhost', user='root', password='shguswls12',db='SpringTest', charset='utf8')
 
connDB.query("set character_set_connection=utf8;")
connDB.query("set character_set_server=utf8;")
connDB.query("set character_set_client=utf8;")
connDB.query("set character_set_results=utf8;")
connDB.query("set character_set_database=utf8;")

curs = connDB.cursor()

SQL = "select * from airbnb_assets" # 기본 data + 업로드 data

normalized_listings=pd.read_sql(SQL,connDB)

# curs.close()
# conn.close()

normalized_listings=normalized_listings.sample(frac=1,random_state=0)

train_num=round(normalized_listings.shape[0]*0.7)

norm_train_df = normalized_listings.copy().iloc[:train_num]
norm_test_df = normalized_listings.copy().iloc[train_num:]

print(norm_train_df.shape)
print(norm_test_df.shape)

cols = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(algorithm='brute')

knn.fit(norm_train_df[cols], norm_train_df['price'])
two_features_predictions=knn.predict(norm_test_df[cols])

two_features_mse =(two_features_predictions-norm_test_df['price'])**2
norm_test_df['predicted_price']=two_features_predictions
norm_test_df['squared_error']=two_features_mse

print(norm_test_df['predicted_price']) # 예측값
print(norm_test_df['squared_error']) # 에러값
