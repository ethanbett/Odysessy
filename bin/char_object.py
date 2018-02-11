from lib.char_list import *
from lib.greaves import * 
from lib.helmets import *
from lib.rings import*
from lib.suits import *
from lib.weapons import *



class char:
    def __init__(self, user):
        self.name = user[0]
        self.health = user[1]
        self.temp_health = self.health
        self.weapon = weapons[user[2]]
        self.helmet = helmets[user[3]]
        self.suit = suits[user[4]]
        self.greaves = greaves[user[5]]
        self.ring1 = rings[user[6]]
        self.ring2 = rings[user[7]]
        self.potion = user[8] 


    def show_name(self):
        print self.name

    def show_health(self):
        print 'Health: ',self.temp_health,'/',self.health

    def show_equip(self):
        print 'Weapon: ',self.weapon[0]
        print 'Helmet: ',self.helmet[0]
        print 'Suit', self.suit[0]
        print 'Greaves: ',self.greaves[0]
        print 'Ring 1: ',self.ring1[0]
        print 'Ring 2: ',self.ring2[0]
        print self.potion
        
    def show_stats(self):
        print "Attack: ", self.weapon[1] + self.ring1[1] + self.ring2[1]
        print 'Defense: ', self.helmet[1] + self.suit[1] + self.greaves[1]

    def use_potion(self):
        if potion > 0:
            self.temp_health = self.health
            print 'Health: ',self.temp_health,'/',self.health
            potion = potion - 1
            print 'Potion: ',self.potion
        else:
            print "You don't have anymore!"




if __name__ == '__main__':
    x = str(raw_input("Please enter name: "))
    characters['player'][0] = x
    user = char(characters['player'])
    user.show_name()
    user.show_health()
    user.show_equip()
    user.show_stats()

