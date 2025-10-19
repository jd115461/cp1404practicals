"""
Emails
Estimate: 13 minutes 39 seconds 270 millisecond
Actual:  19 minutes 33 seconds 860 millisecond
"""

def main():
    """Create dictionary of emails to names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (y/n) ")
        if confirmation != "y" and confirmation != "":
            name = input("Name: ")
            email_to_name[email] = name
            email = input("Email: ")

        for email, name in email_to_name.items():
            print(f"{name} ({email})")

def get_name_from_email(email):
    """Extract name from email address"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()



