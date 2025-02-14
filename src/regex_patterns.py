import re

def extract_and_validate_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z]{2,}\b'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_urls(text):
    pattern = r'https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(/\S*)?'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_and_validate_credit_card_numbers(text):
    pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    return re.findall(pattern, text)
