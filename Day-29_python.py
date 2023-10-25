# Implement a basic database for storing user Information
print("\nRuban Gino Singh - Day 29 of the #100DaysOfCode\n")

print("Python program to implement a basic database for storing user Information\n")

user_db = {}

def add_user(username, email, age): 
    user_db[username] = {'email': email, 'age': age}
    print(f"User {username} added to the database.")

def get_user(username): 
    if username in user_db: 
        user_info = user_db[username]
        print(f"User: {username} \n Email: {user_info['email']} \n Age: {user_info['age']}")
    else: 
        print(f"User {username} not found in the database.")

def update_user(username, email, age): 
    if username in user_db: 
        user_db[username]['email'] = email
        user_db[username]['age'] = age
        print(f"User {username} information updated.")
    else: 
        print(f"User {username} not found in the database. Cannot update.")

def delete_user(username):
    if username in user_db:
        del user_db[username]
        print(f"User {username} deleted from the database.")
    else:
        print(f"User {username} not found in the database. Cannot delete.")

while True:
    print("\nUser Database Options:")
    print("1. Add User")
    print("2. Get User Information")
    print("3. Update User Information")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        username = input("Enter username: ")
        email = input("Enter email: ")
        age = input("Enter age: ")
        add_user(username, email, age)
    elif choice == '2':
        username = input("Enter username to retrieve: ")
        get_user(username)
    elif choice == '3':
        username = input("Enter username to update: ")
        email = input("Enter new email: ")
        age = input("Enter new age: ")
        update_user(username, email, age)
    elif choice == '4':
        username = input("Enter username to delete: ")
        delete_user(username)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

# --------------------------------------------------------- #