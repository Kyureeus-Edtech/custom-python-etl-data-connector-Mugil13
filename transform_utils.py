from datetime import datetime, timezone

def transform_json(endpoint_name, json_data):
    try:
        if not json_data:
            print(f"[ERROR] No data to transform for {endpoint_name}")
            return None

        records = []
        if endpoint_name in ["recent_vulnerabilities", "modified_vulnerabilities"]:
            for item in json_data.get("result", {}).get("CVE_Items", []):
                record = {
                    "cve_id": item.get("cve", {}).get("CVE_data_meta", {}).get("ID"),
                    "description": item.get("cve", {}).get("description", {}).get("description_data", [{}])[0].get("value"),
                    "publishedDate": item.get("publishedDate"),
                    "lastModifiedDate": item.get("lastModifiedDate"),
                    "ingested_at": datetime.now(timezone.utc)
                }
                records.append(record)

        elif endpoint_name == "cpe_dictionary":
            for item in json_data.get("result", {}).get("cpes", []):
                record = {
                    "cpe23Uri": item.get("cpe23Uri"),
                    "title": item.get("titles", [{}])[0].get("title"),
                    "ingested_at": datetime.now(timezone.utc)
                }
                records.append(record)

        print(f"[INFO] Transformed {len(records)} records for {endpoint_name}")
        return records

    except Exception as e:
        print(f"[ERROR] Failed to transform {endpoint_name}: {e}")
        return None
