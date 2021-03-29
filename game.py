import random
score_c= 0
score_u = 0
cycle = 1
i = 1
while i<=3 :
    print("_______________________________________")
    print("Enter a choice :  ", "1-rock","2-paper","3-scissor")
    print("_______________________________________")

    print ("Computer Score is :", score_c , "     user Score is :", score_u   ,"     cycle :" ,cycle)
 
    computer_rand = random.randint(1,3)
    computer ="rock"
    if computer_rand == 1: computer = "rock"
    if computer_rand == 2 : computer = "paper"
    if computer_rand == 3 : computer = "scissor"

    user = input("chose user is :").lower()

    print(f"chose computer is : {computer}")
    if user == "q" or user == "quit":
        break
    if user == computer: print("mosavi shodi")
    elif user == "rock" and  computer == "paper" : 
        print(" win computer") 
        score_c+=1
    elif user == "paper"  and  computer == "rock" :  
        print(" win user")  
        score_u+=1
    
    elif user == "scissor"  and  computer == "rock" :  
        print(" win computer") 
        score_c+=1
    elif user == "rock"  and  computer == "scissor" : 
        print(" win user") 
        score_u+=1
    elif user == "paper"  and  computer == "scissor" :
        print(" win computer") 
        score_c+=1
    elif user == "scissor"  and  computer == "paper" : 
        print(" win user") 
        score_u+=1
    else : print("voroodi na motabar ast ")
    i+=1
    cycle+=1
print ("Computer Score is :", score_c , "     user Score is :", score_u   ,"     cycle :" ,cycle)
if score_u >score_c:print("*****user is win*****")
else:print("*****computer is win*****") 
    

c = input ("_ baraye khoroj 1 ra vared konid :")
if c == 1:
    exit()
