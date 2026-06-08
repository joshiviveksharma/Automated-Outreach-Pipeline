import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PROSPEO_API_KEY")

def get_verified_emails(contacts):

    emails = []

    for contact in contacts:

        payload = {
            "only_verified_email": True,
            "data": {
                "person_id": contact["person_id"]
            }
        }

        response = requests.post(
            "https://api.prospeo.io/enrich-person",
            headers={
                "X-KEY": API_KEY,
                "Content-Type": "application/json"
            },
            json=payload
        )

        data = response.json()

        if not data.get("error"):
            email_data = data.get("person", {}).get("email")

            if email_data and email_data.get("email"):
                emails.append(email_data["email"])

    return emails