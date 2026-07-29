def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    result = ""
    for letter in word:
        if letter not in "AEIOUaeiou":
            result += letter
    return result


if __name__ == "__main__":
    main()