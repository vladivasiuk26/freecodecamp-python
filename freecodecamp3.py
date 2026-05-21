password = "1234"
username = "admin"

password_login = input("Please enter your password: ")
username_login = input("Please enter your username: ")

if password_login == password and username_login == username:
    print("Welcome, you are logged in!")
else:
    print("Access denied.")
