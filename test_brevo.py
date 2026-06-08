import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("BREVO_API_KEY")

headers = {
    "accept": "application/json",
    "api-key": api_key,
    "content-type": "application/json"
}

payload = {
    "sender": {
        "name": "VivekSDE",
        "email": "joshiviveksharma@gmail.com"
    },
    "to": [
        {
            "email": "joshiviveksharma@gmail.com"
        }
    ],
    "subject": "Brevo API Test",
    "htmlContent": "<h1>Brevo is working!</h1>"
}

response = requests.post(
    "https://api.brevo.com/v3/smtp/email",
    json=payload,
    headers=headers
)

print(response.status_code)
print(response.text)