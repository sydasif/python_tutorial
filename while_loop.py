password = "Passw@rd"
count = 0

while count <= 3:
    user = input("Enter Password: ")
    count += 1
    if user != password:
        print("You are not allowed.")
    if user == password:
        print("You are allowed.")
        break
