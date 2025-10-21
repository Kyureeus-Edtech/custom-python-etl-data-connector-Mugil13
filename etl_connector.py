import os
from dotenv import load_dotenv
from api_utils import extract_json
from transform_utils import transform_json
from db_utils import load_to_mongo

# ---------- Load Environment ----------
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB_NAME")
NVD_API_KEY = os.getenv("NVD_API_KEY")

# ---------- API Endpoints ----------
ENDPOINTS = {
    "recent_vulnerabilities": f"https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage=20&apiKey={NVD_API_KEY}",
    "modified_vulnerabilities": f"https://services.nvd.nist.gov/rest/json/cves/1.0?modStartDate=2025-01-01T00:00:00:000 UTC-00:00&resultsPerPage=20&apiKey={NVD_API_KEY}",
    "cpe_dictionary": f"https://services.nvd.nist.gov/rest/json/cpes/1.0?resultsPerPage=20&apiKey={NVD_API_KEY}"
}

# ---------- MAIN FUNCTION ----------
def main():
    for endpoint_name, url in ENDPOINTS.items():
        json_data = extract_json(endpoint_name, url)
        records = transform_json(endpoint_name, json_data)
        load_to_mongo(endpoint_name, records, MONGO_URI, MONGO_DB)

if __name__ == "__main__":
    main()
