camel=input("camelcase:")
print("snake_case: ", end="")
for letter in camel:
    if letter.isupper():
        print("_" + letter.lower() , end="")
    else:
        print(letter, end="")
print()
