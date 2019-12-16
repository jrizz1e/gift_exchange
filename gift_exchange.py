# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:22:48 2019

@author: Jonathan
"""

#gift exchange

#enter everyone in gift exchange
names=[]
def enter_names():
    name = input('Please enter a name. Enter "done" if finished adding names: ')
    if name.upper() != 'DONE':
        names.append(name.upper())
        enter_names()
    else:
        return True


#set up giver:receiver pairs
import random
def draw_name():
    i=1
    while len(d.keys()) != len(names):
        giver = input('Please enter your name: ')
        giver=giver.upper()
        if giver not in names:
            return('Please enter a name in the gift exchange! ')
        else:
            options = [x for x in names if x != giver and x not in list(d.values())]
            receiver = random.choice(options)
            d[giver] = receiver
            print(giver + ' is getting a gift for '+ d[giver])
            if i>1:
                names.remove(giver)
                i+=1
            draw_name()
    return d

#init variables and run gift_exchange functionS
names=[]
d=dict()
def gift_exchange():
    a=enter_names()
    b=draw_name()
    print(d)
    return('Happy Holidays!')
    
gift_exchange()
    