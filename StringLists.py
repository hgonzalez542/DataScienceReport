import string

def clean_string(s):
    return ''.join(c.lower() for c in s if c.isalnum())

def is_palindrome(s):
    cleaned = clean_string(s)
    return cleaned == cleaned[::-1]

while True:
    s = input("\nEnter a string (or type 'exit' to quit): ")
    if s.lower() == 'exit':
        print("Goodbye!")
        break
    if is_palindrome(s):
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")
