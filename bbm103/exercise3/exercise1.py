number = int(input("Write a number N: "))
sum_of_odds = 0
sum_of_evens = 0
for i in range(0,number+1,2):
    sum_of_evens += i
for j in range(1,number+1,2):
    sum_of_odds += j
denominator = number//2
if(denominator==0):
    denominator = 1
print("Sum of odds: ",sum_of_odds)
print("Average of evens: ",int(sum_of_evens/denominator))