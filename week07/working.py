import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s
    )
    if not match:
        raise ValueError("Invalid format")

    start_hour, start_minute, start_period = match.group(1), match.group(2), match.group(3)
    end_hour, end_minute, end_period = match.group(4), match.group(5), match.group(6)

    start = to_24hour(start_hour, start_minute, start_period)
    end = to_24hour(end_hour, end_minute, end_period)

    return f"{start} to {end}"


def to_24hour(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if hour < 1 or hour > 12 or minute > 59:
        raise ValueError("Invalid time")

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
