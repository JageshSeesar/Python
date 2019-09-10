Pharma_List = []
print("*******************************************************************************************")
print("Welcome to the stock of your Pharmacy")
print("*******************************************************************************************")
user_input = input("Enter your items in your stock separated by comma: ")
Pharma_List = user_input.split(",")
print(Pharma_List)

choice = int(input("To add an item press 1| To remove an item press 2| To insert an item in an specified position press 3 --> "))

if choice == 1:
    print("This option allows you to add an item in your stock")
    input_item = input("Enter item you want to add: ")
    Pharma_List.append(input_item)
    print(Pharma_List)

elif choice == 2:
    print("This option allows you to remove an item in your stock")
    input_item = input("Enter item you want to remove: ")
    if input_item in Pharma_List:
        Pharma_List.remove(input_item)
        print(Pharma_List)
    else:
        print("This item is not in the stock")

elif choice == 3:
    print("This option allows you to insert an item to a specified position in your stock list")
    input_item = input("Enter item you want to insert: ")
    position = int(input("In which position in the stock list would you like to add it ?"))
    if position < len(Pharma_List):
        Pharma_List.insert(position, input_item)
        print(Pharma_List)
    else:
        print("Invalid Position")


print("*******************************************************************************************")

