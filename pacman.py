#############################################
##   Initiations et importations modules   ##
#############################################

from tkinter import *
from tkinter.messagebox import *
from random import *
import pygame 
import pickle
import os

fen = Tk()
fen.geometry("860x810")
fen.title("Pacman")

#####################
##     Donnees     ##
#####################

grille_map = [
[2,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,3],
[1,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,1],
[1,0,9,0,9,0,9,0,0,0,9,0,9,0,9,0,1],
[1,0,5,6,4,0,5,6,7,6,4,0,5,6,4,0,1],
[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
[5,6,6,3,0,2,11,0,8,0,10,3,0,2,6,6,4],
[6,6,6,4,0,8,0,0,0,0,0,8,0,5,6,6,6],
[0,0,0,0,0,0,0,10,6,11,0,0,0,0,0,0,0],				# Permet de connaitre l'emplacement de chaque image 
[6,6,6,3,0,9,0,0,0,0,0,9,0,2,6,6,6],				# et donc d'afficher la map selon un paterne :				
[2,6,6,4,0,5,11,0,9,0,10,4,0,5,6,6,3],				# Chaque numero correspond a une image
[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
[1,0,2,6,3,0,2,6,12,6,3,0,2,6,3,0,1],
[1,0,8,0,8,0,8,0,0,0,8,0,8,0,8,0,1],
[1,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,1],
[5,6,6,6,6,6,6,6,12,6,6,6,6,6,6,6,4]
]

grille_pac_gomme = [ 								
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
[0,2,0,1,0,1,0,1,1,1,0,1,0,1,0,2,0],
[0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0],
[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
[0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0],				# Permet de connaitre l'emplacement de chaque pac-gommes :
[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],				# 0 --> Pas de pac-gomme
[0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0],				# 1 --> Une pac-gomme	
[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],				# 2 --> Une super pac-gomme
[0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0],
[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
[0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0],
[0,2,0,1,0,1,0,1,1,1,0,1,0,1,0,2,0],
[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

imgfond=PhotoImage(file="img/fond.gif")
img1=PhotoImage(file="img/1.gif")
img2=PhotoImage(file="img/2.gif")
img3=PhotoImage(file="img/3.gif")
img4=PhotoImage(file="img/4.gif")
img5=PhotoImage(file="img/5.gif")
img6=PhotoImage(file="img/6.gif")					# Importation des images de la map et 
img7=PhotoImage(file="img/7.gif")					# de l'image du menu et de l'onglet meilleurs scores
img8=PhotoImage(file="img/8.gif")			
img9=PhotoImage(file="img/9.gif")
img10=PhotoImage(file="img/10.gif")
img11=PhotoImage(file="img/11.gif")
img12=PhotoImage(file="img/12.gif")
img13=PhotoImage(file="img/13.gif")
img_nom=PhotoImage(file="img/img_nom.gif")
img_titre=PhotoImage(file="img/titre.gif")

img_pacman_droite_1=PhotoImage(file="img/pacman_droite_1.gif")
img_pacman_droite_2=PhotoImage(file="img/pacman_droite_2.gif")
img_pacman_bas_1=PhotoImage(file="img/pacman_bas_1.gif")
img_pacman_bas_2=PhotoImage(file="img/pacman_bas_2.gif")
img_pacman_gauche_1=PhotoImage(file="img/pacman_gauche_1.gif")
img_pacman_gauche_2=PhotoImage(file="img/pacman_gauche_2.gif")
img_pacman_haut_1=PhotoImage(file="img/pacman_haut_1.gif")
img_pacman_haut_2=PhotoImage(file="img/pacman_haut_2.gif")
img_fantome_orange_droite_1=PhotoImage(file="img/fantome_orange_droite_1.gif")
img_fantome_orange_droite_2=PhotoImage(file="img/fantome_orange_droite_2.gif")
img_fantome_orange_bas_1=PhotoImage(file="img/fantome_orange_bas_1.gif")
img_fantome_orange_bas_2=PhotoImage(file="img/fantome_orange_bas_2.gif")
img_fantome_orange_gauche_1=PhotoImage(file="img/fantome_orange_gauche_1.gif")
img_fantome_orange_gauche_2=PhotoImage(file="img/fantome_orange_gauche_2.gif")
img_fantome_orange_haut_1=PhotoImage(file="img/fantome_orange_haut_1.gif")
img_fantome_orange_haut_2=PhotoImage(file="img/fantome_orange_haut_2.gif")
img_fantome_bleu_droite_1=PhotoImage(file="img/fantome_bleu_droite_1.gif")
img_fantome_bleu_droite_2=PhotoImage(file="img/fantome_bleu_droite_2.gif")				# Importation des images du Pacman et de tous les fantomes
img_fantome_bleu_bas_1=PhotoImage(file="img/fantome_bleu_bas_1.gif")
img_fantome_bleu_bas_2=PhotoImage(file="img/fantome_bleu_bas_2.gif")
img_fantome_bleu_gauche_1=PhotoImage(file="img/fantome_bleu_gauche_1.gif")
img_fantome_bleu_gauche_2=PhotoImage(file="img/fantome_bleu_gauche_2.gif")
img_fantome_bleu_haut_1=PhotoImage(file="img/fantome_bleu_haut_1.gif")
img_fantome_bleu_haut_2=PhotoImage(file="img/fantome_bleu_haut_2.gif")
img_fantome_rose_droite_1=PhotoImage(file="img/fantome_rose_droite_1.gif")
img_fantome_rose_droite_2=PhotoImage(file="img/fantome_rose_droite_2.gif")
img_fantome_rose_bas_1=PhotoImage(file="img/fantome_rose_bas_1.gif")
img_fantome_rose_bas_2=PhotoImage(file="img/fantome_rose_bas_2.gif")
img_fantome_rose_gauche_1=PhotoImage(file="img/fantome_rose_gauche_1.gif")
img_fantome_rose_gauche_2=PhotoImage(file="img/fantome_rose_gauche_2.gif")
img_fantome_rose_haut_1=PhotoImage(file="img/fantome_rose_haut_1.gif")
img_fantome_rose_haut_2=PhotoImage(file="img/fantome_rose_haut_2.gif")
img_fantome_rouge_droite_1=PhotoImage(file="img/fantome_rouge_droite_1.gif")
img_fantome_rouge_droite_2=PhotoImage(file="img/fantome_rouge_droite_2.gif")
img_fantome_rouge_bas_1=PhotoImage(file="img/fantome_rouge_bas_1.gif")
img_fantome_rouge_bas_2=PhotoImage(file="img/fantome_rouge_bas_2.gif")
img_fantome_rouge_gauche_1=PhotoImage(file="img/fantome_rouge_gauche_1.gif")
img_fantome_rouge_gauche_2=PhotoImage(file="img/fantome_rouge_gauche_2.gif")
img_fantome_rouge_haut_1=PhotoImage(file="img/fantome_rouge_haut_1.gif")
img_fantome_rouge_haut_2=PhotoImage(file="img/fantome_rouge_haut_2.gif")

img_fantome_blanc_1=PhotoImage(file="img/fantome_blanc_1.gif")
img_fantome_blanc_2=PhotoImage(file="img/fantome_blanc_2.gif")
img_fantome_dark_1=PhotoImage(file="img/fantome_dark_1.gif")
img_fantome_dark_2=PhotoImage(file="img/fantome_dark_2.gif")
img_fantome_yeux_bas=PhotoImage(file="img/fantome_yeux_bas.gif")
img_fantome_yeux_haut=PhotoImage(file="img/fantome_yeux_haut.gif")
img_fantome_yeux_droit=PhotoImage(file="img/fantome_yeux_droit.gif")
img_fantome_yeux_gauche=PhotoImage(file="img/fantome_yeux_gauche.gif")

x_pacman = 427					
y_pacman = 327					
x_fantome_orange = 677			
y_fantome_orange = 627			
x_fantome_bleu = 177			# Initialisation des coordonnees de Pacman
y_fantome_bleu = 627			# et des fantomes
x_fantome_rose = 677			
y_fantome_rose = 127			
x_fantome_rouge = 177			
y_fantome_rouge = 127			

etat_partie = "jeu" 			# Variable contenant l'etat actuel du programme: "menu", "pause", "name_entry", "win", "lose", "meilleurs_scores", "credits", "options"

etat_fantomes = "invulnerable" 	# "vulnerable","invulnerable","fin_vulnerable"
etat_fantome_orange,etat_fantome_bleu,etat_fantome_rose,etat_fantome_rouge = "vivant","vivant","vivant","vivant"			# "vivant","mort"

touches_directions = ["Up","Left","Right","Down"] 		# Touches amenant le changement de direction de Pacamn
touche = ""

forme_pacman,forme_fantome_orange,forme_fantome_bleu,forme_fantome_rouge,forme_fantome_rose = 1,1,1,1,1			# Forme par defaut du Pacman et des fantomes
couleur_fantome_orange_vulnerable,couleur_fantome_rose_vulnerable,couleur_fantome_bleu_vulnerable,couleur_fantome_rouge_vulnerable = "dark","dark","dark","dark"
direction_fantome_orange,direction_fantome_bleu,direction_fantome_rose,direction_fantome_rouge = "Down","Down","Down","Down" # Direction par defaut des fantomes

score = 0
nbr_de_vies = 3						# Variables des parametres du jeu : score,vies,meilleurs scores et victoire
nbr_de_meilleurs_scores = 7
victoire = False
longueur_du_deplacement = 10

directions_tempo = []				# Permet de stocker toutes les directions possibles des fantomes

y_txt_credits16 = 2000				# Pour empecher un bug

pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.music.load("musiques/playlist.wav")	# Initier et loader la musique
pygame.mixer.music.set_volume(0.2)
son_win = pygame.mixer.Sound("musiques/win.wav")
son_lose = pygame.mixer.Sound("musiques/blaguenulle.wav")
son = False
son_etat = "active"


#####################
##    Fonctions    ##
#####################

def afficher_map():
	"""Permet d'afficher la map, le pacman, les fantomes et tout le layout"""
	global grille_map,grille_pac_gomme,vie_1,vie_2,vie_3,score_text,etat_partie,pacman,fantome_orange,fantome_rouge,fantome_bleu,fantome_rose
	for var1 in range(15):
		y_bloc = 28 +(var1*50)
		for var2 in range(17):
			x_bloc = 28 +(var2*50)
			if grille_map[var1][var2] == 0:
				C.create_image(x_bloc,y_bloc,image=imgfond)
			elif grille_map[var1][var2] == 1:
				C.create_image(x_bloc,y_bloc,image=img1)
			elif grille_map[var1][var2] == 2:
				C.create_image(x_bloc,y_bloc,image=img2)
			elif grille_map[var1][var2] == 3:
				C.create_image(x_bloc,y_bloc,image=img3)
			elif grille_map[var1][var2] == 4:
				C.create_image(x_bloc,y_bloc,image=img4)
			elif grille_map[var1][var2] == 5:
				C.create_image(x_bloc,y_bloc,image=img5)
			elif grille_map[var1][var2] == 6:
				C.create_image(x_bloc,y_bloc,image=img6)
			elif grille_map[var1][var2] == 7:
				C.create_image(x_bloc,y_bloc,image=img7)
			elif grille_map[var1][var2] == 8:
				C.create_image(x_bloc,y_bloc,image=img8)
			elif grille_map[var1][var2] == 9:
				C.create_image(x_bloc,y_bloc,image=img9)
			elif grille_map[var1][var2] == 10:
				C.create_image(x_bloc,y_bloc,image=img10)
			elif grille_map[var1][var2] == 11:
				C.create_image(x_bloc,y_bloc,image=img11)
			elif grille_map[var1][var2] == 12:
				C.create_image(x_bloc,y_bloc,image=img12)
			elif grille_map[var1][var2] == 13:
				C.create_image(x_bloc,y_bloc,image=img13)
			if grille_pac_gomme[var1][var2] == 1:
				C.create_oval(x_bloc-5,y_bloc-5,x_bloc+5,y_bloc+5,fill="pink")
			elif grille_pac_gomme[var1][var2] == 2:
				C.create_oval(x_bloc-10,y_bloc-10,x_bloc+10,y_bloc+10,fill="pink")
	score_text = Label(fen, text=score, bg="black", fg="white", font=("Arial",30))
	score_text.place(x=190,y=755)
	C.create_text(100,780,text="SCORE:", fill="white",font=("Arial",30))
	C.create_text(600,780,text="VIES:", fill="white",font=("Arial",30))
	vie_1 = C.create_image(680,780,image=img_pacman_droite_2)
	vie_2 = C.create_image(750,780,image=img_pacman_droite_2)
	vie_3 = C.create_image(820,780,image=img_pacman_droite_2)
	pacman = C.create_image(x_pacman,y_pacman,image=img_pacman_droite_2)
	fantome_orange = C.create_image(x_fantome_orange,y_fantome_orange,image=img_fantome_orange_droite_2)
	fantome_rose = C.create_image(x_fantome_rose,y_fantome_rose,image=img_fantome_rose_droite_2)
	fantome_rouge = C.create_image(x_fantome_rouge,y_fantome_rouge,image=img_fantome_rouge_droite_2)
	fantome_bleu = C.create_image(x_fantome_bleu,y_fantome_bleu,image=img_fantome_bleu_droite_2)
	etat_partie = "jeu"

def afficher_menu():
	"""Permet d'afficher le menu"""
	global txt_menu,txt_menu2,txt_menu3,txt_menu4,txt_menu5,img_menu,etat_partie,son
	pygame.mixer.music.stop()
	son = False
	etat_partie = "menu"
	txt_menu = C.create_text(415,385,text="Jouer", fill="yellow",font=("Terminal",30))
	txt_menu2 = C.create_text(425,455,text="Meilleurs scores", fill="red",font=("Terminal",30))
	txt_menu3 = C.create_text(415,525,text="Credits", fill="pink",font=("Terminal",30))
	txt_menu4 = C.create_text(415,595,text="Options", fill="blue",font=("Terminal",30))
	txt_menu5 = C.create_text(415,665,text="Ragequit", fill="orange",font=("Terminal",30))
	img_menu = C.create_image(440,200, image=img_titre)

def afficher_meilleurs_scores():
	"""Permet d'afficher l'onglet meilleurs scores"""
	global scores,nbr_de_meilleurs_scores,etat_partie
	etat_partie = "meilleurs_scores"
	x = 275
	y = 50
	scores = sorted(scores,reverse=True)
	taille_scores = len(scores)
	if taille_scores >= nbr_de_meilleurs_scores:
		nbr_de_meilleurs_scores = nbr_de_meilleurs_scores
	else:
		nbr_de_meilleurs_scores = taille_scores
	C.create_text(450,745,text="Retour", fill="white",font=("Terminal",30))
	for i in range(nbr_de_meilleurs_scores):
		nom_joueur = scores[i][1]
		score = scores[i][0]
		C.create_text(x,y,text=nom_joueur, fill="yellow",font=("Terminal",30))
		C.create_text(x+350,y,text=score, fill="red",font=("Terminal",30))
		y += 100

def afficher_credits():
	"""Permet d'afficher l'onglet credits"""
	global defilement,y_txt_credits,y_txt_credits2,y_txt_credits3,y_txt_credits4,y_txt_credits5,y_txt_credits6,y_txt_credits7,y_txt_credits8,y_txt_credits9,y_txt_credits10,y_txt_credits11,y_txt_credits12,y_txt_credits13,y_txt_credits14,y_txt_credits15,y_txt_credits16,txt_credits,txt_credits2,txt_credits3,txt_credits4,txt_credits5,txt_credits6,txt_credits7,txt_credits8,txt_credits9,txt_credits10,txt_credits11,txt_credits12,txt_credits13,txt_credits14,txt_credits15,txt_credits16,etat_partie
	y_txt_credits,y_txt_credits2,y_txt_credits3,y_txt_credits4,y_txt_credits5,y_txt_credits6,y_txt_credits7,y_txt_credits8,y_txt_credits9,y_txt_credits10,y_txt_credits11,y_txt_credits12,y_txt_credits13,y_txt_credits14,y_txt_credits15,y_txt_credits16 = 830,905,955,1005,1080,1155,1205,1280,1355,1430,1505,1555,1630,1705,1755,2000
	etat_partie = "credits"
	txt_credits = C.create_text(70,y_txt_credits,text="Realisateurs du projet Pacman:", fill="yellow",font=("Terminal",23),anchor="w")
	txt_credits2 = C.create_text(450,y_txt_credits2,text="Flambard Romain", fill="blue",font=("Terminal",23))
	txt_credits3 = C.create_text(454,y_txt_credits3,text="Pezet Jonathan", fill="orange",font=("Terminal",23))
	txt_credits4 = C.create_text(458,y_txt_credits4,text="Regereau Theo", fill="pink",font=("Terminal",23))
	txt_credits5 = C.create_text(70,y_txt_credits5,text="Conseilles par:", fill="yellow",font=("Terminal",23),anchor="w")
	txt_credits6 = C.create_text(446,y_txt_credits6,text="Deshogues Basile", fill="red",font=("Terminal",23))
	txt_credits7 = C.create_text(450,y_txt_credits7,text="Leconte Clement", fill="blue",font=("Terminal",23))
	txt_credits8 = C.create_text(70,y_txt_credits8,text="Images realisees par: ", fill="yellow",font=("Terminal",23),anchor="w")
	txt_credits9 = C.create_text(446,y_txt_credits9,text="Delaunay Esteban", fill="red",font=("Terminal",23))
	txt_credits10 = C.create_text(70,y_txt_credits10,text="Beta-testeurs :", fill="yellow",font=("Terminal",23),anchor="w")	
	txt_credits11 = C.create_text(446,y_txt_credits11,text="Tougeron Mikael", fill="red",font=("Terminal",23))
	txt_credits12 = C.create_text(446,y_txt_credits12,text="Seghrouchni Redwane", fill="orange",font=("Terminal",23))
	txt_credits13 = C.create_text(70,y_txt_credits13,text="Remerciements:", fill="yellow",font=("Terminal",23),anchor="w")
	txt_credits14 = C.create_text(446,y_txt_credits14,text="Lecouvey Nicolas", fill="pink",font=("Terminal",23))
	txt_credits15 = C.create_text(444,y_txt_credits15,text="Lequertier Alberic", fill="orange",font=("Terminal",23))
	txt_credits16 = C.create_text(415,y_txt_credits16,text="Retour", fill="blue",font=("Terminal",30))
	defilement ="On"
	defilement_credits()

def afficher_options():
	"""Permet d'afficher l'onglet options"""
	global etat_partie,pacman1,pacman2
	etat_partie = "options"
	C.create_text(50,50,text="Activer le son :", fill="white",font=("Terminal",23),anchor="w")
	C.create_text(550,50,text="Oui ", fill="blue",font=("Terminal",23),anchor="w")
	C.create_text(750,50,text="Non", fill="red",font=("Terminal",23),anchor="w")
	if son_etat == "active":
		pacman1 = C.create_image(505,50,image=img_pacman_droite_2)
	else:
		pacman2 = C.create_image(705,50,image=img_pacman_droite_2)
	C.create_text(350,745,text="Retour", fill="white",font=("Terminal",23),anchor="w")

def defilement_credits():
	"""Permet de faire défiler les credits à l'infini"""
	global defilement,y_txt_credits,y_txt_credits2,y_txt_credits3,y_txt_credits4,y_txt_credits5,y_txt_credits6,y_txt_credits7,y_txt_credits8,y_txt_credits9,y_txt_credits10,y_txt_credits11,y_txt_credits12,y_txt_credits13,y_txt_credits14,y_txt_credits15,y_txt_credits16,txt_credits,txt_credits2,txt_credits3,txt_credits4,txt_credits5,txt_credits6,txt_credits7,txt_credits8,txt_credits9,txt_credits10,txt_credits11,txt_credits12,txt_credits13,txt_credits14,txt_credits15,txt_credits16
	if defilement == "On":
		y_txt_credits,y_txt_credits2,y_txt_credits3,y_txt_credits4,y_txt_credits5,y_txt_credits6,y_txt_credits7,y_txt_credits8,y_txt_credits9,y_txt_credits10,y_txt_credits11,y_txt_credits12,y_txt_credits13,y_txt_credits14,y_txt_credits15,y_txt_credits16 = y_txt_credits-5,y_txt_credits2-5,y_txt_credits3-5,y_txt_credits4-5,y_txt_credits5-5,y_txt_credits6-5,y_txt_credits7-5,y_txt_credits8-5,y_txt_credits9-5,y_txt_credits10-5,y_txt_credits11-5,y_txt_credits12-5,y_txt_credits13-5,y_txt_credits14-5,y_txt_credits15-5,y_txt_credits16-5
		C.coords(txt_credits,70,y_txt_credits)
		C.coords(txt_credits2,450,y_txt_credits2)
		C.coords(txt_credits3,454,y_txt_credits3)
		C.coords(txt_credits4,458,y_txt_credits4)
		C.coords(txt_credits5,70,y_txt_credits5)
		C.coords(txt_credits6,446,y_txt_credits6)
		C.coords(txt_credits7,450,y_txt_credits7)
		C.coords(txt_credits8,70,y_txt_credits8)
		C.coords(txt_credits9,446,y_txt_credits9)
		C.coords(txt_credits10,70,y_txt_credits10)
		C.coords(txt_credits11,446,y_txt_credits11)
		C.coords(txt_credits12,446,y_txt_credits12)
		C.coords(txt_credits13,70,y_txt_credits13)
		C.coords(txt_credits14,446,y_txt_credits14)
		C.coords(txt_credits15,444,y_txt_credits15)
		C.coords(txt_credits16,415,y_txt_credits16)
		if y_txt_credits16 <= 0:
			y_txt_credits,y_txt_credits2,y_txt_credits3,y_txt_credits4,y_txt_credits5,y_txt_credits6,y_txt_credits7,y_txt_credits8,y_txt_credits9,y_txt_credits10,y_txt_credits11,y_txt_credits12,y_txt_credits13,y_txt_credits14,y_txt_credits15,y_txt_credits16 = 830,905,955,1005,1080,1155,1205,1280,1355,1430,1505,1555,1630,1705,1755,2000
		fen.after(50,defilement_credits)

def name_enter():
	"""Permet d'afficher l'endroit le joueur rentre son nom"""
	global nom_personne,touche,etat_partie,ligne_texte,txt_votre_nom,cadre_nom
	etat_partie = "name_entry"
	cadre_nom = C.create_image(198,198,image=img_nom,anchor="nw")
	txt_votre_nom = C.create_text(428,290,text="Votre nom :", fill="white",font=("Terminal",30))
	nom_personne = StringVar()
	nom_personne.set("joueur")
	ligne_texte = Entry(fen, textvariable=nom_personne, font=("Terminal",30), width=12, bd=0, bg="black", fg="white", justify="center")
	ligne_texte.place(x=245,y=420)

def recup_name():
	"""Permet de recuperer le nom du joueur"""
	global ligne_texte,nom_personne,touche,cadre_nom,txt_votre_nom,score
	nom_personne = ligne_texte.get()
	touche = ""
	C.delete(cadre_nom,txt_votre_nom)
	ligne_texte.place_forget()
	enregistrement_score(nom_personne,score)
	affichage_lose()

def actions_clavier(evt):
	"""Permet de filtrer les touches entrantes du clavier"""
	global touches_directions,touche,etat_partie
	t = evt.keysym
	if t == "space" and etat_partie == "jeu":
		touche = t
	elif t in touches_directions and traitement_collision(t,x_pacman,y_pacman) == True and (etat_partie == "jeu" or etat_partie == "pause"):
		touche = t
	elif t == "Return" and (etat_partie == "name_entry" or etat_partie == "win" or etat_partie == "lose"):
		touche = t
	elif t == "Escape" and (etat_partie == "lose" or etat_partie == "pause" or etat_partie == "credits"):
		touche = t

def cliquer(evt):
	"""Permet de cliquer sur les differents onglets lorsque l'on se trouve sur le menu"""
	global etat_partie,y_txt_credits13,defilement,pacman1,pacman2,son_etat
	x_clic = evt.x
	y_clic = evt.y
	if 335<= x_clic <=500 and 360<= y_clic <=405 and etat_partie == "menu":
		C.delete(ALL)
		afficher_map()
	elif 190<=x_clic<=660 and 430<= y_clic <=475 and etat_partie == "menu":
		C.delete(ALL)
		afficher_meilleurs_scores()
	elif 310<=x_clic<=525 and 500<= y_clic <=545 and etat_partie == "menu":
		C.delete(ALL)
		afficher_credits()
	elif 310<=x_clic<=525 and 570<= y_clic <=615 and etat_partie == "menu":
		C.delete(ALL)
		afficher_options()
	elif 290<=x_clic<=535 and 640<= y_clic <=685 and etat_partie == "menu":
		fen.quit()
		fen.destroy()
	elif 360<=x_clic<=540 and 720<= y_clic <=760 and etat_partie == "meilleurs_scores":
		C.delete(ALL)
		afficher_menu()
	elif 330<=x_clic<=500 and y_txt_credits16-20<=y_clic<=y_txt_credits16+20 and etat_partie == "credits":
		C.delete(ALL)
		defilement ="Off"
		afficher_menu()
	elif 550<=x_clic<=620 and 20<=y_clic<=70 and etat_partie == "options":
		if son_etat == "desactive":
			son_etat = "active"
			C.delete(pacman2)
			pacman1 = C.create_image(505,50,image=img_pacman_droite_2)
	elif 750<=x_clic<=825 and 30<=y_clic<=65 and etat_partie == "options":
		if son_etat == "active":
			son_etat = "desactive"
			C.delete(pacman1)
			pacman2 = C.create_image(705,50,image=img_pacman_droite_2)
	elif 350<=x_clic<=500 and 725<=y_clic<=760 and etat_partie == "options":
		C.delete(ALL)
		afficher_menu()

def traitement_touche():
	"""Permet de traiter les touches filtres pour y associer un role"""
	global touche,etat_partie,text_pause,x_pacman,y_pacman,pacman,score_text,txt_victoire,txt_victoire2,txt_defaite,txt_defaite2,txt_defaite3,defilement
	if touche == "Up":
		if etat_partie =="pause":
			C.delete(text_pause)
			etat_partie = "jeu"
		if etat_partie == "jeu":
			deplacement(pacman,"pacman","Up",x_pacman,y_pacman)
	if touche == "Down":
		if etat_partie =="pause":
			C.delete(text_pause)
			etat_partie = "jeu"
		if etat_partie == "jeu":
			deplacement(pacman,"pacman","Down",x_pacman,y_pacman)
	if touche == "Left":
		if etat_partie =="pause":
			C.delete(text_pause)
			etat_partie = "jeu"
		if etat_partie == "jeu":
			deplacement(pacman,"pacman","Left",x_pacman,y_pacman)
	if touche == "Right":
		if etat_partie =="pause":
			C.delete(text_pause)
			etat_partie = "jeu"
		if etat_partie == "jeu":
			deplacement(pacman,"pacman","Right",x_pacman,y_pacman)
	if touche == "space":
		if etat_partie == "jeu":
			etat_partie = "pause"
			text_pause = C.create_text(430,380,text="PAUSE", fill="white",font=("Terminal",50))
			touche = ""
	if touche == "Return" and etat_partie == "name_entry":
		recup_name()
	if touche == "Return" and etat_partie == "win":
		C.delete(txt_victoire,txt_victoire2)
		remise_zero_niveau(2)
		pygame.mixer.music.unpause()
	if touche == "Return" and etat_partie == "lose":
		C.delete(txt_defaite,txt_defaite2,txt_defaite3)
		remise_zero_niveau(3)
		pygame.mixer.music.unpause()
	if touche == "Escape" and (etat_partie == "pause" or etat_partie =="lose"):
		remise_zero_niveau(3)
		C.delete(ALL)
		score_text.place_forget()
		afficher_menu()
	if touche == "Escape" and etat_partie == "credits":
		touche = ""
		defilement = "Off"
		C.delete(ALL)
		afficher_menu()

def animation():
	"""Fonction recursive qui permet l'animation du pacman et des fantomes"""
	global etat_partie,touche,victoire
	if etat_partie != "menu":
		traitement_touche()
	if etat_partie == "jeu" and touche != "":
		traitement_fantomes()
	if etat_partie == "jeu":
		detection_win()
	fen.after(50, animation)

def traitement_fantomes():
	"""Permet de traiter l'action des fantomes a chaque tour"""
	global direction_fantome_orange,direction_fantome_bleu,direction_fantome_rose,direction_fantome_rouge
	direction_fantome_orange = generation_direction(direction_fantome_orange,x_fantome_orange,y_fantome_orange)
	deplacement(fantome_orange,"fantome_orange",direction_fantome_orange,x_fantome_orange,y_fantome_orange)
	direction_fantome_bleu = generation_direction(direction_fantome_bleu,x_fantome_bleu,y_fantome_bleu)
	deplacement(fantome_bleu,"fantome_bleu",direction_fantome_bleu,x_fantome_bleu,y_fantome_bleu)
	direction_fantome_rose = generation_direction(direction_fantome_rose,x_fantome_rose,y_fantome_rose)
	deplacement(fantome_rose,"fantome_rose",direction_fantome_rose,x_fantome_rose,y_fantome_rose)
	direction_fantome_rouge = generation_direction(direction_fantome_rouge,x_fantome_rouge,y_fantome_rouge)
	deplacement(fantome_rouge,"fantome_rouge",direction_fantome_rouge,x_fantome_rouge,y_fantome_rouge)

def generation_direction(direction_precedente,x_coords,y_coords):
	"""Permet de generer une direction aleatoire pour les fantomes"""
	global directions
	directions_tempo = []
	if traitement_collision("Up",x_coords,y_coords) == True:
		directions_tempo.append("Up")
	if traitement_collision("Down",x_coords,y_coords) == True:
		directions_tempo.append("Down")
	if traitement_collision("Left",x_coords,y_coords) == True:
		directions_tempo.append("Left")
	if traitement_collision("Right",x_coords,y_coords) == True:
		directions_tempo.append("Right")
	if direction_precedente == "Up" and "Down" in directions_tempo:
		directions_tempo.remove("Down")
		if (x_coords == 177 or x_coords == 677) and y_coords == 627:
			directions_tempo.append("Down")
	if direction_precedente == "Down" and "Up" in directions_tempo:
		directions_tempo.remove("Up")
		if (x_coords == 177 or x_coords == 677) and y_coords == 127:
			directions_tempo.append("Up")
	if direction_precedente == "Left" and "Right" in directions_tempo:
		directions_tempo.remove("Right")
	if direction_precedente == "Right" and "Left" in directions_tempo:
		directions_tempo.remove("Left")
	direction = choice(directions_tempo)
	if direction == "Right" and x_coords >= 810 and y_coords == 377:
		direction = "Left"
	if direction == "Left" and x_coords <= 20 and y_coords == 377:
		direction = "Right"
	return direction

def deplacement(entite,categorie,direction,x_coords,y_coords):
	"""Permet le deplacement de Pacman ou des fantomes"""
	global forme_pacman,forme_fantome_orange,forme_fantome_bleu,forme_fantome_rouge,forme_fantome_rose,x_pacman,y_pacman,score,x_fantome_orange,y_fantome_orange,x_fantome_rouge,y_fantome_rouge,x_fantome_rose,y_fantome_rose,x_fantome_bleu,y_fantome_bleu,etat_fantomes,couleur_fantome_orange_vulnerable,couleur_fantome_bleu_vulnerable,couleur_fantome_rose_vulnerable,couleur_fantome_rouge_vulnerable,etat_fantome_orange,etat_fantome_bleu,etat_fantome_rose,etat_fantome_rouge
	jouer_son()
	if direction == "Up":
		if traitement_collision("Up",x_coords,y_coords) == True:
			y_coords -= longueur_du_deplacement
			C.coords(entite,x_coords,y_coords)
	elif direction == "Down":
		if traitement_collision("Down",x_coords,y_coords) == True:
			y_coords += longueur_du_deplacement
			C.coords(entite,x_coords,y_coords)
	elif direction == "Left":
		if traitement_collision("Left",x_coords,y_coords) == True:
			if x_coords <= 8:
				x_coords = 857
			else:
				x_coords -= longueur_du_deplacement
			C.coords(entite,x_coords,y_coords)
	elif direction == "Right":
		if traitement_collision("Right",x_coords,y_coords) == True:
			x_coords += longueur_du_deplacement
			C.coords(entite,x_coords,y_coords)
		elif traitement_collision("Right",x_coords,y_coords) == "hors_map":
			if x_coords >= 850:
				x_coords = -3
			else:
				x_coords += longueur_du_deplacement
			C.coords(entite,x_coords,y_coords)
	if categorie == "pacman":
		forme_pacman = -forme_pacman
		x_pacman,y_pacman = x_coords,y_coords
		verif_collision_pac_gommes(x_coords,y_coords)
		verif_collision_fantomes_pacman(x_coords,y_coords)
		if direction == "Up" and forme_pacman == 1:
			C.itemconfig(pacman,image=img_pacman_haut_1)
		elif direction == "Up" and forme_pacman == -1:
			C.itemconfig(pacman,image=img_pacman_haut_2)
		elif direction == "Down" and forme_pacman == 1:
			C.itemconfig(pacman, image=img_pacman_bas_1)
		elif direction == "Down" and forme_pacman == -1:
			C.itemconfig(pacman, image=img_pacman_bas_2)
		elif direction == "Right" and forme_pacman == 1:
			C.itemconfig(pacman, image=img_pacman_droite_1)
		elif direction == "Right" and forme_pacman == -1:
			C.itemconfig(pacman, image=img_pacman_droite_2)
		elif direction == "Left" and forme_pacman == 1:
			C.itemconfig(pacman, image=img_pacman_gauche_1)
		elif direction == "Left" and forme_pacman == -1:
			C.itemconfig(pacman, image=img_pacman_gauche_2)
	elif categorie == "fantome_orange":
		forme_fantome_orange = -forme_fantome_orange
		if forme_fantome_orange == 1 and couleur_fantome_orange_vulnerable == "dark":
			couleur_fantome_orange_vulnerable = "blanc"
		elif forme_fantome_orange == 1 and couleur_fantome_orange_vulnerable == "blanc":
			couleur_fantome_orange_vulnerable = "dark"
		x_fantome_orange,y_fantome_orange = x_coords,y_coords
		if direction == "Up" and forme_fantome_orange == 1 and etat_fantomes == "invulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange,image=img_fantome_orange_haut_1)
		elif direction == "Up" and forme_fantome_orange == -1 and etat_fantomes == "invulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange,image=img_fantome_orange_haut_2)
		elif direction == "Down" and forme_fantome_orange == 1 and etat_fantomes == "invulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange, image=img_fantome_orange_bas_1)
		elif direction == "Down" and forme_fantome_orange == -1 and etat_fantomes == "invulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange, image=img_fantome_orange_bas_2)
		elif direction == "Right" and forme_fantome_orange == 1 and etat_fantomes == "invulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange, image=img_fantome_orange_droite_1)
		elif direction == "Right" and forme_fantome_orange == -1 and etat_fantomes == "invulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange, image=img_fantome_orange_droite_2)
		elif direction == "Left" and forme_fantome_orange == 1 and etat_fantomes == "invulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange, image=img_fantome_orange_gauche_1)
		elif direction == "Left" and forme_fantome_orange == -1 and etat_fantomes == "invulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange, image=img_fantome_orange_gauche_2)
		elif forme_fantome_orange == 1 and etat_fantomes == "vulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange,image=img_fantome_dark_1)
		elif forme_fantome_orange == -1 and etat_fantomes == "vulnerable" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange,image=img_fantome_dark_2)
		elif forme_fantome_orange == 1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_orange_vulnerable == "blanc" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange,image=img_fantome_blanc_1)
		elif forme_fantome_orange == -1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_orange_vulnerable == "blanc" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange,image=img_fantome_blanc_2)
		elif forme_fantome_orange == 1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_orange_vulnerable == "dark" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange,image=img_fantome_dark_1)
		elif forme_fantome_orange == -1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_orange_vulnerable == "dark" and etat_fantome_orange == "vivant":
			C.itemconfig(fantome_orange,image=img_fantome_dark_2)
		elif direction == "Up" and etat_fantome_orange == "mort":
			C.itemconfig(fantome_orange,image=img_fantome_yeux_haut)
		elif direction == "Down" and etat_fantome_orange == "mort":
			C.itemconfig(fantome_orange,image=img_fantome_yeux_bas)
		elif direction == "Left" and etat_fantome_orange == "mort":
			C.itemconfig(fantome_orange,image=img_fantome_yeux_gauche)
		elif direction == "Right" and etat_fantome_orange == "mort":
			C.itemconfig(fantome_orange,image=img_fantome_yeux_droit)
	elif categorie == "fantome_rouge":
		forme_fantome_rouge = -forme_fantome_rouge
		if forme_fantome_rouge == 1 and couleur_fantome_rouge_vulnerable == "dark":
			couleur_fantome_rouge_vulnerable = "blanc"
		elif forme_fantome_rouge == 1 and couleur_fantome_rouge_vulnerable == "blanc":
			couleur_fantome_rouge_vulnerable = "dark"
		x_fantome_rouge,y_fantome_rouge = x_coords,y_coords
		if direction == "Up" and forme_fantome_rouge == 1 and etat_fantomes == "invulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge,image=img_fantome_rouge_haut_1)
		elif direction == "Up" and forme_fantome_rouge == -1 and etat_fantomes == "invulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge,image=img_fantome_rouge_haut_2)
		elif direction == "Down" and forme_fantome_rouge == 1 and etat_fantomes == "invulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge, image=img_fantome_rouge_bas_1)
		elif direction == "Down" and forme_fantome_rouge == -1 and etat_fantomes == "invulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge, image=img_fantome_rouge_bas_2)
		elif direction == "Right" and forme_fantome_rouge == 1 and etat_fantomes == "invulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge, image=img_fantome_rouge_droite_1)
		elif direction == "Right" and forme_fantome_rouge == -1 and etat_fantomes == "invulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge, image=img_fantome_rouge_droite_2)
		elif direction == "Left" and forme_fantome_rouge == 1 and etat_fantomes == "invulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge, image=img_fantome_rouge_gauche_1)
		elif direction == "Left" and forme_fantome_rouge == -1 and etat_fantomes == "invulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge, image=img_fantome_rouge_gauche_2)
		elif forme_fantome_rouge == 1 and etat_fantomes == "vulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge,image=img_fantome_dark_1)
		elif forme_fantome_rouge == -1 and etat_fantomes == "vulnerable" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge,image=img_fantome_dark_2)
		elif forme_fantome_rouge == 1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_rouge_vulnerable == "blanc" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge,image=img_fantome_blanc_1)
		elif forme_fantome_rouge == -1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_rouge_vulnerable == "blanc" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge,image=img_fantome_blanc_2)
		elif forme_fantome_rouge == 1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_rouge_vulnerable == "dark" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge,image=img_fantome_dark_1)
		elif forme_fantome_rouge == -1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_rouge_vulnerable == "dark" and etat_fantome_rouge == "vivant":
			C.itemconfig(fantome_rouge,image=img_fantome_dark_2)
		elif direction == "Up" and etat_fantome_rouge == "mort":
			C.itemconfig(fantome_rouge,image=img_fantome_yeux_haut)
		elif direction == "Down" and etat_fantome_rouge == "mort":
			C.itemconfig(fantome_rouge,image=img_fantome_yeux_bas)
		elif direction == "Left" and etat_fantome_rouge == "mort":
			C.itemconfig(fantome_rouge,image=img_fantome_yeux_gauche)
		elif direction == "Right" and etat_fantome_rouge == "mort":
			C.itemconfig(fantome_rouge,image=img_fantome_yeux_droit)
	elif categorie == "fantome_rose":
		forme_fantome_rose = -forme_fantome_rose
		if forme_fantome_rose == 1 and couleur_fantome_rose_vulnerable == "dark":
			couleur_fantome_rose_vulnerable = "blanc"
		elif forme_fantome_rose == 1 and couleur_fantome_rose_vulnerable == "blanc":
			couleur_fantome_rose_vulnerable = "dark"
		x_fantome_rose,y_fantome_rose = x_coords,y_coords
		if direction == "Up" and forme_fantome_rose == 1 and etat_fantomes == "invulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose,image=img_fantome_rose_haut_1)
		elif direction == "Up" and forme_fantome_rose == -1 and etat_fantomes == "invulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose,image=img_fantome_rose_haut_2)
		elif direction == "Down" and forme_fantome_rose == 1 and etat_fantomes == "invulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose, image=img_fantome_rose_bas_1)
		elif direction == "Down" and forme_fantome_rose == -1 and etat_fantomes == "invulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose, image=img_fantome_rose_bas_2)
		elif direction == "Right" and forme_fantome_rose == 1 and etat_fantomes == "invulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose, image=img_fantome_rose_droite_1)
		elif direction == "Right" and forme_fantome_rose == -1 and etat_fantomes == "invulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose, image=img_fantome_rose_droite_2)
		elif direction == "Left" and forme_fantome_rose == 1 and etat_fantomes == "invulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose, image=img_fantome_rose_gauche_1)
		elif direction == "Left" and forme_fantome_rose == -1 and etat_fantomes == "invulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose, image=img_fantome_rose_gauche_2)
		elif forme_fantome_rose == 1 and etat_fantomes == "vulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose,image=img_fantome_dark_1)
		elif forme_fantome_rose == -1 and etat_fantomes == "vulnerable" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose,image=img_fantome_dark_2)
		elif forme_fantome_rose == 1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_rose_vulnerable == "blanc" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose,image=img_fantome_blanc_1)
		elif forme_fantome_rose == -1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_rose_vulnerable == "blanc" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose,image=img_fantome_blanc_2)
		elif forme_fantome_rose == 1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_rose_vulnerable == "dark" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose,image=img_fantome_dark_1)
		elif forme_fantome_rose == -1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_rose_vulnerable == "dark" and etat_fantome_rose == "vivant":
			C.itemconfig(fantome_rose,image=img_fantome_dark_2)
		elif direction == "Up" and etat_fantome_rose == "mort":
			C.itemconfig(fantome_rose,image=img_fantome_yeux_haut)
		elif direction == "Down" and etat_fantome_rose == "mort":
			C.itemconfig(fantome_rose,image=img_fantome_yeux_bas)
		elif direction == "Left" and etat_fantome_rose == "mort":
			C.itemconfig(fantome_rose,image=img_fantome_yeux_gauche)
		elif direction == "Right" and etat_fantome_rose == "mort":
			C.itemconfig(fantome_rose,image=img_fantome_yeux_droit)
	elif categorie == "fantome_bleu":
		forme_fantome_bleu = -forme_fantome_bleu
		if forme_fantome_bleu == 1 and couleur_fantome_bleu_vulnerable == "dark":
			couleur_fantome_bleu_vulnerable = "blanc"
		elif forme_fantome_bleu == 1 and couleur_fantome_bleu_vulnerable == "blanc":
			couleur_fantome_bleu_vulnerable = "dark"
		x_fantome_bleu,y_fantome_bleu = x_coords,y_coords
		if direction == "Up" and forme_fantome_bleu == 1 and etat_fantomes == "invulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu,image=img_fantome_bleu_haut_1)
		elif direction == "Up" and forme_fantome_bleu == -1 and etat_fantomes == "invulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu,image=img_fantome_bleu_haut_2)
		elif direction == "Down" and forme_fantome_bleu == 1 and etat_fantomes == "invulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu, image=img_fantome_bleu_bas_1)
		elif direction == "Down" and forme_fantome_bleu == -1 and etat_fantomes == "invulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu, image=img_fantome_bleu_bas_2)
		elif direction == "Right" and forme_fantome_bleu == 1 and etat_fantomes == "invulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu, image=img_fantome_bleu_droite_1)
		elif direction == "Right" and forme_fantome_bleu == -1 and etat_fantomes == "invulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu, image=img_fantome_bleu_droite_2)
		elif direction == "Left" and forme_fantome_bleu == 1 and etat_fantomes == "invulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu, image=img_fantome_bleu_gauche_1)
		elif direction == "Left" and forme_fantome_bleu == -1 and etat_fantomes == "invulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu, image=img_fantome_bleu_gauche_2)
		elif forme_fantome_bleu == 1 and etat_fantomes == "vulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu,image=img_fantome_dark_1)
		elif forme_fantome_bleu == -1 and etat_fantomes == "vulnerable" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu,image=img_fantome_dark_2)
		elif forme_fantome_bleu == 1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_bleu_vulnerable == "blanc" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu,image=img_fantome_blanc_1)
		elif forme_fantome_bleu == -1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_bleu_vulnerable == "blanc" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu,image=img_fantome_blanc_2)
		elif forme_fantome_bleu == 1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_bleu_vulnerable == "dark" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu,image=img_fantome_dark_1)
		elif forme_fantome_bleu == -1 and etat_fantomes == "fin_vulnerable" and couleur_fantome_bleu_vulnerable == "dark" and etat_fantome_bleu == "vivant":
			C.itemconfig(fantome_bleu,image=img_fantome_dark_2)
		elif direction == "Up" and etat_fantome_bleu == "mort":
			C.itemconfig(fantome_bleu,image=img_fantome_yeux_haut)
		elif direction == "Down" and etat_fantome_bleu == "mort":
			C.itemconfig(fantome_bleu,image=img_fantome_yeux_bas)
		elif direction == "Left" and etat_fantome_bleu == "mort":
			C.itemconfig(fantome_bleu,image=img_fantome_yeux_gauche)
		elif direction == "Right" and etat_fantome_bleu == "mort":
			C.itemconfig(fantome_bleu,image=img_fantome_yeux_droit)

