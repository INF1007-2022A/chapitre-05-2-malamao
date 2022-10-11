#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	#sous total
	somme = 0
	for achat in data:
		somme += achat[INDEX_QUANTITY] * achat[INDEX_PRICE]

	#taxes
	taxes = somme * 0.15
	#total
	total = (somme + taxes)

	info_facture= [
		("SOUS TOTAL", somme),
		("TAXES     ", taxes),
		("TOTAL     ", total),
	]
	facture = name
	for info in info_facture:
		facture += "\n" + '{} {: >10.2f} $'.format(info[0], info[1])
	return facture


def format_number(number, num_decimal_digits):
	#séparer le nombre
	partie_decimale = abs(number)%1.0
	partie_entiere = str(int(abs(number)))

	#formater partie décimale
	chaine_dec = f"{partie_decimale:.{num_decimal_digits}f}"[1:]

	#formater partie entière
	liste_entier=[] #faire une liste avec la partie entière
	for chiffre in partie_entiere:
		liste_entier.append(chiffre)

	len_bloc1 = len(liste_entier)%3 #nombre de chiffre dans le premier bloc
	#mettre des espaces entre chaque bloc
	for i in range (len_bloc1, (len(liste_entier)+len(liste_entier)//2),4):
		liste_entier.insert(i, " ")
	#enlever les espaces de trop
	if liste_entier[0]==" ":
		del liste_entier[0]
	if liste_entier[len(liste_entier)-1]==" ":
		del liste_entier[len(liste_entier)-1]

	#transformer liste en str
	partie_entiere = ""
	for element in liste_entier:
		partie_entiere += element
	if number<0:
		nombre = "-"+partie_entiere + chaine_dec
	else:
		nombre = partie_entiere + chaine_dec

	return nombre

def get_triangle(num_rows):
	#largeur triangle
	element_bord = "+"
	element_triangle = "A"
	largeur_triangle = (num_rows * 2) - 1
	bordure = element_bord * (largeur_triangle + 2)

	#afficher triangle
	triangle = bordure
	for i in range(num_rows):
		triangle += '\n' + element_bord + (" " * (num_rows-(1+i)))+ element_triangle * (i*2+1) + (" " * (num_rows-(1+i))) + element_bord
	triangle += '\n' + bordure
	return triangle


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-123456789.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
