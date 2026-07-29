import sys
import csv


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    try:
        with open(sys.argv[1], newline="") as infile:
            reader = csv.DictReader(infile)

            with open(sys.argv[2], "w", newline="") as outfile:
                writer = csv.DictWriter(
                    outfile,
                    fieldnames=["first", "last", "house"]
                )

                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(",")
                    first = first.strip()

                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()