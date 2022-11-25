import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

# By using abs function, it always uses a positive number.
number = abs(a**b)

def sum_of_digits(number):
    # Loop works depending on whether the number is single digit or not.
    while number>=10:
        # It converts the number to string for use in the for loop.
        str_number = str(number)
        Sum = 0
        # It adds each digit and assigns the sum to the number.
        for digit in str_number:
            Sum += int(digit)
        number = Sum
    return number

# It checks whether it is a float and if it is, prints 0.
if(0<number<1):
    print(0)
else:
    print(sum_of_digits(number))