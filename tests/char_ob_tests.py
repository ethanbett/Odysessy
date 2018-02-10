from nose.tools import *
from bin.char_object import *
from lib.char_list import *
from lib.greaves import * 
from lib.helmets import *
from lib.rings import*
from lib.suits import *
from lib.weapons import *




x = 'Zero'
characters['player'][0] = x
user = char(characters['player'])
user.show_name()
user.show_health()
user.show_equip()
user.show_stats()
