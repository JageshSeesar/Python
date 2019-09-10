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


# Function to return LCM of two numbers
def lcm(a, b):
    return (a * b) / hcf(a, b)


# Driver program to test above function
print('LCM of', a, 'and', b, 'is: ', lcm(a, b))
print("*******************************************************************************************")
