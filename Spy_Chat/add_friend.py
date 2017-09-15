from globals import friends
from termcolor import cprint, colored
import re

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False,
        'chats':[]
        }

    new_friend['name'] = raw_input(colored("Enter your Friend's Name\n", "yellow"))
    while new_friend['name'].isalpha() == False:
        cprint("Name can't be empty and only contains alphabets", "red")
        new_friend['name'] = raw_input(colored("Enter your Friend's Name\n", "yellow"))
    new_friend['salutation'] = raw_input(colored("Enter your Friend's Salutation\n", "yellow"))
    while new_friend['salutation'].isalpha() == False:
        cprint("Salutation can't be empty and only contains alphabets", "red")
        new_friend['salutation'] = raw_input(colored("Enter your Friend's Salutation\n", "yellow"))
    new_friend['name'] = new_friend['name'] + " " + new_friend['salutation']
    new_friend['name'] = colored(new_friend['name'], "magenta", attrs=['bold'])
    try:
        while True:
            new_friend['age'] = int(raw_input(colored("Enter his Age\n", "yellow")))
            age_pattern = '^[0-9]{1,3}$'
            if re.match(age_pattern, str(new_friend['age'])) != None:
                    if new_friend['age'] >= 18 and new_friend['age'] <= 50 and new_friend['age']<110:
                        new_friend['rating'] = float(raw_input(colored("Enter his Rating B/W (0-5)\n", "yellow")))


                        new_friend['is_online'] = raw_input("Enter his Status (Online/Offline) \n")
                        break
                    else:
                        cprint("Age must be b/w (18-50) Sorry -_-", "grey", attrs=['bold'])
            else:
                    cprint("Age cant be more then 3 digits", "red")

    except ValueError:
            cprint("Please enter correct age ", "red")
    friends.append(new_friend)
    return len(friends)
