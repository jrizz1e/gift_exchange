# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:22:48 2019

@author: Jonathan
"""

#gift exchange
import smtplib

#enter everyone in gift exchange
def enter_names():
    name = input('Please enter a name. Enter "done" if finished adding names: ')
    email = input('Please enter the corresponding email address. Enter "done" if finished adding emails: ')
    if name.upper() != 'DONE':
        names.append(name.upper())
        emails.append(email)
        enter_names()
    else:
        return True


#set up giver:receiver pairs
def draw_names():
    for i in range(0, len(names)):
        giver = names[i]
        d[giver] = names[(i+1)%(len(names))]
        msg = '\n You are getting a gift for '+ d[giver]
        giver_email = emails[names.index(giver)]
        smtpObj.sendmail(organizer_email, giver_email, msg)
    return d

#init variables and run gift_exchange function
def gift_exchange():
    a=enter_names()
    b=draw_names()
    smtpObj.quit()
    return('Happy Holidays!')
    

names=[]
emails=[]
d=dict()
organizer_email = 'holidaygiftexchange2019@gmail.com'
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(organizer_email, '2019giftexchange')
gift_exchange()