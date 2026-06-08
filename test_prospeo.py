from services.prospeo import get_contacts

companies = [
    {
        "name": "Microsoft",
        "domain": "microsoft.com"
    }
]

print(get_contacts(companies))