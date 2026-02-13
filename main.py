import random #this will import random functions
import string #this will import constants to select certain strings

letters = string.ascii_letters #this will import from the string libraries a list of ascii characters
numbers = [1,2,3,4,5,6,7,8,9]
symbols = string.punctuation
strongPass = []
medPass = []
easyPass = []


def strongPassword():
        while (len(strongPass) <= 16):
            num = str(random.randrange(0, 9)) #this will select a random integer
            let = random.choice(letters) # this will randomly select letters from the letters array using the random module
            sym = random.choice(symbols)
            strongPass.append(num)
            strongPass.append(let)
            strongPass.append(sym)

def medPassword():
    while (len(medPass) <= 8):
        num = str(random.randrange(0, 9)) #this will select a random integer
        let = random.choice(letters) # this will randomly select letters from the letters array using the random module
        sym = random.choice(symbols)
        medPass.append(num)
        medPass.append(let)
        medPass.append(sym)

def easyPassword():
    while (len(easyPass) <= 4):
        num = str(random.randrange(0, 9)) #this will select a random integer
        let = random.choice(letters) # this will randomly select letters from the letters array using the random module
        sym = random.choice(symbols)
        easyPass.append(num)
        easyPass.append(let)
        easyPass.append(sym)
             

           

print("___________________________________________________________________________\n")
print("Welcome, to your own personal password generator, press (y) to continue...")
answer=input()
print("____________________________________________________________________________")
if answer == "y":
    print("Let's begin, \n Do you want a strong(s), medium(m) or easy(e)")
    strength=input()
    if (strength == "s"):
        print("Great, here you go: \n ")
        strongPassword() #calling function
        print("".join(strongPass))

    if (strength == "m"):
        print("Great, here you go: \n ")
        medPassword() #calling function
        print("".join(medPass))

    if (strength == "e"):
        print("Great, here you go: \n ")
        easyPassword() #calling function
        print("".join(easyPass))




