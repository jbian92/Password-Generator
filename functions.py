import random

def generator(data):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_chars = ['!', '@', '#', '%', '+', '/', '\\', "'", '$', '^', '?', ':', ',', '(', ')', '{', '}', '[', ']', '~', '-', '_', '.']
    length = data['length']
    num_checked_boxes = data['num_checked_boxes']
    lower = upper = numeric = special = ""

    # frequency for each category initialized to zero
    required = {
        'num_lower': 0,
        'num_upper': 0,
        'num_numeric': 0,
        'num_special': 0
    }

    # categories checked off by the user
    required_list = data['checked_categories']

    # -- Determine the frequency of each different category of characters --
    if num_checked_boxes == 4:
        required[required_list[0]] = random.randint(1, length - 3)
        required[required_list[1]] = random.randint(1, length - required[required_list[0]] - 2)
        required[required_list[2]] = random.randint(1, length - required[required_list[0]] - required[required_list[1]] - 1)
        required[required_list[3]] = length - required[required_list[0]] - required[required_list[1]] - required[required_list[2]]
    elif num_checked_boxes == 3:
        required[required_list[0]] = random.randint(1, length - 2)
        required[required_list[1]] = random.randint(1, length - required[required_list[0]] - 1)
        required[required_list[2]] = length - required[required_list[0]] - required[required_list[1]]
    elif num_checked_boxes == 2:
        required[required_list[0]] = random.randint(1, length - 1)
        required[required_list[1]] = length - required[required_list[0]]
    else:
        required[required_list[0]] = length
    
    # -- Get each category's characters -- 
    for i in range(required['num_upper']):
        upper += (random.choice(alphabet)).upper()
    
    for i in range(required['num_lower']):
        lower += random.choice(alphabet)

    for i in range(required['num_numeric']):
        numeric += str(random.randint(0, 9))

    for i in range(required['num_special']):
        special += random.choice(special_chars)
    
    # concatenate the strings and convert to a list
    password_list = list(upper + lower + numeric + special)

    # randomly shuffle the characters in the password
    random.shuffle(password_list)
    
    # return the password as a string
    return "".join(password_list)