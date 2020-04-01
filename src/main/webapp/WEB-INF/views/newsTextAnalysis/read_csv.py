import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://DAN:dudeks7052@localhost/AI',convert_unicode=True)
conn = engine.connect()

data = pd.read_sql_table('uploadfile', conn)
print(data.head())