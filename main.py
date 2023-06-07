import os

# User Class
class User:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_user_type(self):
        return self.user_type


# User Authentication Functions
def add_new_user():
    # Only the admin can perform this task
    if current_user.get_user_type() == "admin":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_type = input("Enter user type (admin, inventory-checker, purchaser): ")
        new_user = User(username, password, user_type)

        # Append the new user data to the userdata.txt file
        with open("userdata.txt", "a") as file:
            file.write(f"{username}\t{password}\t{user_type}\n")

        print("New user added successfully!")
    else:
        print("Access denied. Only admin can add new users.")


def user_authentication():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("userdata.txt", "r") as file:
        for line in file:
            line = line.strip().split("\t")
            if line[0] == username and line[1] == password:
                return line[2]

    print("Incorrect password or username.")
    return None


# Inventory Item Class
class InventoryItem:
    def __init__(self, code, description, category, unit, price, quantity, minimum):
        self.code = code
        self.description = description
        self.category = category
        self.unit = unit
        self.price = price
        self.quantity = quantity
        self.minimum = minimum

    def get_code(self):
        return self.code

    def get_description(self):
        return self.description

    def get_category(self):
        return self.category

    def get_unit(self):
        return self.unit

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_minimum(self):
        return self.minimum


# Inventory Management Functions
def insert_new_item():
    # Prompt the user to enter the details of the new item
    code = input("Enter item code: ")
    description = input("Enter item description: ")
    category = input("Enter item category: ")
    unit = input("Enter item unit: ")
    price = input("Enter item price: ")
    quantity = input("Enter item quantity: ")
    minimum = input("Enter item minimum threshold: ")

    # Create an instance of the InventoryItem class
    new_item = InventoryItem(code, description, category, unit, price, quantity, minimum)

    # Append the new item data to the inventory.txt file
    with open("inventory.txt", "a") as file:
        file.write(f"{code}\t{description}\t{category}\t{unit}\t{price}\t{quantity}\t{minimum}\n")

    print("New item added successfully!")


def update_item():
    # Read the data from the inventory.txt file and store it in a master list
    inventory_data = read_inventory_data()

    # Prompt the user to enter the code of the item to be updated
    code = input("Enter the code of the item to update: ")

    # Find the item in the master list by code
    for item in inventory_data:
        if item.get_code() == code:
            # Prompt the user to select the detail to be updated
            print("Select the detail to be updated:")
            print("1. Code")
            print("2. Description")
            print("3. Category")
            print("4. Unit")
            print("5. Price")
            print("6. Minimum Threshold")
            choice = input("Enter your choice: ")

            if choice == "1":
                new_code = input("Enter the new code: ")
                item.code = new_code
            elif choice == "2":
                new_description = input("Enter the new description: ")
                item.description = new_description
            elif choice == "3":
                new_category = input("Enter the new category: ")
                item.category = new_category
            elif choice == "4":
                new_unit = input("Enter the new unit: ")
                item.unit = new_unit
            elif choice == "5":
                new_price = input("Enter the new price: ")
                item.price = new_price
            elif choice == "6":
                new_minimum = input("Enter the new minimum threshold: ")
                item.minimum = new_minimum
            else:
                print("Invalid choice.")

            # Rewrite the updated master list to the inventory.txt file
            write_inventory_data(inventory_data)

            print("Item updated successfully!")
            return

    print("Item not found.")


def delete_item():
    # Read the data from the inventory.txt file and store it in a master list
    inventory_data = read_inventory_data()

    # Prompt the user to enter the code of the item to be deleted
    code = input("Enter the code of the item to delete: ")

    # Find the item in the master list by code
    for item in inventory_data:
        if item.get_code() == code:
            inventory_data.remove(item)

            # Rewrite the updated master list to the inventory.txt file
            write_inventory_data(inventory_data)

            print("Item deleted successfully!")
            return

    print("Item not found.")


