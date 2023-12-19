import json

class ContactManager:
    def __init__(self):
        self.contacts = []

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=2)

    def add_contact(self, name, phone, email, address):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact["name"].lower() or query in contact["phone"]]
        if not results:
            print("No matching contacts found.")
        else:
            for result in results:
                print(f"{result['name']} - {result['phone']}")

    def update_contact(self, index, field, new_value):
        if 1 <= index <= len(self.contacts):
            self.contacts[index - 1][field] = new_value
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            self.save_contacts()
            print(f"Contact '{deleted_contact['name']}' deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_manager = ContactManager()
    contact_manager.load_contacts()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            query = input("Enter the name or phone number to search: ")
            contact_manager.search_contact(query)
        elif choice == '4':
            index = int(input("Enter the index of the contact to update: "))
            field = input("Enter the field to update (name, phone, email, address): ")
            new_value = input("Enter the new value: ")
            contact_manager.update_contact(index, field, new_value)
        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index)
        elif choice == '6':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
