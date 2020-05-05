#-*-coding: utf-8-*-
import csv
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import string
import math
from sqlalchemy import create_engine
from sklearn.neighbors import KNeighborsRegressor

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.metrics import mean_squared_error

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# ### 매개변수 받기
# ### 업로드한 파일 이름 (장소는 임의로 지정)
# parser = argparse.ArgumentParser()
# parser.add_argument('X', type=str,
#             help="fileName")
# 
# args = parser.parse_args()
#     
# X = args.X # upload file name


# skip row 1 so pandas can parse the data properly.
uploadFilePath='/Users/hyunjin/Desktop/'+'325daeb6-fffc-4e69-a0d3-44bf533cc9fa_000_Cambridge(200222).csv'
 
connDB = pymysql.connect(host='localhost', user='root', password='shguswls12',db='SpringTest', charset='utf8')
 
connDB.query("set character_set_connection=utf8;")
connDB.query("set character_set_server=utf8;")
connDB.query("set character_set_client=utf8;")
connDB.query("set character_set_results=utf8;")
connDB.query("set character_set_database=utf8;")

curs = connDB.cursor()

sql="delete from airbnb_result" #예측결과가 담긴 테이블
print("0") 
curs.execute(sql)
connDB.commit()

sql="delete from airbnb_test" #사용자가 올린 csv데이터 정규화 함. 
print("0.3")  
curs.execute(sql)
connDB.commit()

sql="delete from airbnb_statistics" #통계수치 delete  
print("0.6")  
curs.execute(sql)
connDB.commit()

print("0.9") 
### 정규화 시작      
loans_2007 = pd.read_csv(uploadFilePath,header=0,thousands = ',', low_memory=False)
half_count = len(loans_2007) / 2
loans_2007 = loans_2007.dropna(thresh=half_count,axis=1) # Drop any column with more than 50% missing values
    
print(loans_2007.shape)
    
loans_2007.head()
    
null_counts = loans_2007.isnull().sum()
    
loans_2007_filtered=loans_2007.fillna(1)
    
#print(loans_2007_filtered.isnull().sum())
loans_2007_filtered.shape
    
object_columns_df = loans_2007_filtered.select_dtypes(include=['object'])

int_columns_df = loans_2007_filtered.select_dtypes(include=['int'])
#print(int_columns_df.iloc[0])
    
loans_2007_filtered= loans_2007_filtered.astype('float')
engine = create_engine("mysql+pymysql://root:"+"shguswls12"+"@localhost:3306/SpringTest",encoding="utf8")

new_dataframe=pd.DataFrame(loans_2007_filtered)
#new_dataframe.to_csv(uploadFilePath,index=False) #정규화한 파일 저장

print("끝!!!!!!!!!!!!!1")

conn = engine.connect()   

new_df=new_dataframe.set_index("id") #index해줘야 자동으로 만든 index 삭제함
new_df.to_sql(name='airbnb_test', con=engine, if_exists='append')

print("끝!!!!!!!!!!!!!2")

conn.close()

### 정규화 완료

### 에어비앤비 가격 예측 시작
SQL = "select * from airbnb_assets" # 기본 data + 업로드 data

normalized_listings=pd.read_sql(SQL,connDB)

curs.close()
connDB.close()

print("***************")
#normalized_listings=normalized_listings.sample(frac=1,random_state=0,replace=False) 

#print(len(normalized_listings))

num=int(round(len(normalized_listings)/8))
print(num)

# print("0")
train_num=int(round(num*0.90))
print('train_num : ',train_num)

#print("1")
norm_train_df=normalized_listings.iloc[:train_num]
print('norm_train_df_len : ',len(norm_train_df))

#print("2")
norm_test_df=normalized_listings.iloc[train_num:num]
print('norm_test_df_len : ',len(norm_test_df))

print("***********88")

# cols=['minimum_nights','maximum_nights','number_of_reviews','accommodates','bedrooms','bathrooms','beds']
cols=['accommodates','bedrooms','bathrooms']
# 
print("2.5")
knn=KNeighborsRegressor(algorithm='brute')
# 

