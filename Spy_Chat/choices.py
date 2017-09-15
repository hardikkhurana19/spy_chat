from status import status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
from termcolor import cprint


def choices():
    from globals import current_status_message
    loop = True
    while loop:

        cprint ("You Can Do following Things\n" \
              "What do you want to do? \n " \
              "1. Add a status update \n " \
              "2. Add a friend \n " \
              "3. Send a secret message \n " \
              "4. Read a secret message \n " \
              "5. Read Chats from a user \n " \
              "6. Close Application \n", "cyan")
        try:
            choice = int(raw_input())
            if choice == 1:
                    current_status_message = status(current_status_message)
            elif choice == 2:
                total = add_friend()
                print "You have " + str(total) + " Friends."

            elif choice == 3:
                    send_message()

            elif choice == 4:
                    read_message()
            elif choice == 5:
                    print
            elif choice == 6:
                    cprint("Thank You\nGood Bye!!!!!!!!!!!!!!", "red")
                    exit()
            else:
                    cprint("Wrong Choice", "red", attrs=["bold"])
                    loop = False
        except ValueError:
            cprint ("Choose from the above please", "green", attrs=["bold"])

