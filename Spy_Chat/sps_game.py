import random
print "Let's Play Stone Paper Scissor :)"
ch = 'y'
tries = 0
win = 0
lose = 0
while ch == 'y' or ch == 'Y':
    comp = random.randint(1, 3)
    user = int(raw_input("What you choose\n1. Stone 2. Paper 3. Scissor\n"))
    if user == 1 and comp == 1:
        print "You choose Stone\nComputer also choose Stone\nIt,s a tie!!!"
    elif user == 1 and comp == 2:
        print "You choose Stone\nComputer choose Paper\nComputer Wins!!!"
        lose = lose+1
    elif user == 1 and comp == 3:
        print "You choose Stone\nComputer choose Scissor\nYou Win!!!"
        win = win+1
    elif user == 2 and comp == 1:
        print "You choose Paper\nComputer choose Stone\nYou Win!!!"
        win = win+1
    elif user == 2 and comp == 2:
        print "You choose Paper\nComputer also choose Paper\nIt's a Tie!!!"
    elif user == 2 and comp == 3:
        print "You choose Paper\nComputer choose Scissor\nComputer Win's!!!"
        lose = lose+1
    elif user == 3 and comp == 1:
        print "You choose Scissor\nComputer choose Stone\nComputer Win!!!"
        lose = lose+1
    elif user == 3 and comp == 2:
        print "You choose Scissor\nComputer also choose Paper\nYou Win!!!"
        win = win+1
    elif user == 3 and comp == 3:
        print "You choose Scissor\nComputer choose Scissor\nIt's a Tie!!!"
    else:
        print "Wrong choice"
    tries = tries+1
    print "Score:\nTries = "+str(tries)+"\nWins's = "+str(win)+"\nLose = "+str(lose)
    ch = raw_input("Wanna try again\nPress (Y/N)")
if ch == 'n' or ch == 'N':
    print "Well played!!!!"
    print "Score:\nTries = " + str(tries) + "\nWins's = " + str(win) + "\nLose = " + str(lose)
    exit()
