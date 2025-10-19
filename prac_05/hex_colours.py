"""
CP1404/CP5632 Practical
Hexadecimal colour code searcher
"""

NAME_TO_CODE = {
    "absolute zero": "#0048ba",
    "amethyst": "#9966cc",
    "aqua": "#00ffff",
    "ash grey": "#b2beb5",
    "azure4": "#838b8b",
    "beaver": "#9f8170",
    "bitter lemon": "#cae00d",
    "bitter lime": "#bfff00",
    "black coffee": "#3b2f2f",
    "blue green": "#0d98ba"
}

for name, code in NAME_TO_CODE.items():
    print(f"{name:13} is {code}")

color_code = input("Enter colour name: ").lower()
while color_code != "":
    try:
        print(f"{color_code.title()} is {NAME_TO_CODE[color_code]}")
    except KeyError:
        print("Invalid colour name")
    color_code = input("Enter colour name: ").lower()
