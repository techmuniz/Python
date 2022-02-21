#Esse programa é feito para você poder jogar dados contra o computador.
#Se você acertar o número, você ganha

import sys


print ('Hey player! Wanna play a game?:\nYes\tNo')


while True:
    resp1 = str(input()).strip().upper()
    if resp1 in ("Yes"):
        print("Let\'s begin!")
        break

    elif resp1 in ("No"):
        print ("Little pussy")
        exit()
            

print ("Vamos começar")
        

    

#user_Name = str(input()).capitalize().strip()

#print (f"Muito bem {user_Name}, você gostaria de jogar o dado?")

#while True:
#    resposta = str(input()).upper().strip
#    if resposta in ("SIM", "")

