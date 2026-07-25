text = input("Input: ")

print("Output: ", end="")

for c in text:
    if c.lower() not in "aeiou":
        print(c, end="")

print()