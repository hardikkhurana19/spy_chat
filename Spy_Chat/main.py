from __builtin__ import raw_input
from lib2to3.fixes import fix_imports2

from default_spy import spy
from default_user import details
from choices import choices



print "Let's Get Started!!"

choice = raw_input("Do you want to continue as "+spy['name']+" "+spy['salutation']+" or not (Y/N)\n")
if choice == "y" or choice == "Y":
    print "Welcome "+spy['name']+" "+spy['salutation']
    while True:
            choices()
elif choice == "n" or choice == "N":
    print "Enter Your Details:"
    details()
    choices()