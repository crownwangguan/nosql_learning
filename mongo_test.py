import pymongo

client = pymongo.MongoClient('localhost', 27017)
# db = client['test-database']

# collection = db['test-collection']

# test_data = {'age': 25, 'gender': 'M', 'occupation': 'Software Engineer'}
# insert_result = collection.insert_one(test_data)

# print(insert_result)
# print(collection.count())

# delete_result = collection.delete_one({'age': 25})
# print(collection.count())

db = client['chapter3']
collection = db['income']

# with open('income_header.txt') as f_in:
# 	columns_headings = f_in.readline()

# columns_headings_list = columns_headings.split(',')

# row_dict_list = list()
# with open('income.txt') as f_in:
# 	for line in f_in:
# 		row_list = line.rstrip('\n').split(',')
# 		row_dict = dict(zip(columns_headings_list, row_list))
# 		row_dict_list.append(row_dict)
# 		collection.insert_one(row_dict)

# print(collection.count())

# collection.delete_many({})

# with open('income_header.txt') as f_in:
# 	columns_headings = f_in.readline()

# columns_headings_list = columns_headings.split(',')

# row_dict_list = list()
# with open('income.txt') as f_in:
# 	for line in f_in:
# 		row_list = line.rstrip('\n').split(',')
# 		row_dict = dict(zip(columns_headings_list, row_list))
# 		try:
# 			row_dict['age'] = int(row_dict['age'])
# 			collection.insert_one(row_dict)
# 		except:
# 			pass

# over_35 = collection.find({'age': {"$gt": 35}})
# print(over_35.next())
# print(over_35.count())

import time

start = time.time()
age50 = collection.find({'age': {'$eq':50}})
end = time.time()
print(end - start)

index_result = db.profiles.create_index([('age', pymongo.ASCENDING)], unique=False)

start = time.time()
age50 = collection.find({'age': {'$eq':50}})
end = time.time()
print(end - start)