import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BREVO_API_KEY")

def send_emails(emails):

    print("\n[Brevo] Sending emails...")

    for email in emails:

        payload = {
            "sender": {
                "name": "VivekSDE",
                "email": "joshiviveksharma@gmail.com"
            },
            "to": [
                {
                    "email": email
                }
            ],
            "subject": "Automated Outreach Test",
            "htmlContent": "<p>Hello from VivekSDE Pipeline.</p>"
        }

        headers = {
            "accept": "application/json",
            "api-key": API_KEY,
            "content-type": "application/json"
        }

        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            json=payload,
            headers=headers
        )

        print(f"{email} -> {response.status_code}")