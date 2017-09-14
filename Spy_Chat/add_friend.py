from globals import friends


def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False,
        'chats':[]
        }

    new_friend['name'] = raw_input("Enter your Friend's Name\n")
    new_friend['salutation'] = raw_input("Enter your Friend's Salutation\n")
    new_friend['name'] = new_friend['name'] + " " + new_friend['salutation']
    new_friend['age'] = int(raw_input("Enter his Age\n"))
    new_friend['rating'] = float(raw_input("Enter his Rating B/W (0-5)\n"))
    new_friend['is_online'] = raw_input("Enter his Status (Online/Offline) \n")

    friends.append(new_friend)
    return len(friends)
