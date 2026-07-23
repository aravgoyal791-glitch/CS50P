filename=input("enter the name of the file:").lower()
if filename.endswith(".jpg"):
    print("image/jpeg")
elif filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")