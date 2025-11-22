"""
CP1404/CP5632 Practical
SilverServiceTaxi test program
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)  # fanciness 2
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare for 18 km: ${fare:.2f}")
    assert round(fare, 2) == 48.78, f"Expected 48.78, got {fare:.2f}"


if __name__ == "__main__":
    main()
