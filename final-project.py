def main():
    contacts = {
        "Contact1": {"Name": "Alice", "Phone": "8767789899", "Email": "alice@example.com"},
        "Contact2": {"Name": "Kevin", "Phone": "9099754322", "Email": "kevinkev@yahoo.com"},
        "Contact3": {"Name": "Lisa", "Phone": "7654332239", "Email": "lisacakes@aol.com"},
    }
               
    print("Welcome to the Contact Management System Menu!")
    
    def add_contact(name, phone, email, contact_list):
        if name not in contact_list:
            contact_list[name] = {"Name": name, "Phone": phone, "Email": email}
            print(f"Contact {name} has been added")

    def update_contact(contact_list, name, phone, email):
        if name in contact_list:
            contact_list[name]["Phone"] = phone
            contact_list[name]["Email"] = email
            print(f"Contact {name} has been updated")

    def delete_contact(contact_list, name):
        if name in contact_list:
            del contact_list[name]
            print(f"Contact {name} has been deleted")
        else:
            print(f"Contact {name} not found")

    def search_contact(contact_list, name):
        if name in contact_list:
            print(f"Contact details for {name}: {contact_list[name]}")
        else:
            print(f"Contact {name} not found")

    def display_contact(contact_list):
        print("\nContacts:")
        for name, details in contact_list.items():
            print(f"Name: {details['Name']}, Email: {details['Email']}, Phone: {details['Phone']}")

    def export_contact(contacts):
        filename = input("Enter the filename to export contacts (e.g., contacts.txt): ")
        try:
            with open(filename, "w") as file:
                for name, details in contacts.items():
                    file.write(f"Name: {details['Name']}, Email: {details['Email']}, Phone: {details['Phone']}\n")
                    print("Contacts exported successfully.")
        except Exception as e:
            print(f"Error exporting contacts: {e}")

    
    def import_contact(contacts):
        filename = input("Enter the filename to import contacts from (e.g., contacts.txt): ")
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, phone, email = line.strip().split(",")
                    add_contact(name, phone, email, contacts)
                    print("Contacts imported successfully.")
        except Exception as e:
            print(f"Error importing contacts: {e}")

    while True:
        print("\n1. Add New Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Export Contacts")
        print("7. Import Contacts")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email, contacts)
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            update_contact(contacts, name, phone, email)
        elif choice == "3":
            name = input("Enter name: ")
            delete_contact(contacts, name)
        elif choice == "4":
            name = input("Enter name: ")
            search_contact(contacts, name)
        elif choice == "5":
            display_contact(contacts)
        elif choice == "6":
            export_contact()
        elif choice == "7":
            import_contact()
        elif choice == "8":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
