# ===================================================================================
# DAY 14: SHOPPING LIST APP PRO MAX
# TOPICS: File Hanling, List, Functions, Categories
# AUTHOR: DESIGN CHRISTOPHER OKESON
# DATE: 13-08-2026
# ====================================================================================

shopping_list = []


def add_item():
    name = input("Enter item name: ")
    category = input("Enter category - Food/Toiletries/Electronics/Other: ")
    try:
        price = float(input(f"Enter price: N"))
        shopping_list.append([name, category, price])
        print(f"{name} added to {category} category!")
    except:
        print("Please enter a valid number for price")

def show_list():
    if not shopping_list:
        print("Your shopping list is empty")
        return
    print("\n=========YOUR SHOPPING LIST========")
    total = 0
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item[0].title()} -  {item[1]} - N{item[2]:.2f}")
        total += item[2]
    print("----------------------------------")
    print(f"TOTAL: N{total:.2f}")
    print("=================================================")

def remove_item():
    show_list()
    if len(shopping_list) == 0:
        return
    try:
        num = int(input("which number do you want to remove? "))
        removed = shopping_list.pop(num - 1)
        print(f"{removed[0]} removed")

    except:
        print("invalid number")

def save_list():
    file = open("shopping_list.txt", "w")
    for item in shopping_list:
        file.write(f"{item[0]}, {item[1]}, {item[2]}\n")
    file.close()
    print("list saved to shopping_list.txt")

def load_list():
    global shopping_list
    try:
        file = open("shopping_list.txt", "r")
        for line in file:
            name, category, price = line.strip().split(",")
            shopping_list.append([name, category, float(price)])
        file.close()
        print("previous list loaded!")
    except FileNotFoundError:
        pass

def search_item():
    search = input("Enter item name to search: ").lower()
    found = False
    for i, item in enumerate(shopping_list, 1):
        if search in item[0].lower():
            print(f"{i}. {item1[0].title()} - N{item[1]:.2f}")
            found = True
    if not found:
        print("item not found")

def edit_item():
    show_list()
    try:
        num = int(input("Enter item number to edit: "))
        if 1 <= num <= len(shopping_list):
            new_price = float(input("Enter new price: N"))
            shopping_list[num-1][2] = new_price
            print("Price updated")

        else:
            print("Invalid number")
    except:
        print("Please enter numbers only")

def clear_list():
    confirm = input("Are you sure? This will delete everything y/n: ").lower()
    if confirm == "y":
        shopping_list.clear()
        print("List cleared")

while True:
    print("\n==WELCOME TO YOUR SHOPPING LIST APP DESIGN CHRISTOPHER==")    
    print("1. Add item")
    print("2. Show List")
    print("3. Remove item")
    print("4. Save list to file")
    print("5. search item")
    print("6. Edit item price")
    print("7. clear Entire List")
    print("8. Exit")

    choice = input("Choose 1-8: ")

    if choice == "1":
            add_item()
    elif choice == "2":
            show_list()
    elif choice == "3":
            remove_item()
    elif choice == "4":
            save_list()
    elif choice == "5":
        search_item()
    elif choice == "6":
        edit_item()
    elif choice == "7":
        clear_list()
    elif choice =="8":
        save_list()
        print("Goodbye! Thank you shopping with us")
        break
    else:
         print("invalid choice. Try 1-8")

