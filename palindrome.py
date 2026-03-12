import re

# Function to clean the input and ignore spaces and punctuation
def clean_string(input_string):
    return re.sub('[^A-Za-z0-9]', '', input_string).lower()

# Function to check if a string is a palindrome
def is_palindrome(input_string):
    cleaned_string = clean_string(input_string)
    return cleaned_string == cleaned_string[::-1]

# Function to check if a number is a palindrome
def is_palindrome_number(num):
    return is_palindrome(str(num))

# Example functions to check palindromes
if __name__ == '__main__':
    test_strings = ["A man, a plan, a canal: Panama", "racecar", "12321", "hello"]
    for s in test_strings:
        print(f'"{s}" is a palindrome: {is_palindrome(s)}')
    
    test_numbers = [12321, 12345]
    for n in test_numbers:
        print(f'{n} is a palindrome: {is_palindrome_number(n)}')