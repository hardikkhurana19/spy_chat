from datetime import datetime
from select_friend import select_friend
from steganography.steganography import Steganography
from globals import friends


def send_message():
    friend_choice = select_friend()
    original_image = raw_input("Choose the image to hide the text:")
    output_path = raw_input("Enter the name of output image:")
    text = raw_input("Enter your message:")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True

    }

    # friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready "

