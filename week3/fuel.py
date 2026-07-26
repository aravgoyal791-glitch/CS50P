while True:
    try:
        fraction = input("Fraction: ")

        numerator, denominator = fraction.split("/")

        numerator = int(numerator)
        denominator = int(denominator)

        if numerator < 0 or denominator <= 0 or numerator > denominator:
            continue

        percentage = round((numerator / denominator) * 100)

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")

        break

    except (ValueError, ZeroDivisionError):
        pass