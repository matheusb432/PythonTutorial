name = input("What is your name? ")
name_length = len(name)
if name_length < 3:
    print("Name too short")
elif name_length > 50:
    print("Name too long")
else:
    print("Good name")