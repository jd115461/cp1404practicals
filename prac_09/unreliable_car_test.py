"""
CP1404/CP5632 Practical
Test program for UnreliableCar
"""

from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar behaviour over many drive attempts."""
    normal_car = UnreliableCar("normal", 100, 90)
    unreliable_car = UnreliableCar("unreliable", 100, 10)

    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{normal_car.name:12} drove {normal_car.drive(i):2}km")
        print(f"{unreliable_car.name:12} drove {unreliable_car.drive(i):2}km")

    print(normal_car)
    print(unreliable_car)

main()
