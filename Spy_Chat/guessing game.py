import random
print "Let's Get Started\n"
count = 0
var =1
tries =0
while(var==1):
    print "Guess a Number Between 1 to 9 (1 & 9 included) press 0 to exit"
    user = int(raw_input("Enter the Number "))
    if (user==0):
        exit()
    elif  (user>0) and (user<10) :
        print "you choosed "+str(user)
        i = random.randint(1, 9)
        print "The random number is "+str(i)
        if (user==i):
            count = count+1
            print "correct guess "+str(count)
    else:
     print "wrong choice"
    tries = tries+1
    print "you tried %d" %(tries)

