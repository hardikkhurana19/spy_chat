from steganography.steganography import Steganography
from select_friend import select_friend


def read_message():
    sender = select_friend()
    encrypted_image = raw_input("Enter encrypted image:")
    secret_message = Steganography.decode(encrypted_image)
    print str(sender) + "sends you " + secret_message
