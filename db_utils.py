from pymongo import MongoClient

def load_to_mongo(endpoint_name, records, mongo_uri, mongo_db):
    try:
        if not records:
            print(f"[ERROR] No records to load for {endpoint_name}")
            return

        client = MongoClient(mongo_uri)
        db = client[mongo_db]
        collection = db[f"{endpoint_name}_raw"]

        print(f"[INFO] Loading {len(records)} records into MongoDB collection: {endpoint_name}_raw")
        collection.insert_many(records)
        print("[INFO] Load successful.\n")

    except Exception as e:
        print(f"[ERROR] Failed to load {endpoint_name}: {e}")
