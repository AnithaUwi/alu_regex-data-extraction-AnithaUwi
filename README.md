 ALU Regex Data Extraction
Anitha Uwimpuhwe: a.uwimpuhwe@alustudent.com


## Overview
This project is designed to extract and validate specific types of data from text using regular expressions. The data types include email addresses, URLs, phone numbers, and credit card numbers.

## Requirements
- Python 3.6+
- The `re` module (built into Python's standard library)

## Installation
Clone the repository:

```sh
git clone https://github.com/AnithaUwi/alu_regex-data-extraction-AnithaUwi.git
```

Navigate to the project directory:

```sh
cd alu_regex-data-extraction-Elvin100s
```

No external dependencies are required. All necessary modules are part of Python's standard library.

## Usage
### Extract and Validate Emails
```python
from src.regex_patterns import extract_and_validate_emails
from src.validators import validate_email

text = "Contact us at support@example.com or admin@company.co.uk"
emails = extract_and_validate_emails(text)
for email in emails:
    print(f"Email: {email}, Valid: {validate_email(email)}")
```

### Extract and Validate URLs
```python
from src.regex_patterns import extract_and_validate_urls
from src.validators import validate_url

text = "Visit https://www.example.com or https://subdomain.example.org/page"
urls = extract_and_validate_urls(text)
for url in urls:
    print(f"URL: {url}, Valid: {validate_url(url)}")
```

### Extract and Validate Phone Numbers
```python
from src.regex_patterns import extract_and_validate_phone_numbers
from src.validators import validate_phone_number

text = "Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890 or 123 456 7890"
phone_numbers = extract_and_validate_phone_numbers(text)
for phone_number in phone_numbers:
    print(f"Phone Number: {phone_number}, Valid: {validate_phone_number(phone_number)}")
```

### Extract and Validate Credit Card Numbers
```python
from src.regex_patterns import extract_and_validate_credit_card_numbers
from src.validators import validate_credit_card_number

text = "Credit card numbers: 1234 5678 9012 3456 or 1234-5678-9012-3456"
credit_card_numbers = extract_and_validate_credit_card_numbers(text)
for credit_card_number in credit_card_numbers:
    print(f"Credit Card Number: {credit_card_number}, Valid: {validate_credit_card_number(credit_card_number)}")
```

## Test Cases
To run the test cases, navigate to the project directory and execute:

```sh
python -m unittest tests.py
```

## Project Structure
```
alu_regex-data-extraction-yourusername/
├── README.md
├── requirements.txt
├── src/
│   ├── regex_patterns.py
│   ├── validators.py
│   └── __init__.py
└── tests.py
```

## Contributors
AnithaUwimpuhwe : a.uwimpuhwe@alustudent.com

## Additional Notes
- Ensure your regular expressions handle various formats and edge cases.
- Test your functions thoroughly to ensure they work as expected.

## requirements.txt
```
# This project does not require any external dependencies.
# All necessary modules (e.g., `re`) are part of Python's standard library.
```

