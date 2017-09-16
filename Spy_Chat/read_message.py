from steganography.steganography import Steganography
from select_friend import select_friend
from globals import friends
from termcolor import colored, cprint


def read_message():
    # Checking friends list
    if len(friends) != 0:
        sender = select_friend()
        encrypted_image = raw_input(colored("Enter encrypted image:", "yellow"))
        secret_message = Steganography.decode(encrypted_image)
        print friends[sender]['name'] + " sends you " + "'" + secret_message + "'"
    else:
        cprint("you don't have any friends yet", "red")