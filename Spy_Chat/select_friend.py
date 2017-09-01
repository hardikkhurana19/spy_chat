from globals import friends


def select_friend():
    counter = 1
    for friend in friends:
        print str(counter)+". "+friend['salutation'] + " " + friend['name']
        counter += 1

    user_input = int(raw_input("Choose the friend\n"))
    if user_input <= counter:
        return user_input-1
    else:
        print "wrong Choice"
        return 1
