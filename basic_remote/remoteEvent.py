import click
import spytank

z = "z : avancer"
s = "s : reculer"
x = "x : stop"
q = "q : touner a gauche"
d = "d : tourner a droite"
vp = "a : plus vite"
vm = "e : moins vite"
vitesse = 150
# 1 pour avancer ; 2 pour reculer ; 3 gauche ; 4 droite
direction = 1
print(z,s,x,q,d,vp,vm)

while True:
    lettre = click.getchar()
    if lettre == "z" : 
        spytank.avance(vitesse)
        direction = 1
    elif lettre == "s" :
        spytank.recule(vitesse)
        direction = 2
    elif lettre == "x" :
        spytank.stop()
    elif lettre == "q" :
        spytank.gauche(vitesse)
        direction = 3
    elif lettre == "d" :
        spytank.droite (vitesse)
        direction = 4
    elif lettre == "+" :
        if vitesse < 250 : 
            vitesse = vitesse + 10
            
        if direction == 1 :
            spytank.avance(vitesse)
        elif direction == 2 :
            spytank.recule(vitesse)
        elif direction == 3 :
            spytank.gauche(vitesse)
        elif direction == 4 :
            spytank.droite(vitesse)
    elif lettre == "-" : 
        if vitesse > 70 : 
            vitesse = vitesse - 10 

        if direction == 1 :
            spytank.avance(vitesse)
        elif direction == 2 :
            spytank.recule(vitesse)
        elif direction == 3 :
            spytank.gauche(vitesse)
        elif direction == 4 :
            spytank.droite(vitesse)