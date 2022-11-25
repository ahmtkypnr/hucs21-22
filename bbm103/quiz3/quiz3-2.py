import sys

numbers = sys.argv[1::2] # It chooses odd numbers.

i = 1 # A loop counter. It is used for finding the a variable.

# If statement checks length of numbers to avoid the index error.
if(len(numbers)>1):
    while True:
        # a is the number that its multiplies will be eliminated.
        a = int(numbers[i])
        # By using a, it creates a list from numbers that to be removed.
        rem_numbers = numbers[a - 1::a]
        for number in rem_numbers:
            numbers.remove(number)
        i += 1
        # A if statement that finishes the loop.
        if(a>len(numbers)):
            break

print(numbers)