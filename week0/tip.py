mealprice=input("Enter the meal price: ")
mealprice= float(mealprice.replace("$",""))
tippercentage=input("Enter the tip percentage: ")
tippercentage= float(tippercentage.replace("%",""))
tipamount=mealprice*tippercentage/100
print(f"The tip amount is: ${tipamount:.2f}")
