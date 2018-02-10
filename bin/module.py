


def initilize():
    x = str(raw_input('Name your hero: '))
    characters['player'][0] = x
    user = char(characters['player'])
    return user



def user_input(user):    
    while True:
        x = raw_input("What would you like to do? ")
        if x == 'help' or x == 'Help' or x == 'h' or x == 'H':
            user.help()
    



def ai():



def battle(user,monster):
    # all user input for battle and ai go here
