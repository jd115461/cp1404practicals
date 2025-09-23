MINIMUM_CHARACTERS = 6


def main():
    password = get_password(MINIMUM_CHARACTERS)
    print_asterisks(password)


def get_password(MINIMUM_CHARACTERS):
    password = input(f"Enter password of at least {MINIMUM_CHARACTERS} characters: ")
    while len(password) < MINIMUM_CHARACTERS:
        print("Password too short")
        password = input(f"Enter password of at least {MINIMUM_CHARACTERS} characters: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
