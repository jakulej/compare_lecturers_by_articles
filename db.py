import json

def extract_data(file_path, author_id):
    extracted_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            json_data = json.loads(line.strip())
            if author_id not in json_data.get("author_ids", ""):
                continue
        data = {
            "pii": json_data.get("pii"),
            "title": json_data.get("title"),
            "subtype": json_data.get("subtype"),
            "author_count": json_data.get("author_count"),
            "author_ids": json_data.get("author_ids"),
            "coverDate": json_data.get("coverDate"),
            "publicationName": json_data.get("publicationName"),
            "description": json_data.get("description"),
            "authkeywords": json_data.get("authkeywords"),
            "fund_sponsor": json_data.get("fund_sponsor"),
            "citedby_count": json_data.get("citedby_count"),
            "interests": json_data.get("author_ids"),  # Assuming interests map to author_ids
            "citedby": json_data.get("citedby_count"),  # Assuming citedby is reflected in citedby_count
        }
        extracted_data.append(data)
    return extracted_data

file_path='./database/articles_PWR.jsonl'

# Example call for processing
result = extract_data(file_path, author_id="6602252130")

# Print the results
print(json.dumps(result, indent=4))