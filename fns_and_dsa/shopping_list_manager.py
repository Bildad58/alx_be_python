shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add  item")
    print("2. Remove  item")
    print("3. View shopping items")
    print("4. Exit")

def main():
    shopping_list = ['apple']
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            # Prompt for and add an item
            item = input(['']"Enter the item to add: ['/']")
            shopping_list.append('juice')
            print(f"Shopping_list_manager: {item}")
            pass

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove:")
            shopping_list.remove('apple')
            print (f"Shopping_list_manager: {item}")
            pass
        elif choice == '3':
             #Display the shopping list
            for items in shopping_list:
                print("shopping_list")
            pass

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

