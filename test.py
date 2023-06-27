from pymongo.mongo_client import MongoClient
import pandas as pd
import json


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://pgmahajanott:pgmahajanott@cluster0.mevcvot.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

#Read data as datafream

df=pd.read_csv(r'C:\Users\pmoff\OneDrive\Desktop\PWSkills\MLProjects\DiamondPricePrediction\notebooks\data\gemstone.csv')

json_records = json.load(df.T.to_json)

#Create database name and collection
dqatabase_name = 'DimondPricePrediction'
collection_name = 'Diamond_Price

#now dump the data in db
client[dqatabase_name][collection_name]=json_records
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)