def traitement_collision(direction,x_coords,y_coords):
	"""Permet d'interpreter, selon la position et la direction du Pacman ou des fantomes, les endroits ou il faut tester la collision'"""
	global nbr_de_bloc
	nbr_de_bloc = 0
	if direction == "Up":
		x_test_1,y_test_1 = x_coords+24,y_coords-26
		x_test_2,y_test_2 = x_coords-24,y_coords-26
	elif direction == "Down":
		x_test_1,y_test_1 = x_coords+24,y_coords+26
		x_test_2,y_test_2 = x_coords-24,y_coords+26
	elif direction == "Left":
		x_test_1,y_test_1 = x_coords-26,y_coords+24
		x_test_2,y_test_2 = x_coords-26,y_coords-24
	elif direction == "Right":
		x_test_1,y_test_1 = x_coords+26,y_coords+24
		x_test_2,y_test_2 = x_coords+26,y_coords-24
	if verif_collision_murs(x_test_1,y_test_1) == True and verif_collision_murs(x_test_2,y_test_2) == True:
		return True
	elif verif_collision_murs(x_test_1,y_test_1) == "hors_map" or verif_collision_murs(x_test_2,y_test_2) == "hors_map":
		return "hors_map"
	else:
		return False

def verif_collision_murs(x_coords,y_coords):
	"""Permet de verifier la collision avec les murs"""
	global grille_map
	x_bloc = x_coords % 100
	y_bloc = y_coords % 100
	if 3 <= x_bloc < 53:
		x_bloc = x_coords - x_bloc + 28
	elif x_bloc < 3:
		x_bloc = x_coords - x_bloc - 22
	elif x_bloc >= 53:
		x_bloc = x_coords - x_bloc + 78
	else:
		x_bloc = x_coords
	if 3 <= y_bloc < 53:
		y_bloc = y_coords - y_bloc + 28
	elif y_bloc < 3:
		y_bloc = y_coords - y_bloc - 22
	elif y_bloc >= 53:
		y_bloc = y_coords - y_bloc + 78
	else:
		y_bloc = y_coords
	var2 = int((x_bloc - 28)/50)
	var1 = int((y_bloc - 28)/50)
	try:
		id_bloc = grille_map[var1][var2]
		if id_bloc != 0:
			return False
		else:
			return True
	except IndexError:
		return "hors_map"

