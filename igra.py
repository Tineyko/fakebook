# -*- coding: utf-8 -*-
import random
import re

def igra(): #funkcija za igro
    num = random.randint(0, 1000) #random funkcija
    print 'Pozdravljen v tej majhni igri imenovani "Ugani število"!'

    while True:    #omejitev vnosa na samo števila
        try:
            get_nmbr = int(raw_input("Prosim, vnesi število med 0 in 1000 : "))
            break
        except:
            print("SAMO ŠTEVILKE PROSIM!!! \n")

    stevec = 0
    while True: #omejitev vnosa na samo števila
        try:
            if get_nmbr > 1000 or get_nmbr < 0: #omejitev na [0,1000]
                print ("Ne pozabi, veljavna so samo števila med 0 in 1000 :)")
                get_nmbr = int(raw_input("Ponovno vnesi število: "))

            elif get_nmbr < num:
                print ("Iskano število je večje!")
                stevec += 1
                get_nmbr = int(raw_input("Ponovno vnesi število: "))

            elif get_nmbr > num:
                print ("Iskano število je manjše!")
                stevec += 1
                get_nmbr = int(raw_input("Ponovno vnesi število: "))

            elif get_nmbr == num:
                print ("Čestitke ugotovil/a si število %d :)" % num )
                print ("In sicer v %d poskusu :)) " % stevec)
                print ("čžš žšč šžč samo zato ker lahko\n") #izpis
                break
        except:
            print("SAMO ŠTEVILKE PROSIM!!! \n")

while True:
        game = str(raw_input("Bi se igral/a :)? y/n? "))
        if not re.match("^[a-z]*$", game):         #http://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths
            print("SAMO y ALI n PROSIM!!! \n")
        elif game == "y":
            igra()
        elif game == "n":
            print "papa :) !"
            break
        else:
            print "Vnesi samo y ali n pliiiiizzzz "
