# Ici on import les differrentes elements du librairie Tkinter dont on
# aura besoin. Pour rappel Tkinter est un Libfrairie Python qui nous permet
# de cree des interfaces graphiques.

from tkinter import * # Le etoile signifie Importer Tous.
from tkinter.font import Font # on import la librafie font qui nous permettra de Changer la
# la police de nos ecritures.
import random # La librairie random permet de choisir un nombre aleatoirement ou un nombre
# Parmis une liste de nombre.

# La ligne suivante represente l'initialisation de tous les variables dont on aura besoin.
y ,frame ,dt1 ,dt2 ,saut ,flag ,compteur , pos=236,1,-25,25,False,1,0,[600]

# La fonction suivante nous permet d'afficher a l'ecran le temps de jeu.
# elle manipule une variable compteur et ce conmpeur est incrementer par 1
# a chaque 150 millisecondes. Biensur en fonction de l'status du jeu.
def incremTime():
  "Incrémente le compteur à chaque seconde"
  global compteur,dt2
  compteur += 1
  if compteur<10:
    temp['text'] = "000"+str(compteur)
  elif compteur>=10 and compteur<100:
    temp['text'] = "00"+str(compteur)
  elif compteur>=100 and compteur<1000:
    temp['text'] = "0"+str(compteur)
    dt2=35
  else:
    temp['text'] = str(compteur)
    dt2=40
  if flag:
    fen.after(150,incremTime)

# La fonction corrir comme sont nom l'indique, permet au petit personnage de3 courrir
# Avant de fair courrir le personnage on teste d'abord si il n'est pas en train de sauter
# Si c'est le cas on charge deux images diefferent du meme personnage(leur nom : 1.png et 2.png.
# Ensuite on les echange tout les 150 millisecondes.
def courrir():
  global frame,photo,photo2,saut,y,flag
  photo = PhotoImage(file = str(frame)+".png")
  if saut==0:
    can.create_image(120,y,image=photo)
    frame += 1

    if frame>2:
      frame=1

    if flag:
      fen.after(150,courrir)
# La fontion sauter vpermet au personnage de sauter
#Grace a la variable y qui corespond a son ordonner.
def sauter():
  global saut,photo2,photo,y,dt1,flag,p2
  saut=1
  can.delete(photo)
  photo2 = PhotoImage(file = "2.png")
  if flag:
    y=y+dt1
    if y>215:
      y,dt1,saut=236,-25,False
      courrir()
    if y<130:
      y,dt1=140,25
  else:
    p2=can.create_image(120,y,image=photo2)
    return "Saut suspendu !"
  if saut:
    can.create_image(120,y,image=photo2)
    fen.after(150,sauter)

#Cette fonction permet de placer des le debut les diferrentes positions
#de l'obstacle
def position():
    for i in range(1,50):
      pos.append(pos[i-1]+random.choice([0,300,500]))

#Cette fontion a son tour a pour but de depalcer les obstacle vers le personnage
def obstacle():
  global y,saut,flag,obs,pos,dt2,b2,rep,p2
  obs = PhotoImage(file = "obs.png")
  for i in range(len(pos)):
    can.create_image(pos[i],210,image=obs)
    x1=pos[i]-50
    pos[i]-=dt2
    if (x1<122 and pos[i]>90 and y<=236 and y>165):
      stop()
      b2 = Button(can,text="Rejouer",command=replay,font=font,bg='#f0Eab7')
      rep = Label(can,text="Dommage, vous avez Perdu !",font=font)
      rep.place(relx=0.3,rely=0.2)
      b2.place(relx=0.44, rely=0.4)
  can.create_line(0,275,600,275,width=2)
  if flag:
    fen.after(150,obstacle)
#Cette foction permet de stoper le jeux.
def stop():
  global flag
  flag = 0

#Permet de rejouer une partie apres avoir perdu
def replay():
  global y,saut,frame,dt1,saut,flag,compteur,pos,rep,b2,p2
  y,saut,frame,flag,dt1,dt2,compteur,pos=236,0,1,1,-25,25,0,[600]
  can.delete(p2)
  b2.destroy()
  rep.destroy()
  jeu()

#C'est cette fonction qui permet au jeu de s'executer
#En ordonant au personnage de courrir et les obstacles de venir vers lui.
def jeu():
  position()
  courrir()
  obstacle()
  incremTime()

#Et enfin ici on cree la fenetre du jeu.
fen = Tk()
fen.title("Jeu de Google")
fondImage = PhotoImage(file="fondjeux2.png")
can = Canvas(fen,width=600, heigh=300)
font = Font(size=12,weight='bold')
b1 = Button(fen, text="Sauter", command=sauter, font=font, bg='#f0Eab7')
b3 = Button(fen, text="Pause", command=stop, font=font, bg='#f0Eab7')
temp = Label(fen, font=font, bg='#f0Eab7')
can.pack(side=TOP, padx=5, pady=5)
can.create_image(150, 100, image=fondImage)
b1.pack()
b3.pack()
temp.place(relx=0.9, rely=0.1)
jeu()
fen.mainloop()