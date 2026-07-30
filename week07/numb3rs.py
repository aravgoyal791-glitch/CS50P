import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip)
    if not match:
        return False

    for part in match.groups():
        # Reject leading zeros (e.g. "01", "007"), except "0" itself
        if len(part) > 1 and part[0] == "0":
            return False
        if int(part) < 0 or int(part) > 255:
            return False

    return True


if __name__ == "__main__":
    main()
