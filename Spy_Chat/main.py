from __builtin__ import raw_input
from default_spy import spy
from default_user import details
from choices import choices
from termcolor import colored, cprint


cprint("Let's Get Started!!", "cyan", attrs=['dark', 'underline', 'bold'])
choice = raw_input(colored("Do you want to continue as "+spy['name']+" "+spy['salutation']+" or not (Y/N)\n", "red"))
if choice == "y" or choice == "Y":
    cprint("Welcome " + spy['name']+" "+spy['salutation'], "blue")
    while True:
            choices()
elif choice == "n" or choice == "N":
    print "Enter Your Details:"
    details()
    choices()

