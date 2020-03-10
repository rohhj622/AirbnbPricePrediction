#-*-coding: utf-8-*-
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


### 에어비앤비 가격 예측 시작
conn = pymysql.connect(host='localhost', user='root', password='shguswls12',db='SpringTest', charset='utf8')
 
conn.query("set character_set_connection=utf8;")
conn.query("set character_set_server=utf8;")
conn.query("set character_set_client=utf8;")
conn.query("set character_set_results=utf8;")
conn.query("set character_set_database=utf8;")

curs = conn.cursor()




X='testdfsf'
Y=63459.0

print(type(Y))
SQL = "insert into airbnb_result(filename,predictPrice) values (%s, %s)"

curs.execute(SQL, (X,Y))
conn.commit()
 
conn.close()
curs.close()



# 
# parser = argparse.ArgumentParser()
# parser.add_argument('X', type=str,
#             help="What is the first number?")
# 
# args = parser.parse_args()
#     
# X = args.X

# 
# def normalizatioUploadFile(z):
#     # skip row 1 so pandas can parse the data properly.
#     uploadFilePath='/Users/hyunjin/Desktop/'+z
#     
#     #'/Users/hyunjin/Documents/dataAnalysis/airbnb/airbnb_listings.csv'  
#        
#     loans_2007 = pd.read_csv(uploadFilePath,header=0,thousands = ',', low_memory=False)
# 
#     engine = create_engine("mysql+pymysql://root:"+"shguswls12"+"@localhost:3306/SpringTest",encoding="utf8")
#     
#     
# #     dataframe=pd.DataFrame(loans_2007_filtered)
# #     dataframe.to_csv(uploadFilePath,index=False)
#     conn = engine.connect()   
#     
#     df=pd.DataFrame(loans_2007)
#     df=df.set_index("id")
#     df.to_sql(name='airbnb_assets', con=engine, if_exists='append')
# 
# normalizatioUploadFile('3ce8f8ff-5e19-4c9f-b2ed-5d36270dc2b3_USAsheville.csv')
### DB 연결 & 읽어오기 시작
# 
# conn = pymysql.connect(host='localhost', user='root', password='shguswls12',db='SpringTest', charset='utf8')
#  
# conn.query("set character_set_connection=utf8;")
# conn.query("set character_set_server=utf8;")
# conn.query("set character_set_client=utf8;")
# conn.query("set character_set_results=utf8;")
# conn.query("set character_set_database=utf8;")
# 
# curs = conn.cursor()
# 
# sql = "select * from airbnb_asset"
# #query = "SQL Sentence"
# curs.execute("set names utf8")
# 
# result = curs.execute(sql)
# conn.commit()
# curs.execute(sql)
# 
# rows = curs.fetchall()
# 
# curs.close()
# conn.close()
# 
# print(rows)
