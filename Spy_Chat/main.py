from __builtin__ import raw_input
from default_spy import spy
from default_user import details
from choices import choices
from termcolor import colored, cprint

while True:
    cprint("Let's Get Started!!", "cyan", attrs=['dark', 'underline', 'bold'])
    choice = raw_input(colored("Do you want to continue as "+spy['name']+" "+spy['salutation']+" or not (Y/N)\n", "yellow"))
    if choice == "y" or choice == "Y":
        cprint("Welcome " + spy['name']+" "+spy['salutation'], "magenta", attrs=["bold"])
        while True:
                choices()
    elif choice == "n" or choice == "N":
        print "Enter Your Details:"
        details()
        choices()
    else:
        if choice == "e" or choice == "E":
            cprint("you pressed the quit button \n     GoodBye!!!", "red")
            exit()
        cprint("please try again", "red")
        cprint("For exit press E", "red", attrs=["bold"])


