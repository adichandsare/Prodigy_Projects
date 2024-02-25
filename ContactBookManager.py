import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter contact's name: ")
    phone = input("Enter contact's phone number: ")
    email = input("Enter contact's email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("List of Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    if not contacts:
        print("No contacts found.")
        return

    view_contacts(contacts)
    index = int(input("Enter the index of the contact you want to edit: ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        print("Editing contact:")
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        contact["name"] = input("Enter new name (leave empty to keep current): ") or contact["name"]
        contact["phone"] = input("Enter new phone number (leave empty to keep current): ") or contact["phone"]
        contact["email"] = input("Enter new email address (leave empty to keep current): ") or contact["email"]
        contacts[index] = contact
        print("Contact updated successfully!")
    else:
        print("Invalid index.")

def delete_contact(contacts):
    if not contacts:
        print("No contacts found.")
        return

    view_contacts(contacts)
    index = int(input("Enter the index of the contact you want to delete: ")) - 1
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully!")
    else:
        print("Invalid index.")

def main():
    contacts = load_contacts()
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Exiting program. Your contacts have been saved.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
