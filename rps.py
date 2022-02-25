import random

r = "rock"
p = "paper"
s = "scissors"

rps = ['s','p','r']
system = random.choice(rps)
print ("let's play rock, paper, scissors! ")
player = input("What is your choice? (r)ock, (p)aper, (s)cissors " )

if player  == "r" and system == 'r':
    print("You chose rock, computer chose rock!")
    print("tied")

elif player  == "r" and system == 's':
    print("You chose rock, computer chose scissors!")
    r
    print("yeah! you win.")


elif player  == "r" and system == 'p':
    print("You chose rock, computer chose paper!")
    print("Sorry! you lose.")

elif player  == "p" and system == 'r':
    print("You chose paper, computer chose rock!")
    print("yeah! you win.")

elif player  == "p" and system == 's':
    print("You chose paper, computer chose scissors!")
    print("Sorry! you'r paper got cut to pieces.")

elif player  == "p" and system == 'p':
    print("You chose paper, computer chose paper!")
    print("tied")

elif player  == "s" and system == 'r':
    print("You chose scissors, computer chose rock!")
    print("Sorry! your scissors got smashed. ")

elif player  == "s" and system == 's':
    print("You chose scissors, computer chose scissors!")
    print("tied")

elif player  == "s" and system == 'p':
     print("You chose scissors, computer chose paper!")
     print("yeah! you win.")

else :
 print("please,choice (r)ock, (p)aper, (s)cissors next time.")