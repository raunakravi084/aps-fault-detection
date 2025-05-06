import pymongo
import pandas as pd
import json
uri = "mongodb+srv://root:root@cluster0.zujon.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri)

DATA_FILE_PATH = "D:\\VScode\\APS_sensor_failure_Project\\aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ =="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")
    
    # Convert the dataframe to JSON format so that we can insert it into MongoDB
    
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])
    
    # Insert the JSON record into MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)