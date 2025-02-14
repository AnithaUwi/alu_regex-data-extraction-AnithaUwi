import unittest
from src.regex_patterns import extract_and_validate_emails, extract_and_validate_urls, extract_and_validate_phone_numbers, extract_and_validate_credit_card_numbers
from src.validators import validate_email, validate_url, validate_phone_number, validate_credit_card_number

class TestRegexPatterns(unittest.TestCase):
    def test_extract_and_validate_emails(self):
        text = "Contact us at support@example.com or admin@company.co.uk or invalid email or user@com or user@.com"
        expected = ["support@example.com", "admin@company.co.uk"]
        self.assertEqual(extract_and_validate_emails(text), expected)

    def test_extract_and_validate_urls(self):
        text = "Visit https://www.example.com or https://subdomain.example.org/page or invalid-url or www.example.com or http://example"
        expected = ["https://www.example.com", "https://subdomain.example.org/page"]
        self.assertEqual(extract_and_validate_urls(text), expected)

    def test_extract_and_validate_phone_numbers(self):
        text = "Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890 or 123 456 7890 or 1234567890 or 123-456-789 or 123.456.789 or 123 456 789 or 123456789"
        expected = ["(123) 456-7890", "123-456-7890", "123.456.7890", "123 456 7890"]
        self.assertEqual(extract_and_validate_phone_numbers(text), expected)

    def test_extract_and_validate_credit_card_numbers(self):
        text = "Credit card numbers: 1234 5678 9012 3456 or 1234-5678-9012-3456 or 1234567890123456 or 1234 5678 9012 345 or 123456789012345 or 1234-5678-9012-345 or 1234 5678 9012 34567"
        expected = ["1234 5678 9012 3456", "1234-5678-9012-3456"]
        self.assertEqual(extract_and_validate_credit_card_numbers(text), expected)

    def test_validate_email(self):
        self.assertTrue(validate_email("support@example.com"))
        self.assertTrue(validate_email("firstname.lastname@company.co.uk"))
        self.assertFalse(validate_email("invalid-email"))
        self.assertFalse(validate_email("user@com"))
        self.assertFalse(validate_email("user@.com"))

    def test_validate_url(self):
        self.assertTrue(validate_url("https://www.example.com"))
        self.assertTrue(validate_url("http://subdomain.example.org/page"))
        self.assertFalse(validate_url("invalid-url"))
        self.assertFalse(validate_url("www.example.com"))
        self.assertFalse(validate_url("http://example"))

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("(123) 456-7890"))
        self.assertTrue(validate_phone_number("123-456-7890"))
        self.assertTrue(validate_phone_number("123.456.7890"))
        self.assertTrue(validate_phone_number("123 456 7890"))
        self.assertFalse(validate_phone_number("1234567890"))
        self.assertFalse(validate_phone_number("123-456-789"))
        self.assertFalse(validate_phone_number("123.456.789"))
        self.assertFalse(validate_phone_number("123 456 789"))
        self.assertFalse(validate_phone_number("123456789"))

    def test_validate_credit_card_number(self):
        self.assertTrue(validate_credit_card_number("1234 5678 9012 3456"))
        self.assertTrue(validate_credit_card_number("1234-5678-9012-3456"))
        self.assertFalse(validate_credit_card_number("1234567890123456"))
        self.assertFalse(validate_credit_card_number("1234 5678 9012 345"))
        self.assertFalse(validate_credit_card_number("123456789012345"))
        self.assertFalse(validate_credit_card_number("1234-5678-9012-345"))
        self.assertFalse(validate_credit_card_number("1234 5678 9012 34567"))

if __name__ == '__main__':
    unittest.main()