def verif_collision_pac_gommes(x_coords,y_coords):
	"""Permet de verifier la collision avec les pac_gommes"""
	global grille_pac_gomme,score,pacman,score_text,etat_fantomes
	x_bille = x_coords % 100
	y_bille = y_coords % 100
	if 3 <= x_bille < 53:
		x_bille = x_coords - x_bille + 28
	elif x_bille < 3:
		x_bille = x_coords - x_bille - 22
	elif x_bille >= 53:
		x_bille = x_coords - x_bille + 78
	else:
		x_bille = x_coords
	if 3 <= y_bille < 53:
		y_bille = y_coords - y_bille + 28
	elif y_bille < 3:
		y_bille = y_coords - y_bille - 22
	elif y_bille >= 53:
		y_bille = y_coords - y_bille + 78
	else:
		y_bille = y_coords
	var2 = int((x_bille - 28)/50)
	var1 = int((y_bille - 28)/50)
	try:
		id_bonus = grille_pac_gomme[var1][var2]
		if x_coords + 1 == x_bille and y_coords + 1 == y_bille:
			if id_bonus == 1:
				C.create_image(x_coords,y_coords,image=imgfond)
				C.tag_raise(pacman)
				C.tag_raise(fantome_orange)
				C.tag_raise(fantome_bleu)
				C.tag_raise(fantome_rose)
				C.tag_raise(fantome_rouge)
				score += 10
				score_text.place_forget()
				score_text = Label(fen, text=score, bg="black", fg="white", font=("Arial",30))
				score_text.place(x=190,y=755)
				grille_pac_gomme[var1][var2] = 0
			elif id_bonus == 2:
				C.create_image(x_coords,y_coords,image=imgfond)
				C.tag_raise(pacman)
				C.tag_raise(fantome_orange)
				C.tag_raise(fantome_bleu)
				C.tag_raise(fantome_rose)
				C.tag_raise(fantome_rouge)
				score += 50
				score_text.place_forget()
				score_text = Label(fen, text=score, bg="black", fg="white", font=("Arial",30))
				score_text.place(x=190,y=755)
				etat_fantomes = "vulnerable"
				timer(4500,animation_fin_vulnerabilite_fantomes)
				grille_pac_gomme[var1][var2] = 0
	except IndexError:
		return False

