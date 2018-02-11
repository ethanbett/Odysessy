


def initilize_char():
    x = str(raw_input('Name your hero: '))
    characters['player'][0] = x
    user = char(characters['player'])
    return user
    
def initilize_room():
    room = room(rooms['beginning']]
    return room



def user_input(user,room):    
    while True:
        x = raw_input("What would you like to do? ")
        if x == 'help' or x == 'Help' or x == 'h' or x == 'H':
            user.help()
            
        elif x == 'equip' or x == 'Equip' or x == 'Equipment' or x == 'equipment':
            user.show_equip()
            
        elif x == 'name' or x == 'Name':
            user.show_name()
            
        elif x == 'health' or x == 'Health':
            user.show_health()
            
        elif x == 'Use Potion' or x == 'use potion' or x == 'Use potion':
            user.use_potion()
            
        
    



def ai():



def battle(user,monster):
    # all user input for battle and ai go here
