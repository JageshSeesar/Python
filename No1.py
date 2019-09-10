print("**************************************************************************")
print("WELCOME")
print("**************************************************************************")
sentence = input("Enter a Sentence with Uppercase, Lowercase, Digits, and Special Characters: ")
upper = int(0)
lower = int(0)
digit = int(0)
sp_char = int(0)

for c in sentence:
    if c.isupper():
        upper = upper + 1
    elif c.islower():
        lower = lower + 1
    elif c.isdigit():
        digit = digit + 1
    else:
        sp_char = sp_char + 1
print("*****************************************************************************")
print("No. of Upper case characters : ", upper)
print("No. of Lower case Characters : ", lower)
print("No. of Digits: ", digit)
print("No. of Special Characters", sp_char)
print("*****************************************************************************")

