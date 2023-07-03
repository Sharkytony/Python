def add( a, b):
    return a + b
def multiply(a, b):
    return a * b
print(add(5,6))



def Sign_in(username, new_username):
    username = username
    while new_username in username:
        print(f"Sorry username : \'@{new_username}\' is currently unaviable")
        new_username = input('Please enter a new username : ')
    else :
        print(f"Welcome @{new_username} you have successfully created your profile")
        username.append(new_username)
        print(username)

print(__name__)

if __name__ ==  "__main__" :
    usernames = ['Anthony', 'Amar007', 'Akbar123', 'Rajat', 'Rashid', 'Romeo455']
    new_username = input('Enter your username : ')
    Sign_in(usernames, new_username)
