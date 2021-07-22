import random

def generator(data):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = data['length']
    checked_boxes = data['checked_boxes']
    lower = upper = numeric = ""
    num_lower = num_upper = num_numeric = 0

    # -- Determine the frequency of each different category of characters --
    if checked_boxes == 3:
        # randomly choose how many uppercase letters 
        num_upper = random.randint(1, length - 2)

        # randomly choose how many lowercase letters
        num_lower = random.randint(1, length - num_upper - 1)
        num_numeric = length - num_upper - num_lower

    elif checked_boxes == 2:
        if data['upper'] and data['lower']:
            # randomly choose how many uppercase letters 
            num_upper = random.randint(1, length - 1)
            num_lower = length - num_upper

        elif data['upper'] and data['numeric']:
            # randomly choose how many uppercase letters 
            num_upper = random.randint(1, length - 1)
            num_numeric = length - num_upper

        elif data['lower'] and data['numeric']:
            # randomly choose how many lowercase letters 
            num_lower = random.randint(1, length - 1)
            num_numeric = length - num_lower
    
    else:
        if data['upper']:
            num_upper = length

        elif data['lower']:
            num_lower = length

        elif data['numeric']:
            num_numeric = length
    
    # -- Get each category's characters -- 
    for i in range(num_upper):
        upper += (random.choice(alphabet)).upper()
    
    for i in range(num_lower):
        lower += random.choice(alphabet)

    for i in range(num_numeric):
        numeric += str(random.randint(0, 9))
    
    # concatenate the strings and convert to a list
    password_list = list(upper + lower + numeric)

    # randomly shuffle the characters in the password
    random.shuffle(password_list)
    
    # return the password as a string
    return "".join(password_list)