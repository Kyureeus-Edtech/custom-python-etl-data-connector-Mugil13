import requests
import time

def extract_json(endpoint_name, url):
    headers = {"User-Agent": "Mugil-ETL-Connector"}
    
    for attempt in range(3):
        try:
            print(f"[INFO] Fetching data from {endpoint_name}, attempt {attempt+1}...")
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"[ERROR] HTTPError for {endpoint_name}: {e}")
            if response.status_code == 429:
                print("[INFO] Rate limit hit, waiting 30 seconds...")
                time.sleep(30)
            else:
                break
        except Exception as e:
            print(f"[ERROR] Failed to fetch {endpoint_name}: {e}")
            break
    return None
