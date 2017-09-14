def age():
    while True:
        try:
            spy_age = int(raw_input("Enter your age: \t (18-50)\n"))
            if spy_age >18 and spy_age <50:
                return spy_age
            else:
                print "you are under age Sorry -_-"
        except ValueError:
            print "Please enter correct age "


def rating():
    while True:
        try:
            spy_rating = int(raw_input("How much you rate yourself----->\nB/W (0-5)"))
            if spy_rating == 0:
                print "Not Good Start Working on yourself"
            elif spy_rating > 0 and spy_rating < 1:
                print "Good but need improvement"
                return spy_rating

            elif spy_rating >= 1 and spy_rating < 2:
                print "NIce "
                return spy_rating

            elif spy_rating >= 2 and spy_rating <3:
                print "Very good"
                return spy_rating

            elif spy_rating >= 3 and spy_rating <4:
                print "Great"
                return spy_rating

            elif spy_rating >= 4 and spy_rating <5:
                print "Excellent"
                return spy_rating

            elif spy_rating == 5:
                print "ACE!!!!!!!!!!"
                return spy_rating

            else:
                print "Wrong choice"

        except ValueError:
            print "Wrong Spy Rating \n Rating should be B/W (0-5)"



def name():
    spy_name = raw_input("What's your name------>\n")
    if len(spy_name) > 0 and spy_name != " ":   # logic will be here if condition is true

        spy_salutation = raw_input("What should we call you\n")
        spy_name = spy_name + " " + spy_salutation
        print "Let's get Started Mr. " + spy_name
        return spy_name


def details():
    a = name()
    b = age()
    c = rating()
    print "Welcome Mr. %s you are %s years old and you rated yourself %s" % (a, b, c)

