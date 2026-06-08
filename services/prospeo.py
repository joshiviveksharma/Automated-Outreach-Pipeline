import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PROSPEO_API_KEY")


def get_contacts(companies):
    contacts = []

    for company in companies:

        payload = {
            "page": 1,
            "filters": {
                "company": {
                    "names": {
                        "include": [company["name"]]
                    }
                }
            }
        }

        response = requests.post(
            "https://api.prospeo.io/search-person",
            headers={
                "X-KEY": API_KEY,
                "Content-Type": "application/json"
            },
            json=payload
        )

        print(company["name"], response.status_code)

        # Handle rate limit
        if response.status_code == 429:
            print("Rate limit hit. Waiting 15 seconds...")
            time.sleep(15)

            response = requests.post(
                "https://api.prospeo.io/search-person",
                headers={
                    "X-KEY": API_KEY,
                    "Content-Type": "application/json"
                },
                json=payload
            )

            print("Retry:", response.status_code)

        # Skip if still failing
        if response.status_code != 200:
            print("Error:", response.text)
            continue

        data = response.json()

        if data.get("results"):
            person = data["results"][0]["person"]

            contacts.append({
                "company": company["name"],
                "name": person.get("full_name"),
                "person_id": person.get("person_id")
            })

    return contacts