print("Welcome to my Quiz!")
option = " "

option = input("Do you want to play? (Yes/No)   ")

if option.lower() != "yes": 
    quit()

print("Let's Play!")
marks = 0 
answer = input("Which was the first fully supported 64-bit operating system?  ")
if answer.lower() == 'linux':
    print("Correct!")
    marks +=1
else:
    print("Incorrect, the correct answer is : linux")
answer = input("What protocol is used to recieve mail? ")
if answer.lower() == "pop3":
    print("Correct!")
    marks+=1
else:
    print("Incorrect, the correct answer is : POP3")

answer = input("Which type of number system does the computer use to store data?  ")
if answer.lower() == "binary":
    print("Correct!")
    marks+=1 
else:
    print("Incorrect, the correct answer is : binary")

answer = input("Which data type is immutable?  ")
if answer.lower() == "string":
    print("Correct!")
    marks+=1
elif answer.lower() == "tuple":
    print("Correct!")
    marks+=1
else:
    print("Incorrect, the correct answer is : tuple or string")

answer = input("What is the output of 18//4 in Python?  ")
if answer == '4':
    print("Correct!")
    marks+= 1
else:
    print("Incorrect, the correct answer is : 4")

print("The quiz is done!")
print("You scored : ",marks, "/5")
