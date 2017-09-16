from globals import ss
from termcolor import cprint,colored


def status(current_status_message):
    updated_message = None
    # Checking default status
    if current_status_message != None:
        cprint('Your current status message is %s \n' % current_status_message, "yellow")
    else:
        cprint("You don't have any current status", "yellow")
    # Adding status
    default = raw_input(colored("do you want to choose from old status (y/n) ", 'yellow'))
    if default == "y" or default == "Y":
        counter = 1
        for message in ss:
            print '%d. %s' % (counter, message)
            counter = counter + 1
        choice = int(raw_input("please choose your status"))
        if len(ss) >= choice:
            updated_message = ss[choice-1]
            print"your updated message is " + updated_message
        else:
            cprint("wrong choice", "red", attrs=["bold"])
    # User wants to add new status
    elif default == "n" or default == "N":
            status_message = raw_input("Enter your status update")
            if len(status_message) >= 1:
                ss.append(status_message)
                updated_message = status_message
                final = "your updated status message is " + updated_message
                cprint(final, "magenta", attrs=['bold'])
            else:
                cprint("Status must have a body", "red")
    else:
        cprint("Wrong choice choose correct", "red")

    return updated_message