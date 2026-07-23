x=int(input("enter a number:"))
y=input("enter a operator:")
z=int(input("enter another number:"))
if y == "+":
    print(f"{x+z:.1f}")
elif y== "-":
    print(f"{x-z:.1f}")
elif y== "*":
    print(f"{x*z:.1f}")
elif y== "/":
    print(f"{x/z:.1f}")
else:
    print("invalid operator")