def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    numerator, denominator = fraction.split("/")

    numerator = int(numerator)
    denominator = int(denominator)

    if denominator == 0:
        raise ZeroDivisionError

    if numerator < 0 or denominator < 0:
        raise ValueError

    if numerator > denominator:
        raise ValueError

    return round((numerator / denominator) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()