print('------------------------------------')
output=normalized_listings


min_max_scaler = MinMaxScaler()
fitted = min_max_scaler.fit(output)

output = min_max_scaler.transform(output)
output = pd.DataFrame(output, columns=normalized_listings.columns, index=list(normalized_listings.index.values))


std_scaler = StandardScaler()
output.head()

fitted = std_scaler.fit(output)

output = std_scaler.transform(output)
output = pd.DataFrame(output, columns=normalized_listings.columns, index=list(normalized_listings.index.values))

###################

out_num=int(round(len(output)/8))
print(out_num)

# print("0")
out_train_num=int(round(out_num*0.90))
print('out_train_num : ',out_train_num)

#print("1")
out_norm_train_df=output.iloc[:train_num]
print('out_norm_train_df_len : ',len(out_norm_train_df))

#print("2")
out_norm_test_df=output.iloc[out_train_num:out_num]
print('out_norm_test_df_len : ',len(out_norm_test_df))

print('------------------------------------')
print("3")
knn.fit(norm_train_df[cols], norm_train_df['price']) #모델제작

four_features_predictions=knn.predict(norm_test_df[cols]) #예측

print('---------------------------분산&표준편차-------------------------------')

norm_test_df['predicted_price']=four_features_predictions

norm_test_df['p_pp_sub']= (norm_test_df['price']-norm_test_df['predicted_price'])

a= norm_test_df['p_pp_sub'].var() #분산
#print("분산 : ",a)

b=norm_test_df['p_pp_sub'].std() #표준편차
#print("표준편차 : ",b)

c=norm_test_df['p_pp_sub'].mean()
#print("평균 : ",c)

d=math.sqrt(len(norm_test_df)) #표준오차

z={'var':[a],'std':[b],'mean':[c],'numsqrt':[d]}

statistics = pd.DataFrame(z)
print(z)

e=abs((norm_test_df['price']-norm_test_df['predicted_price'])) #오차에 절댓값 

trainChart=pd.DataFrame()
trainChart['id']=norm_test_df['id']
trainChart['price']=norm_test_df['price']
trainChart['predictedPrice']=norm_test_df['predicted_price']
trainChart['absError']=e

engine = create_engine("mysql+pymysql://root:"+"shguswls12"+"@localhost:3306/SpringTest",encoding="utf8")
conn = engine.connect()   

result1_df=statistics.set_index("var") #index해줘야 자동으로 만든 index 삭제함

result1_df.to_sql(name='airbnb_statistics', con=engine, if_exists='append')
print("분산,표준편차,평균 넣기 성공")

conn.close()

engine = create_engine("mysql+pymysql://root:"+"shguswls12"+"@localhost:3306/SpringTest",encoding="utf8")
conn = engine.connect()   
# 
print("--22")
result2_df=trainChart.set_index("id") #index해줘야 자동으로 만든 index 삭제함
print("--33")
result2_df.to_sql(name='airbnb_trainChart', con=engine, if_exists='append')
print("가격,예측가격,오차 넣기 성공")

conn.close()

print('---------------------------------끝-------------------------------------')
print("4")
print('------------------------------사용자 csv 예측----------------------------------')
test_df=new_dataframe #예측할 데이터
test_four_features_predictions=knn.predict(test_df[cols])

print("5")

test_df['predicted_price']=test_four_features_predictions #예측값 저장

print("6")
print(test_df['predicted_price']) # 예측값
print(list(test_df))

engine = create_engine("mysql+pymysql://root:"+"shguswls12"+"@localhost:3306/SpringTest",encoding="utf8")
print("이제 인서트하면 끝")
conn = engine.connect()   
print("7")

result_df=test_df.set_index("id") #index해줘야 자동으로 만든 index 삭제함
print("8")

result_df.to_sql(name='airbnb_result', con=engine, if_exists='append')
print("성공")

conn.close()