def stock_taking():
    # Read the data from the inventory.txt file and store it in a master list
    inventory_data = read_inventory_data()

    # Prompt the user to enter the code of the item for stock taking
    code = input("Enter the code of the item for stock taking: ")

    # Find the item in the master list by code
    for item in inventory_data:
        if item.get_code() == code:
            # Prompt the user to confirm or change the quantity
            print(f"Current quantity: {item.get_quantity()}")
            new_quantity = input("Enter the new quantity: ")
            item.quantity = new_quantity

            # Rewrite the updated master list to the inventory.txt file
            write_inventory_data(inventory_data)

            print("Stock taking completed!")
            return

    print("Item not found.")


def view_replenish_list():
    # Read the data from the inventory.txt file and store it in a master list
    inventory_data = read_inventory_data()

    # Print the items with a quantity lower than the minimum threshold
    print("Replenish List:")
    for item in inventory_data:
        if item.get_quantity() < item.get_minimum():
            print(f"Code: {item.get_code()}")
            print(f"Description: {item.get_description()}")
            print(f"Category: {item.get_category()}")
            print(f"Unit: {item.get_unit()}")
            print(f"Price: {item.get_price()}")
            print(f"Quantity: {item.get_quantity()}")
            print(f"Minimum Threshold: {item.get_minimum()}")
            print("--------------------")

    print("End of Replenish List.")


def stock_replenishment():
    # Read the data from the inventory.txt file and store it in a master list
    inventory_data = read_inventory_data()

    # Prompt the user to enter the code of the item for stock replenishment
    code = input("Enter the code of the item for stock replenishment: ")

    # Find the item in the master list by code
    for item in inventory_data:
        if item.get_code() == code:
            # Prompt the user to add the quantity of the newly purchased items
            print(f"Current quantity: {item.get_quantity()}")
            replenish_quantity = input("Enter the quantity of the newly purchased items: ")
            item.quantity = str(int(item.get_quantity()) + int(replenish_quantity))

            # Rewrite the updated master list to the inventory.txt file
            write_inventory_data(inventory_data)

            print("Stock replenishment completed!")
            return

    print("Item not found.")


def search_items_by_description():
    # Read the data from the inventory.txt file and store it in a master list
    inventory_data = read_inventory_data()

    # Prompt the user to enter the description to search for
    search_description = input("Enter the item description to search for: ")

    # Search for items with matching description
    matching_items = []
    for item in inventory_data:
        if search_description.lower() in item.get_description().lower():
            matching_items.append(item)

    # Print the matching items
    print("Matching Items:")
    if len(matching_items) > 0:
        for item in matching_items:
            print(f"Code: {item.get_code()}")
            print(f"Description: {item.get_description()}")
            print(f"Category: {item.get_category()}")
            print(f"Unit: {item.get_unit()}")
            print(f"Price: {item.get_price()}")
            print(f"Quantity: {item.get_quantity()}")
            print(f"Minimum Threshold: {item.get_minimum()}")
            print("--------------------")
    else:
        print("No matching items found.")


def search_items_by_code_range():
    # Read the data from the inventory.txt file and store it in a master list
    inventory_data = read_inventory_data()

    # Prompt the user to enter the code range to search for
    start_code = input("Enter the starting code: ")
    end_code = input("Enter the ending code: ")

    # Search for items within the code range
    matching_items = []
    for item in inventory_data:
        if start_code <= item.get_code() <= end_code:
            matching_items.append(item)

    # Print the matching items
    print("Matching Items:")
    if len(matching_items) > 0:
        for item in matching_items:
            print(f"Code: {item.get_code()}")
            print(f"Description: {item.get_description()}")
            print(f"Category: {item.get_category()}")
            print(f"Unit: {item.get_unit()}")
            print(f"Price: {item.get_price()}")
            print(f"Quantity: {item.get_quantity()}")
            print(f"Minimum Threshold: {item.get_minimum()}")
            print("--------------------")
    else:
        print("No matching items found.")


