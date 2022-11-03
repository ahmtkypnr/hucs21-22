number = int(input("Please write the number: "))
if(number==0):
    binary = 0
else:
    binary = ""
    while number>0:
        rem = number%2
        binary = str(rem) + binary
        number = number//2
    binary = int(binary)
print(binary)