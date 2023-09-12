login_name = input("Create login name: ")

while len(login_name) < 8:
    print("Error...")
    login_name = input("Create login name: ")
print(f"login name: {login_name}")
