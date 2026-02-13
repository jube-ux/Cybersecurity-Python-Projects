###########################################################################################
#BY:JULIEN SAINDON
#This cybersecurity application takes username as an input and checks if its valid
#It performs a type of user input sanitization to check if this is safe username to use
###########################################################################################



#checks if characters are between 4 and 20 characters
def charcters(username):
       if (len(username) >= 4 and len(username) <=20):
          return True
       else:
           return False

#checks if it starts with a letter
def letter(username):
    if (username[0].isalpha()):
        return True
    else:
        return False

#checks if only contains a-z and A-Z), and number
def check(username):
         if username.isalnum():
             return True
         else:
            return False
             
      


#checks if not username is not common usernames used in wild
def adminCheck(username):
     if (username == "admin" or username == "Admin" or username == "test" or username =="guest"):
        return False
     else:
         return True

#outputs a message saying if its valid or not
def message(check1,check2,check3,check4):
    if all([check1,check2,check3,check4]):
        return print("You have chosen a valid user name, good job!")
    else:
        print("You have entered in invalid username, try to avoid spaces, special characters\nand include numbers and letters")


username = input("Please enter a username: ")
check1 = charcters(username)
check2 = letter(username)
check3 = check(username)
check4 = adminCheck(username)
message(check1,check2,check3,check4)