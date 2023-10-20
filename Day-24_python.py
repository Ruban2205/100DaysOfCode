# Implement a basic address book with CRUD operations.
print("\nRuban Gino Singh - Day24 of #100DaysOfCode\n")

print("Program to implement a basic address book with CRUD Operations\n")

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def create_contact(self, name, phone, email):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact '{name}' added.")
        else:
            print(f"Contact '{name}' already exists. Use 'update' to modify.")

    def read_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name]['phone'] = phone
            self.contacts[name]['email'] = email
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' not found. Use 'create' to add a new contact.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")

    def list_contacts(self):
        print("Contacts:")
        for name, info in self.contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def main():
    address_book = AddressBook()

    while True:
        print("\nOptions:")
        print("1. Create contact")
        print("2. Read contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. List all contacts")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address_book.create_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name: ")
            address_book.read_contact(name)
        elif choice == '3':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address_book.update_contact(name, phone, email)
        elif choice == '4':
            name = input("Enter name: ")
            address_book.delete_contact(name)
        elif choice == '5':
            address_book.list_contacts()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

# --------------------------------------------------------- #