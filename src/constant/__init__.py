import os


AWS_S3_BUCKET_NAME = "Diamond-Price"
MONGO_DATABASE_NAME = "DimondPricePrediction"
MONGO_COLLECTION_NAME = "Diamond_Price"

TARGET_COLUMN = "price"
MONGO_DB_URL="mongodb+srv://pgmahajanott:pgmahajanott@cluster0.mevcvot.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"