def verif_collision_fantomes_pacman(x_coords,y_coords):
	"""Permet de verifier la collision du Pacman avec les fantomes"""
	global x_fantome_orange,y_fantome_orange,x_fantome_bleu,y_fantome_bleu,x_fantome_rose,y_fantome_rose,x_fantome_rouge,y_fantome_rouge,nbr_de_vies,son_etat,etat_fantomes,etat_fantome_orange,etat_fantome_bleu,etat_fantome_rose,etat_fantome_rouge
	list_coords_x_pacman,list_coords_y_pacman,list_coords_x_fantome_orange,list_coords_y_fantome_orange,list_coords_x_fantome_rose,list_coords_y_fantome_rose,list_coords_x_fantome_bleu,list_coords_y_fantome_bleu,list_coords_x_fantome_rouge,list_coords_y_fantome_rouge = [],[],[],[],[],[],[],[],[],[]
	correspondance_y_rouge,correspondance_y_rose,correspondance_y_bleu,correspondance_y_orange,correspondance_x_rouge,correspondance_x_rose,correspondance_x_bleu,correspondance_x_orange= False,False,False,False,False,False,False,False
	collision_pacman_fantome_orange,collision_pacman_fantome_rouge,collision_pacman_fantome_rose,collision_pacman_fantome_bleu = False,False,False,False
	for i in range(-15,15,1):
		list_coords_x_pacman.append(x_coords+i)
		list_coords_y_pacman.append(y_coords+i)
		list_coords_x_fantome_orange.append(x_fantome_orange+i)
		list_coords_y_fantome_orange.append(y_fantome_orange+i)
		list_coords_x_fantome_rose.append(x_fantome_rose+i)
		list_coords_y_fantome_rose.append(y_fantome_rose+i)
		list_coords_x_fantome_bleu.append(x_fantome_bleu+i)
		list_coords_y_fantome_bleu.append(y_fantome_bleu+i)
		list_coords_x_fantome_rouge.append(x_fantome_rouge+i)
		list_coords_y_fantome_rouge.append(y_fantome_rouge+i)
	for e in list_coords_x_pacman:
		if e in list_coords_x_fantome_rouge:
			correspondance_x_rouge = True
		if e in list_coords_x_fantome_rose:
			correspondance_x_rose = True
		if e in list_coords_x_fantome_bleu:
			correspondance_x_bleu = True
		if e in list_coords_x_fantome_orange:
			correspondance_x_orange = True
	for e in list_coords_y_pacman:
		if e in list_coords_y_fantome_rouge:
			correspondance_y_rouge = True
		if e in list_coords_y_fantome_rose:
			correspondance_y_rose = True
		if e in list_coords_y_fantome_bleu:
			correspondance_y_bleu = True
		if e in list_coords_y_fantome_orange:
			correspondance_y_orange = True
	if correspondance_x_orange == True and correspondance_y_orange == True:
		collision_pacman_fantome_orange = True
	if correspondance_x_rose == True and correspondance_y_rose == True:
		collision_pacman_fantome_rose = True
	if correspondance_x_bleu == True and correspondance_y_bleu == True:
		collision_pacman_fantome_bleu = True
	if correspondance_x_rouge == True and correspondance_y_rouge == True:
		collision_pacman_fantome_rouge = True
	if ((collision_pacman_fantome_orange == True and etat_fantome_orange == "vivant") or (collision_pacman_fantome_rose == True and etat_fantome_rose == "vivant") or (collision_pacman_fantome_bleu == True and etat_fantome_bleu == "vivant") or (collision_pacman_fantome_rouge == True and etat_fantome_rouge == "vivant")) and etat_fantomes == "invulnerable":
		nbr_de_vies -= 1
		if nbr_de_vies == 2:
			C.delete(vie_3)
			remise_zero_niveau(1)
		elif nbr_de_vies == 1:
			C.delete(vie_2)
			remise_zero_niveau(1)
		elif nbr_de_vies == 0:
			C.delete(vie_1)
			if son_etat == "active":
				pygame.mixer.music.pause()
				son_lose.play()
			name_enter()
	if collision_pacman_fantome_orange == True and etat_fantomes != "invulnerable":
		etat_fantome_orange = "mort"
		timer(6000,fin_mort_orange)
	if collision_pacman_fantome_rose == True and etat_fantomes != "invulnerable":
		etat_fantome_rose = "mort"
		timer(6000,fin_mort_rose)
	if collision_pacman_fantome_bleu == True and etat_fantomes != "invulnerable":
		etat_fantome_bleu = "mort"
		timer(6000,fin_mort_bleu)
	if collision_pacman_fantome_rouge == True and etat_fantomes != "invulnerable":
		etat_fantome_rouge = "mort"
		timer(6000,fin_mort_rouge)

