# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
from textwrap import wrap

user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(user, *args, **kwargs):
        if (user['valid']):
            #room for optional decorations 
            res = fn(user, *args, **kwargs)
            #room for optional decorations 
            return res
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)