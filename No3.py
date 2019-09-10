print("*******************************************************************************************")
print("Welcome to palindrome program")
print("*******************************************************************************************")
input_num = int(input("Enter number:"))
temp = input_num
reverse = 0
while input_num > 0:
    dig = input_num % 10
    reverse = reverse * 10 + dig
    input_num = input_num // 10
if temp == reverse:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

print("*******************************************************************************************")

