import sys


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    try:
        count = 0
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                count += 1
        print(count)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()