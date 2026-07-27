def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length must be between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # First two characters must be letters
    if not s[:2].isalpha():
        return False

    number_started = False

    for char in s:
        if char.isdigit():
            if not number_started:
                number_started = True
                # First number cannot be 0
                if char == "0":
                    return False
        else:
            # No letters after numbers begin
            if number_started:
                return False
            # No punctuation or spaces
            if not char.isalpha():
                return False

    return True


if __name__ == "__main__":
    main()