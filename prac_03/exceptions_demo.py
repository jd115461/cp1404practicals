"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# When the user price can't be converted to an int
2. When will a ZeroDivisionError occur?
# When the denominator value is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Check if the denominator value is 0 before handling the division value itself
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be 0!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