def remise_zero_niveau(categorie): 
	"""Permet de remettre le jeu a zero. Il existe 3 etats de remise à niveau: 1 : remise fantomes et pacman place ; 2 : remise bonus ; 3 : remise vies"""
	global x_pacman,y_pacman,x_fantome_orange,y_fantome_orange,x_fantome_bleu,y_fantome_bleu,x_fantome_rose,y_fantome_rose,x_fantome_rouge,y_fantome_rouge,grille_pac_gomme,pacman,fantome_orange,fantome_rose,fantome_bleu,fantome_rouge,touche,forme_pacman,forme_fantome_orange,forme_fantome_bleu,forme_fantome_rouge,forme_fantome_rose,directions_tempo,direction_fantome_orange,direction_fantome_bleu,direction_fantome_rose,direction_fantome_rouge,etat_partie,bonus,nbr_de_vies,vie_1,vie_2,vie_3,score,score_text,etat_fantomes,etat_fantome_orange,etat_fantome_bleu,etat_fantome_rose,etat_fantome_rouge
	x_pacman = 427
	y_pacman = 327
	x_fantome_orange = 677
	y_fantome_orange = 627
	x_fantome_bleu = 177
	y_fantome_bleu = 627
	x_fantome_rose = 677
	y_fantome_rose = 127
	x_fantome_rouge = 177
	y_fantome_rouge = 127
	touche = ""
	forme_pacman,forme_fantome_orange,forme_fantome_bleu,forme_fantome_rouge,forme_fantome_rose = 1,1,1,1,1
	directions_tempo = []
	direction_fantome_orange,direction_fantome_bleu,direction_fantome_rose,direction_fantome_rouge = "Down","Down","Down","Down"
	if categorie >= 2:
		grille_pac_gomme = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],[0,2,0,1,0,1,0,1,1,1,0,1,0,1,0,2,0],[0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0],[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],[0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0],[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],[0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0],[0,2,0,1,0,1,0,1,1,1,0,1,0,1,0,2,0],[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
		for var1 in range(15):
			y_bloc = 28 +(var1*50)
			for var2 in range(17):
				x_bloc = 28 +(var2*50)
				if grille_pac_gomme[var1][var2] == 1:
					C.create_oval(x_bloc-5,y_bloc-5,x_bloc+5,y_bloc+5,fill="pink")
				elif grille_pac_gomme[var1][var2] == 2:
					C.create_oval(x_bloc-10,y_bloc-10,x_bloc+10,y_bloc+10,fill="pink")
	if categorie >= 3:
		etat_fantomes = "invulnerable"
		etat_fantome_orange,etat_fantome_bleu,etat_fantome_rose,etat_fantome_rouge = "vivant","vivant","vivant","vivant"
		nbr_de_vies = 3
		vie_1 = C.create_image(680,780,image=img_pacman_droite_2)
		vie_2 = C.create_image(750,780,image=img_pacman_droite_2)
		vie_3 = C.create_image(820,780,image=img_pacman_droite_2)
		score = 0
		score_text.place_forget()
		score_text = Label(fen, text=score, bg="black", fg="white", font=("Arial",30))
		score_text.place(x=190,y=755)
	C.delete(pacman)
	C.delete(fantome_orange)
	C.delete(fantome_rose)
	C.delete(fantome_rouge)
	C.delete(fantome_bleu)
	pacman = C.create_image(x_pacman,y_pacman,image=img_pacman_droite_2)
	fantome_orange = C.create_image(x_fantome_orange,y_fantome_orange,image=img_fantome_orange_droite_2)
	fantome_rose = C.create_image(x_fantome_rose,y_fantome_rose,image=img_fantome_rose_droite_2)
	fantome_rouge = C.create_image(x_fantome_rouge,y_fantome_rouge,image=img_fantome_rouge_droite_2)
	fantome_bleu = C.create_image(x_fantome_bleu,y_fantome_bleu,image=img_fantome_bleu_droite_2)
	etat_partie = "jeu"

def timer(duree,fonction):
	"""Timer d'une duree determine"""
	fen.after(duree,fonction)

def animation_fin_vulnerabilite_fantomes():
	global etat_fantomes
	etat_fantomes = "fin_vulnerable"
	fen.after(1500,fin_vulnerabilite)

def fin_vulnerabilite():
	global etat_fantomes
	etat_fantomes = "invulnerable"

def fin_mort_rouge():
	global etat_fantome_rouge
	etat_fantome_rouge = "vivant"

def fin_mort_rose():
	global etat_fantome_rose
	etat_fantome_rose = "vivant"

def fin_mort_bleu():
	global etat_fantome_bleu
	etat_fantome_bleu = "vivant"

def fin_mort_orange():
	global etat_fantome_orange
	etat_fantome_orange = "vivant"

def detection_win():
	"""Permet de detecter la victoire du joueur lorsqu'il n'y a plus de pac-gommes"""
	global grille_pac_gomme,txt_victoire,txt_victoire2,etat_partie,son_etat
	win = True
	for i in range(15):
		for j in range(17):
			if grille_pac_gomme[i][j] != 0:
				win = False 
	if win == True:
		etat_partie = "win"
		txt_victoire = C.create_text(430,380,text="VICTOIRE !", fill="white",font=("Terminal",50))
		txt_victoire2 = C.create_text(430,450,text="Appuyez sur Entree pour continuer", fill="white",font=("Terminal",25))
		pygame.mixer.music.pause()
		if son_etat == "active":
			son_win.play()

def affichage_lose():
	"""Permet d'afficher les messages de la defaite"""
	global etat_partie,txt_defaite,txt_defaite2,txt_defaite3
	etat_partie = "lose"
	txt_defaite = C.create_text(435,380,text="GAME OVER !", fill="white",font=("Terminal",50))
	txt_defaite2 = C.create_text(430,480,text="Appuyez sur Entree pour refaire une game", fill="white",font=("Arial",23))
	txt_defaite3 = C.create_text(430,520,text="Appuyez sur Echap pour retourner au menu", fill="white",font=("Arial",23))

def enregistrement_score(nom_joueur,score):
	"""Permet d'enregistrer les scores"""
	global scores
	scores.append((score,nom_joueur))
	with open("scores.txt","wb") as e:
		mon_pickler = pickle.Pickler(e)
		mon_pickler.dump(scores)

def recup_scores():
	"""Permet de recuperer les scores"""
	global scores
	if os.path.exists("scores.txt"):
		with open("scores.txt","rb") as r:
			mon_depickler = pickle.Unpickler(r)
			scores = mon_depickler.load()
	else:
		scores = []

def jouer_son():
	"""Permet de jouer le son"""
	global son,etat_partie,son_etat
	if etat_partie == "jeu" and son == False and son_etat == "active":
		son = True
		pygame.mixer.music.play(-1)

#####################
##    Programme    ##
#####################

C=Canvas(fen,bg="black",width=854,height=804)
C.grid(row=0,column=0)

recup_scores()
afficher_menu()

fen.bind_all('<KeyPress>',actions_clavier)
fen.bind_all('<ButtonPress-1>',cliquer)

animation()

fen.mainloop()