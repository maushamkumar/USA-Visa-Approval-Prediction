import pandas as pd 
import pymongo

df = pd.read_csv('Notebook/EasyVisa.csv')

data = df.to_dict(orient='records')

DB_NAME = "US_VISA"
COLLETION_NAME = "VISA"
CONNECTION_URL = 'mongodb+srv://maushamkumarr26:maushamkumarr26@cluster0.lke4x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = pymongo.MongoClient(CONNECTION_URL)
# Once we have created a client now we have to create a database
data_base = client[DB_NAME]
collection = data_base[COLLETION_NAME]

# rec = collection.insert_many(data)


records = collection.find()
records

# for i, j in enumerate(records):
#     print(f"{i}: {j}")
    
df = pd.DataFrame(list(collection.find()))
print(df.head())