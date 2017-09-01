from globals import ss, current_status_message


def status(status_message):

    if status_message != None:
        print "your current status is" + current_status_message + "\n"
    elif status_message == None:
        print "You don't have any current status"
        default = raw_input("do you want to choose from old status (y/n) ")
        if default == "y" or default == "Y":
            print "\n" .join(ss)
            choice = int(raw_input(""))
            status_message = ss[choice-1]
            print status_message
            print "Status Updated"
            return status_message
        elif default == "n" or default == "N":
            status_message = raw_input("Enter your status update")
            return status_message