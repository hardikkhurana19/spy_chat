import datetime
import time
from select_friend import select_friend
from steganography.steganography import Steganography
from globals import friends
from termcolor import cprint,colored
import re


def send_message():
    # Checking current friend list
    if len(friends) != 0:
        friend_choice = select_friend()
        while True:
            # verifying the user input for sending message using regex
            original_image = raw_input(colored("Choose the image to hide the text:", "yellow"))
            if len(original_image) > 0:
                image_pattern = '^[1-9]*[a-zA-Z\s]+\.jpg$'
                if re.match(image_pattern, original_image) != None:
                    if original_image == "mmu.jpg":
                        while True:
                            output_path = raw_input(colored("Enter the name of output image:", "yellow"))
                            if len(output_path) > 0:
                                image_pattern = '^[1-9]*[a-zA-Z\s]+\.jpg$'
                                if re.match(image_pattern, output_path) != None:
                                    while True:
                                        text = raw_input(colored("Enter your message:", "yellow"))
                                        if len(text) >= 1:
                                            if len(text) < 100:
                                                Steganography.encode(original_image, output_path, text)
                                                # Appending chat details to friends list
                                                new_chat = {
                                                    "message": text,
                                                    "time": time.strftime("%I:%M:%S"),
                                                    "day": datetime.date.today().strftime("%d"),
                                                    "month": datetime.date.today().strftime("%B"),
                                                    "year": datetime.date.today().strftime("%Y"),
                                                    "sent_by_me": True

                                                }
                                                friends[friend_choice]['chats'].append(new_chat)
                                                cprint("Your secret message is ready ", "blue", attrs=['bold'])
                                                break
                                            else:
                                                cprint("message must have less than 100 characters", "red")
                                        else:
                                            cprint("Enter some message to send", "red")
                                    break
                                else:
                                    cprint("image must be in jpg format", "red")
                            else:
                                cprint("enter image name to continue", "red")
                        break
                    else:
                        cprint("You must choose the image mmu.jpg", "red")
                else:
                    cprint("image must be in jpg format", "red")
            else:
                cprint("enter image name to continue", "red")

    else:
        cprint("You Don't have any friends yet -_-", "grey")

