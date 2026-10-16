
import sys


import sys


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python leap_year.py <year>")
        sys.exit(1)

    try:
        year = int(sys.argv[1])

        if year <= 0:
            raise ValueError

    except ValueError:
        print("Error: Enter a valid positive year.")
        sys.exit(1)

    if is_leap_year(year):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python leap_year.py <year>")
        sys.exit(1)

    try:
        year = int(sys.argv[1])

        if year <= 0:
            raise ValueError

    except ValueError:
        print("Error: Enter a valid positive year.")
        sys.exit(1)

    if is_leap_year(year):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")
