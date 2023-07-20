# Create an empty dictionary
my_dict ={
    "Toyota": "Corolla",
    "Honda": "Civic",
    "Ford": "Mustang",
    "Chevrolet": "Camaro",
    "BMW": "X5"
}
print("----- Choice Menu -----")
print("1. Access value")
print("2. Modify value")
print("3. Add key-value pair")
print("4. Remove key-value pair")
print("5. Check key existence")
print("6. Get keys")
print("7. Get values")
print("8. Exit")

choice = input("Enter your choice (1-8): ")
match choice:
        case '1':
            key = input("Enter the key: ")
            value = my_dict[key]
            print(f"{my_dict[key]}")
        case '2':
            key = input("Enter the key: ")
            new_value = input("Enter the new value: ")
            my_dict[key] = new_value
            print(f"{key} is updated successfully with {my_dict[key]}")
        case '3':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            my_dict[key] = value
            print(f"Key-value pair '{key}': '{value}' added to the dictionary")
        case '4':
            key = input("Enter the key to remove: ")
            if key in my_dict:
                del my_dict[key]
                print(f"Key-value pair '{key}' removed from the dictionary")
                print("new Dictionary is ",my_dict)
            else:
                print(f"No value found for the key '{key}'")
        case '5':
            key = input("Enter the key to check: ")
            if key in my_dict:
                print(f"Key '{key}' exists in the dictionary")
            else:
                print(f"Key '{key}' does not exist in the dictionary")
        case '6':
            keys = my_dict.keys()
            print("Keys in the dictionary:")
            for key in keys:
                print(key)
        case '7':
            values = my_dict.values()
            print("Values in the dictionary:")
            for value in values:
                print(value)
        case '8':
            print("Exiting the program...")
            exit()
        case _:
            print("Invalid choice! Please enter a number from 1 to 8.")
