import network
import click

IP = "10.0.0.111"
PORT = 1111
z = "z : avancer"
s = "s : reculer"
x = "x : stop"
q = "q : touner a gauche"
d = "d : tourner a droite"
vp = "+ : plus vite"
vm = "- : moins vite"
a = "a : allumer ou eteindre les leds"

# 1 pour avancer ; 2 pour reculer ; 3 gauche ; 4 droite
print(z,s,x,q,d,vp,vm)
while True: 
    socket = network.newClientSocket()
    socket.connect((IP,PORT))

    print("Tape la lettre a afficher")
    lettre = click.getchar()
    
    socket.send(lettre.encode())