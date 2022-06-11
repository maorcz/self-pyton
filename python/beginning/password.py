user = input('what\'s your name? ')
password = input('enter password please ')

len = len(password)
pass_sequence = '*'*len
print(f'hey {user}, your password {pass_sequence} is {len} letters long')