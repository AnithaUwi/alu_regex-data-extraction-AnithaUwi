import re

def validate_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z]{2,}\b '
    return re.match(pattern, email, re.IGNORECASE) is not None

def validate_url(url):
    pattern = r'https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(/\S*)? '
    return re.match(pattern, url, re.IGNORECASE) is not None

def validate_phone_number(phone_number):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4} '
    return re.match(pattern, phone_number) is not None

def validate_credit_card_number(credit_card_number):
    pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b '
    return re.match(pattern, credit_card_number) is not None
