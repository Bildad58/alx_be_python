shopping_list = []

def display_menu():
    print("Shopping list manager!")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping items")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list.append()
            print("shopping_list")
            pass

        elif choice == '2':
            # Prompt for and remove an item
            shopping_list.remove()
            print ("shopping_list")
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