def search_items_by_category():
    # Read the data from the inventory.txt file and store it in a master list
    inventory_data = read_inventory_data()

    # Prompt the user to enter the category to search for
    search_category = input("Enter the category to search for: ")

    # Search for items with matching category
    matching_items = []
    for item in inventory_data:
        if search_category.lower() == item.get_category().lower():
            matching_items.append(item)

    # Print the matching items
    print("Matching Items:")
    if len(matching_items) > 0:
        for item in matching_items:
            print(f"Code: {item.get_code()}")
            print(f"Description: {item.get_description()}")
            print(f"Category: {item.get_category()}")
            print(f"Unit: {item.get_unit()}")
            print(f"Price: {item.get_price()}")
            print(f"Quantity: {item.get_quantity()}")
            print(f"Minimum Threshold: {item.get_minimum()}")
            print("--------------------")
    else:
        print("No matching items found.")


def read_inventory_data():
    # Read the inventory data from the inventory.txt file and return it as a list of InventoryItem objects
    inventory_data = []
    with open("inventory.txt", "r") as file:
        for line in file:
            line = line.strip().split("\t")
            item = InventoryItem(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
            inventory_data.append(item)
    return inventory_data


def write_inventory_data(inventory_data):
    # Write the inventory data from the list of InventoryItem objects to the inventory.txt file
    with open("inventory.txt", "w") as file:
        for item in inventory_data:
            file.write(f"{item.get_code()}\t{item.get_description()}\t{item.get_category()}\t"
                       f"{item.get_unit()}\t{item.get_price()}\t{item.get_quantity()}\t{item.get_minimum()}\n")


# Main Program
def main():
    while True:
        print("Welcome to the Grocery Store Inventory System!")
        print("Please login to continue.")

        global current_user

        # User Authentication
        while True:
            user_type = user_authentication()
            if user_type is not None:
                current_user = User("", "", user_type)
                break

        # Access Control
        if current_user.get_user_type() == "admin":
            print("\nAccess Granted!")
            while True:
                print("\n--- Admin Menu ---")
                print("1. Add New User")
                print("2. Insert New Item")
                print("3. Update Item")
                print("4. Delete Item")
                print("5. Stock Taking")
                print("6. View Replenish List")
                print("7. Stock Replenishment")
                print("8. Search Items by Description")
                print("9. Search Items by Code Range")
                print("10. Search Items by Category")
                print("11. Logout")
                choice = input("Enter your choice: ")

                if choice == "1":
                    add_new_user()
                elif choice == "2":
                    insert_new_item()
                elif choice == "3":
                    update_item()
                elif choice == "4":
                    delete_item()
                elif choice == "5":
                    stock_taking()
                elif choice == "6":
                    view_replenish_list()
                elif choice == "7":
                    stock_replenishment()
                elif choice == "8":
                    search_items_by_description()
                elif choice == "9":
                    search_items_by_code_range()
                elif choice == "10":
                    search_items_by_category()
                elif choice == "11":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice.")

        elif current_user.get_user_type() == "inventory-checker":
            print("\nAccess Granted!")
            while True:
                print("\n--- Inventory Checker Menu ---")
                print("1. View Replenish List")
                print("2. Search Items by Description")
                print("3. Search Items by Code Range")
                print("4. Search Items by Category")
                print("5. Logout")
                choice = input("Enter your choice: ")

                if choice == "1":
                    view_replenish_list()
                elif choice == "2":
                    search_items_by_description()
                elif choice == "3":
                    search_items_by_code_range()
                elif choice == "4":
                    search_items_by_category()
                elif choice == "5":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice.")

        elif current_user.get_user_type() == "purchaser":
            print("\nAccess Granted!")
            while True:
                print("\n--- Purchaser Menu ---")
                print("1. Stock Replenishment")
                print("2. Search Items by Description")
                print("3. Search Items by Code Range")
                print("4. Search Items by Category")
                print("5. Logout")
                choice = input("Enter your choice: ")

                if choice == "1":
                    stock_replenishment()
                elif choice == "2":
                    search_items_by_description()
                elif choice == "3":
                    search_items_by_code_range()
                elif choice == "4":
                    search_items_by_category()
                elif choice == "5":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice.")

        else:
            print("\nAccess Denied!")

        # Prompt the user to continue or exit the program
        while True:
            option = input("\nDo you want to continue (Y/N)? ").lower()
            if option == "n":
                print("Exiting the program...")
                return
            elif option == "y":
                break
            else:
                print("Invalid option. Please enter 'Y' or 'N'.")


if __name__ == "__main__":
    main()
