import sys
try:
    two_points = int(sys.argv[1])
    three_points = int(sys.argv[2])
    free_throws = int(sys.argv[3])
    players_score = (2*two_points) + (3*three_points) + (free_throws)
    print(players_score)
except IndexError:
    pass
except:
    print(-1)

def healthStatus(height, mass):
    try:
        bmi = mass / ((height/100) ** 2)  
        if(bmi<18.5):
            return "underweight"
        if(18.5<=bmi<24.9):
            return "healthy"
        if(24.9<=bmi<30):
            return "overweight"
        if(30<=bmi):
            return "obese"
    except:
        return -1
    
#Name: Ahmet İkbal
#Surname: Kayapınar
#Number: 2210356043