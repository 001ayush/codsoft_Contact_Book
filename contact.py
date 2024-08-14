

contacts = {}



def add_contact():
    name = input("Enter contact name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    if name in contacts:
        print("Contact already exists. ")
    else:
        contacts[name] = {
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        print("Contact added successfully.")




def view_contacts():
    if not contacts:
        print("Contact Not Available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)



def search_contact():
    search_term = input("Enter the name or phone number : ").strip()
    found = False
    
    for name, details in contacts.items():
        if search_term in name or search_term in details['phone_number']:
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)
            found = True
    
    if not found:
        print("No matching contacts found.")




def update_contact():
    name = input("Enter the name : ").strip()
    
    if name in contacts:

        phone_number = input(f"Enter new phone number (current: {contacts[name]['phone_number']}): ").strip()
        email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()
        address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()
        
        if phone_number:
            contacts[name]['phone_number'] = phone_number
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print("Contact updated successfully.")
    else:
        print("Contact not found.")




def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")




def main_menu():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
