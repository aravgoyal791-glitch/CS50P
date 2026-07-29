def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    # Rule 1: Length
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Rule 2: Only letters and numbers
    if not plate.isalnum():
        return False

    # Rule 3: First two characters must be letters
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    number_started = False

    for letter in plate:

        # Rule 4: Once numbers start, no letters are allowed
        if letter.isdigit():

            if not number_started:
                number_started = True

                # Rule 5: First number cannot be 0
                if letter == "0":
                    return False

        elif number_started and letter.isalpha():
            return False

    return True


main()