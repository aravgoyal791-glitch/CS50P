import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    valid = (".jpg", ".jpeg", ".png")

    if not sys.argv[1].lower().endswith(valid):
        print("Invalid input")
        sys.exit(1)

    if not sys.argv[2].lower().endswith(valid):
        print("Invalid output")
        sys.exit(1)

    if os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
        print("Input and output have different extensions")
        sys.exit(1)

    try:
        person = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")

        person = ImageOps.fit(person, shirt.size)
        person.paste(shirt, shirt)

        person.save(sys.argv[2])

    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()

