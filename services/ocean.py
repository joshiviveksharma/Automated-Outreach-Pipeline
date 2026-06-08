import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PROSPEO_API_KEY")

def get_similar_companies(domain):

    payload = {
        "page": 1,
        "filters": {
            "company": {
                "websites": {
                    "include": [domain]
                }
            }
        }
    }

    response = requests.post(
        "https://api.prospeo.io/search-company",
        headers={
            "X-KEY": API_KEY,
            "Content-Type": "application/json"
        },
        json=payload
    )

    print("Company Search:", response.status_code)

    data = response.json()

    companies = []

    if data.get("results"):

        for item in data["results"][:3]:

            company = item["company"]

            companies.append({
                "name": company.get("name"),
                "domain": company.get("domain")
            })

    return companies