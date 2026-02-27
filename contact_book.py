# contact_book.py

contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added.")

def view_contacts():
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("Search by name or phone: ")
    for contact in contacts:
        if query in contact["name"] or query in contact["phone"]:
            print(contact)

def update_contact():
    view_contacts()
    index = int(input("Enter contact number to update: ")) - 1
    contacts[index]["phone"] = input("New phone: ")
    print("Updated.")

def delete_contact():
    view_contacts()
    index = int(input("Enter contact number to delete: ")) - 1
    contacts.pop(index)
    print("Deleted.")

def main():
    while True:
        print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
