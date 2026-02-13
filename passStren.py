##########################################################################################
#Code by Julien Saindon
# This is a simple password complexity verifier made by me
###########################################################################################
def length(passw):
    point1 = 0
    if (len(passw) >= 8):
        point1+=2
    if (len(passw) >= 12):
        point1+=1
    return point1

def case(passw):
    point2 = 0
    for letter in passw:
        if letter.isupper():
            point2+=1
            break;
    for letter in passw:
        if letter.islower():
            point2+=1
            break
    return point2

def numbers(passw):
    point3 = 0
    for num in passw:
        if num.isdigit():
            point3+=1
            break
    return point3
         
    

def spec(passw):
    point4 = 0
    for num in passw:
        if not num.isalnum():
            point4+=1
            break
    return point4
        
def score(score):
    if (score >=0 and score <=2):
        return "This password is weak - easy to crack"
    if (score >=3 and score <=4):
        return "Weak – could be improved."
    if (score ==6):
        return "Medium – decent, but add more variety."
    if (score == 5):
        return "Strong – good password!"
    if (score == 7):
        return "Very strong – excellent!"
    


passw = input("Welcome to the password strength checker\n Please enter your password here:")

point1 = length(passw)  #this function checks the length and awards point
point2 = case(passw)    #this function checks the case and awards point
point3 = numbers(passw) #this function checks if theres any numbers and awards point
point4 = spec(passw)    #this function checks if any special characters
total = point1 + point2 + point3 + point4 # this will add up the total
score = score(total)  

print("\nYour total is " + str(total) + "/7. " + score)
    