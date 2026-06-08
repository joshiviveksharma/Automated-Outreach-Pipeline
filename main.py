from services.ocean import get_similar_companies
from services.prospeo import get_contacts
from services.eazyreach import get_verified_emails
from services.brevo import send_emails

print("🚀 Automated Outreach Pipeline Started")

domain = input("Enter company domain: ")

companies = get_similar_companies(domain)
contacts = get_contacts(companies)
emails = get_verified_emails(contacts)

print("\n===== SUMMARY =====")
print(f"Companies Found: {len(companies)}")
print(f"Contacts Found: {len(contacts)}")
print(f"Emails Found: {len(emails)}")

for email in emails:
    print(email)

confirm = input("\nProceed with email sending? (y/n): ")

if confirm.lower() == "y":
    send_emails(emails)
else:
    print("Email sending cancelled.")