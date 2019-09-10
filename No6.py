storing_list = []
even_list = []
odd_list = []

print("**************************************************************************")
print("Program to determine odd and even values from a list")
print("WELCOME")
print("**************************************************************************")
user_input = input("Enter integers separated by comma: ")
storing_list = user_input.split(",")
# print(storing_list)

for X in storing_list:
     if (int(X) % 2) == 0:
         new = even_list.append(X)
     else:
         new = odd_list.append(X)

print("List containing Even values: ", even_list)
print("List containing Odd values: ", odd_list)

print("*******************************************************************************************")
