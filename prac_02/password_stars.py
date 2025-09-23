password = input("Enter Password of at least 6 characters: ")
while len(password) < 6:
    print("Error, please try again!")
    password = input("Enter Password of at least 6 characters: ")
print("*" * len(password))

