import sys
from datetime import date
import inflect

def main():
    dob = input("Date of Birth: ")
    print(minutes(dob))

def minutes(dob):
    try:
        year, month, day = dob.split("-")
        birth = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    total_days = (today - birth).days
    total_minutes = round(total_days * 24 * 60)

    p = inflect.engine()
    words = p.number_to_words(total_minutes, andword="")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()
