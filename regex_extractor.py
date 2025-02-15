import re

def extract_emails(text):
    """
    Extracts email addresses from given text or text strings using regular expressions.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)

    return list(set(emails))  # Remove duplicates

def process_emails():
    """
    prompts the user for input and extracts email addresses using regular expressions
    """
    try:
        text = input("Please enter the text for email extraction:\n")
        
        if not text.strip():
            print("No text provided. Exiting.")
            return
        
        extracted_emails = extract_emails(text)
        
        if extracted_emails:
            print("\nExtracted Emails:")
            for email in extracted_emails:
                print(f"- {email}")
        else:
            print("No valid email addresses found.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    process_emails()
    
    
    
    # extracting urls
    def extract_urls(text):
        return list(set(urls))  # Remove duplicates
        
    """
    Extracts URLs from the given text using regular expressions.
    """
    url_pattern = r'https?://(?:www\.)?[-\w]+(?:\.\w[-\w]*)+[\w\-._~:/?#[\]@!$&\'()*+,;=]*'
    urls = re.findall(url_pattern, "text")
    


# importing urls 

def extract_urls(text):
    """
    Extracts URLs from the given text using a regular expression.
    """
    url_pattern = r'https?://(?:www\.)?[-\w]+(?:\.\w[-\w]*)+[\w\-._~:/?#[\]@!$&\'()*+,;=]*'
    urls = re.findall(url_pattern, text)

    return list(set(urls))  # Remove duplicates

def process_urls():
    """
    Prompts the user for input and extracts URLs from the provided text.
    """
    try:
        text = input("Please enter the text for URL extraction:\n")
        
        if not text.strip():
            print("No text provided. Exiting.")
            return
        
        extracted_urls = extract_urls(text)
        
        if extracted_urls:
            print("\nExtracted URLs:")
            for url in extracted_urls:
                print(f"- {url}")
        else:
            print("No valid URLs found.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    process_urls()
    
    
# extracting phone numbers 
text = """
Call me at (123) 456-7890 or 123-456-7890.
You can also reach me at 123.456.7890 or 123 456 7890.
"""

# Regular expression to match different phone number formats
phone_regex = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

# Loop to allow user to input the phone number or exit
while True:
    # Ask the user to input a phone number or 'exit' to quit
    user_input = input("Enter the phone number you're looking for (or type 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    
    # Search for the phone number in the text
    phone_numbers = re.findall(phone_regex, text)
    
    # Check if the input matches any extracted phone numbers
    if user_input in phone_numbers:
        print(f"Phone number {user_input} found in the text!")
    else:
        print(f"Phone number {user_input} not found in the text.")
        
        
# extracting credit cards
# Regular expression pattern for matching credit card numbers (space-separated or hyphen-separated)
credit_card_pattern = r'\b(?:\d{4}[-\s]){3}\d{4}\b|\b\d{4}[-\s]\d{6}[-\s]\d{5}\b|\b\d{4}[-\s]{3,6}\d{4}\b'

# Luhn's algorithm to check if a credit card number is valid
def luhn_algorithm(card_number):
    
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Reverse the card number and apply Luhn's algorithm
    total = 0
    reverse_digits = card_number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Double every second digit
        if i % 2 == 1:
            n *= 2
            
            if n > 9:
                n -= 9
        total += n

    # Valid if the total modulo 10 is 0
    return total % 10 == 0

# Function to check if the card has a valid prefix (Visa, MasterCard, etc.)
def is_valid_card_prefix(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check known prefixes
    valid_prefixes = {
        "Visa": r'^4\d{12}(?:\d{3})?$',                             
        "MasterCard": r'^5[1-5]\d{14}$',                           
        "American Express": r'^3[47]\d{13}$',                      
        "Discover": r'^6(?:011|5\d{2})\d{12}$',                    
        "JCB": r'^(?:2131|1800|35\d{3})\d{11}$',                   
        "Diners Club": r'^3(?:0[0-5]|[68]\d)\d{11}$',              
        "Maestro": r'^(?:5[0678]\d{2}|6304|6390|67\d{2})\d{8,15}$' 
    }

    # Validate the card number against the known prefixes
    for card_type, prefix_pattern in valid_prefixes.items():
        if re.match(prefix_pattern, card_number):
            return True, card_type
    return False, None

# Function to find and validate credit card numbers in a given string
def find_and_validate_credit_card_numbers(text):
    potential_cards = re.findall(credit_card_pattern, text)
    valid_cards = []
    
    for card in potential_cards:
        normalized_card = card.replace(" ", "").replace("-", "")
        
        if luhn_algorithm(normalized_card):
            is_valid, card_type = is_valid_card_prefix(normalized_card)
            if is_valid:
                valid_cards.append((card, card_type))
    
    return valid_cards

# Main function to take input from the terminal
if __name__ == "__main__":
    while True:
        # Take input string
        sample_text = input("Enter the text containing credit card numbers (or type 'exit' to quit): ")
        
        # Exit condition
        if sample_text.lower() == 'exit':
            break
        
        # Find and print all valid credit card numbers
        valid_credit_card_numbers = find_and_validate_credit_card_numbers(sample_text)
        
        if valid_credit_card_numbers:
            for card, card_type in valid_credit_card_numbers:
                print(f"Valid {card_type} credit card found: {card}")
        else:
            print("No valid credit card numbers found.")
            
# Time in 12-hour or 24-hour format
time_24hr_pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d$'  
time_12hr_pattern = r'^(?:0?[1-9]|1[0-2]):[0-5]\d\s?[AaPp][Mm]$'  

# Additional logic to handle edge cases in the 12-hour format
def is_valid_12hr_format(time_str):
    match = re.fullmatch(time_12hr_pattern, time_str)
    if match:
        # Split time into parts
        time, meridiem = time_str[:-2].strip(), time_str[-2:].upper().strip()
        hour, minute = map(int, time.split(':'))

        # Ensure minutes are in a valid range (00-59)
        if not (0 <= minute < 60):
            return False

        # Special handling for 12 AM and 12 PM
        if meridiem == 'AM' and hour == 12:
            return True  
        elif meridiem == 'PM' and hour == 12:
            return True  

        # Validate hour (01-11 for AM/PM)
        if 1 <= hour <= 11:
            return True
    return False

# Function to identify time format with strict validation
def identify_time_format(time_str):
    if re.fullmatch(time_24hr_pattern, time_str):
        return "24-hour time format"
    elif is_valid_12hr_format(time_str):
        return "12-hour time format"
    else:
        return "Invalid time format"

# Main loop to take input from the terminal
while True:
    # Prompt the user for input
    time_str = input("Enter a time-format (or type 'exit' to quit): ").strip()
    
    # Exit condition
    if time_str.lower() == 'exit':
        break
    
    # Identify the time format
    result = identify_time_format(time_str)
    
    # Print the result
    print(f"'{time_str}' is in {result}")
    
    
    # extracting html tags
{ 'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b', 'base', 'bdi',
    'bdo', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'cite', 'code',
    'col', 'colgroup', 'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog',
    'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer',
    'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'hr',
    'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li',
    'link', 'main', 'map', 'mark', 'meta', 'meter', 'nav', 'noscript', 'object',
    'ol', 'optgroup', 'option', 'output', 'p', 'picture', 'pre', 'progress', 'q',
    'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source',
    'span', 'strong', 'style', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'template',
    'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'u', 'ul', 'var', 'video',
    'wbr'
}

def is_valid_html_tag(tag):
   
    tag_name_pattern = re.compile(r'^<(/?\s*([\w-]+))[^>]*>$')
    match = tag_name_pattern.match(tag)
    if match:
        tag_name = match.group(2).lower()  
        return tag_name in "is_valid_html_tags"
    else:
        return False

def main():
   
    html_string = input("Please Enter your HTML string:\n")

    
    html_tag_pattern = r'<[^>]+>'
    
   
    matches = re.findall(html_tag_pattern, html_string)
    
    if matches:
        print(" You got it!...valid html tag:")
        for match in matches:
            print(match)
    else:
        print("Oh No!... invalid html tag.")
        
while True:
    
    html_str = input("Enter an html tag (or type 'exit' to quit): ").strip()
    
    
    if html_str.lower() == 'exit':
        break

if __name__ == "__main__":
    main()
    
    
# extracting hashtags
def main():
  
    text_input = input(" please Enter your text string:\n")

   
    hashtag_pattern = r'#\w+'
    
    
    matches = re.findall(hashtag_pattern, text_input)
    
    
    if matches:
        print("Hashtags extracted:")
        for match in matches:
            print(match)
    else:
        print("Sorry! No hashtags found.")

if __name__ == "__main__":
    main()

# extracting currency amounts
sample_text = """
Here are some currency amounts:
$19.99
$1,234.56
$100
$12,345
$9.99
"""

# Regular expression to match currency amounts
currency_regex = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'

# Find all currency amounts in the sample text
currency_amounts = re.findall(currency_regex, sample_text)

# Print extracted currency amounts
for amount in currency_amounts:
    print(amount)
