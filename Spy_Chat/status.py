from globals import ss


def status(current_status_message):
    updated_message = None

    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print "You don't have any current status"
    default = raw_input("do you want to choose from old status (y/n) ")
    if default == "y" or default == "Y":
        counter = 1
        for message in ss:
            print '%d. %s' % (counter, message)
            counter = counter + 1
        choice = int(raw_input("please choose your status"))
        if len(ss) >= choice:
            updated_message = ss[choice-1]
            print "your updated message is " + updated_message
        else:
            print "wrong choice"
    elif default == "n" or default == "N":
            status_message = raw_input("Enter your status update")
            if len(status_message) >= 1:
                ss.append(status_message)
                updated_message = status_message
                print "your updated status message is " + updated_message
    else:
        print"Wrong choice choose correct"

    return updated_message