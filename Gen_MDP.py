# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:19:07 2023

@author: kerva
"""
import random

# Les différentes lettres possibles

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
Character = "&#{([-|_)@°]}=+£$¤%*?,.;/:§!*<>"
ACCENT_UPPER = "ÀÂÄÉÊÈËÌÎÏÒÖÔÙÜÛŸ"
accent_lower = "àâäéêèëìîïòöôùüûÿ"
Chiffre = "0123456789"

Liste_Character = [UPPER, lower, ACCENT_UPPER, accent_lower, Character, Chiffre]


def Generator_MDP (NBR_Character = 8, liste = Liste_Character):
    """
    Génère aléatoirement un mot de passe

    Parameters
    ----------
    NBR_Character : int, optional
        Nombre de caractère pour le mot de passe. The default is 8.
    liste : List, optional
        Liste des différentes lettres possibles pour former le mot de passe. The default is Liste_Character.

    Returns
    -------
    Mot_De_Pass : str
        Le mot de passe générer.

    """
    Mot_De_Pass = ""
    for i in range (NBR_Character) :
         Catégorie = liste[random.randint(0,len(liste))-1]
         Mot_De_Pass += Catégorie[random.randint(0,len(Catégorie))-1]
    return Mot_De_Pass
