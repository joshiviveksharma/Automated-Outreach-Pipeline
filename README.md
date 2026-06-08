# Automated Outreach Pipeline

## Overview

This project automates the process of discovering business contacts and sending outreach emails.

The pipeline takes a company domain as input, finds relevant contacts, retrieves verified email addresses, and sends emails using Brevo.

---

## Features

* Company Discovery using Prospeo API
* Contact Discovery using Prospeo Search Person API
* Verified Email Enrichment using Prospeo Enrich Person API
* Automated Email Sending using Brevo API
* Modular Service-Based Architecture
* Command Line Interface

---

## Project Structure

```text
outreach-pipeline/
│
├── main.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── ocean.py
│   ├── prospeo.py
│   ├── eazyreach.py
│   └── brevo.py
│
├── logs/
├── output/
│
├── test_company.py
├── test_prospeo.py
└── test_brevo.py
```

---

## Architecture

```text
Input Company Domain
        ↓
Prospeo Search Company API
        ↓
Prospeo Search Person API
        ↓
Prospeo Enrich Person API
        ↓
Verified Email Extraction
        ↓
Brevo Email API
        ↓
Email Delivery
```

---

## Technologies Used

* Python 3
* Requests
* Python Dotenv
* Prospeo API
* Brevo API

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd outreach-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
PROSPEO_API_KEY=your_prospeo_api_key
BREVO_API_KEY=your_brevo_api_key
```

---

## Running the Project

```bash
python main.py
```

Example:

```text
Enter company domain: microsoft.com
```

Sample Output:

```text
🚀 Automated Outreach Pipeline Started

Company Search: 200

===== SUMMARY =====
Companies Found: 1
Contacts Found: 1
Emails Found: 1

mayas@microsoft.com

[Brevo] Sending emails...
mayas@microsoft.com -> 201
```

---

## APIs Used

### Prospeo

* Search Company
* Search Person
* Enrich Person

### Brevo

* Transactional Email API

---

## Assignment Notes

Ocean.io onboarding was unavailable during implementation. As permitted in the assignment FAQ, Prospeo was used as an alternative service for company discovery, contact discovery, and email enrichment.

The final pipeline successfully demonstrates:

* Real company lookup
* Real contact discovery
* Real email enrichment
* Automated email delivery

---

## Author

Vivek Sharma
