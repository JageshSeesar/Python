print("*******************************************************************************************")
print("WELCOME to LCM program")
print("*******************************************************************************************")

a = int(input("Enter First number and press Enter: "))
b = int(input("Enter Second number: "))


# func to return hcf for later use
def hcf(a, b):
    if a == 0:
        return b
    return hcf(b % a, a)


print('HCF of', a, 'and', b, 'is: ', hcf(a, b))
print("*******************************************************************************************")

