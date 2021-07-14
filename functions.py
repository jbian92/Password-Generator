import random

def generator(data):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = data['length']
    lower = ""
    num_lower = 0
    upper = ""
    num_upper = 0

    # check if need uppercase/lowercase letters
    if data['upper'] and data['lower']:
        # randomly choose how many uppercase letters 
        num_upper = random.randint(1, length - 1)
        num_lower = length - num_upper
    elif data['upper']:
        num_upper = length
    elif data['lower']:
        num_lower = length
    
    for i in range(num_upper):
        upper += (random.choice(alphabet)).upper()
    
    for i in range(num_lower):
        lower += random.choice(alphabet)
    
    password_list = list(upper + lower)

    # randomly shuffle the characters in the password
    random.shuffle(password_list)
    
    # return the password as a string
    return "".join(password_list)