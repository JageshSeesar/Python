list1 = []
list2 = []
list3 = []
list4 = []

# inputList1 = input("Enter your first value and press Enter to enter second value: ")
# storeInList1 = list1.append(inputList1)
# inputList1 = input("Enter your second value and press Enter to enter third value: ")
# storeInList1 = list1.append(inputList1)
# inputList1 = input("Enter your third value and press Enter to enter forth value: ")
# storeInList1 = list1.append(inputList1)
# inputList1 = input("Enter your forth value and press Enter to continue: ")
# storeInList1 = list1.append(inputList1)

print("**************************************************************************")
print("Program to check which sum of element of 4 lists is highest")
print("WELCOME")
print("**********************************************************************************")
inputList1 = input("Enter elements of the First List separated by comma: ")
list1 = inputList1.split(",")
sum1 = 0
for X in list1:
    sum1 = sum1 + int(X)
print(sum1)

inputList2 = input("Enter elements of the Second List separated by comma: ")
list2 = inputList2.split(",")
sum2 = 0
for X in list2:
    sum2 = sum2 + int(X)
print(sum2)

inputList3 = input("Enter elements of the Third List separated by comma: ")
list3 = inputList3.split(",")
sum3 = 0
for X in list3:
    sum3 = sum3 + int(X)
print(sum3)

inputList4 = input("Enter elements of the Forth List separated by comma: ")
list4 = inputList4.split(",")
sum4 = 0
for X in list4:
    sum4 = sum4 + int(X)
print(sum4)

print("*******************************************************************************")
if sum1 > sum2 and sum1 > sum3 and sum1 > sum4:
    print("List whose sum of element is highest is the First List with sum =", sum1)

elif sum2 > sum1 and sum2 > sum3 and sum2 > sum4:
    print("List whose sum of element is highest is the Second List with sum =", sum2)


elif sum3 > sum1 and sum3 > sum2 and sum3 > sum4:
    print("List whose sum of element is highest is the Third List with sum =", sum3)

elif sum4 > sum1 and sum4 > sum2 and sum4 > sum3:
    print("List whose sum of element is highest is the Forth List with sum =", sum4)

else:
    print("sum of elements in some lists are the same")


print("*********************************************************************************")
# elif sum1 == sum2 and sum2 == sum1:
#  print("Sum of elements in list1 and list2 are same")
# elif sum1 == sum3 and sum3 == sum1:
#    print("Sum of elements in list1 and list3 are same")
# elif sum1 == sum4 and sum4 == sum1:
#   print("Sum of elements in list1 and list4 are same")
# elif sum2 == sum3 and sum3 == sum2:
#    print("Sum of elements in list2 and list3 are same")
# elif sum2 == sum4 and sum4 == sum2:
#    print("Sum of elements in list2 and list4 are same")
# elif sum3 == sum4 and sum4 == sum3:
#    print("Sum of elements in list3 and list4 are same")
# sum of these list are the same:
