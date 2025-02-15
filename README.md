# alu_regex-data-extraction-Rachel-png-coder
Regular Expressions.  

This project is part of the Regex Onboarding Hackathon and is aimed at demonstrating the use of Regular Expressions (Regex) to extract specific data types. The project handles various formats including email addresses, URLs, phone numbers, credit card numbers, and more, all through the power of Regex.

**Overview**

In this project, I have implemented a series of Python scripts that extract important pieces of data from raw text. Whether it's web-scraped content or API responses, the scripts utilize regular expressions to efficiently find and extract the following data types:

Email Addresses
URLs
Phone Numbers
Credit Card Numbers
Time Formats (12-hour and 24-hour)
HTML Tags
Hashtags
Currency Amounts

**Project Breakdown**

Email Address Extraction The email extractor uses a regular expression designed to match standard email formats such as:

user@example.com

firstname.lastname@company.co.uk

URL Extraction

The URL extractor captures various types of URLs, including:

https://www.example.com

http://subdomain.example.org/page

Phone Number Extraction

Various phone number formats are supported, such as:

(123) 456-7890

123-456-7890

123.456.7890

Credit Card Number Extraction -The system can identify common credit card formats like:

1234 5678 9012 3456

1234-5678-9012-3456

Currency Amount Extraction

**How It Works**

The process starts by feeding a large string or webpage data into the program. The text is parsed, and each type of information (e.g., emails, phone numbers) is extracted using specialized regular expressions. The extracted data can then be stored, displayed, or processed further.
