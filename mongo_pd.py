import pymongo
import pandas as pd


client = pymongo.MongoClient('localhost', 27017)
db = client['chapter3']
collection = db['income']

income_df = pd.DataFrame(list(collection.find()))
print(income_df.head())
print(income_df.tail())
print(income_df['age'].describe())