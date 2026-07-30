import re


def main():
    html = input("HTML: ")
    print(parse(html))


def parse(s):
    match = re.search(
        r"<iframe[^>]*src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)\"", s
    )
    if not match:
        return None
    return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()
