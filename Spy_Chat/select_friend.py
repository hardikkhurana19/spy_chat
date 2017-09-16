from globals import friends
from termcolor import colored,cprint


def select_friend():
    counter = 1
    for friend in friends:
        print str(counter)+". " + friend['name']
        counter += 1

    user_input = int(raw_input(colored("Choose the friend\n", 'yellow')))
    if user_input <= counter:
        return user_input-1
    else:
        cprint("wrong Choice", "red")
        return 1
