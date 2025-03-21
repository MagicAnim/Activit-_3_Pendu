# Importation de Flask et de render_template
from flask import Flask, render_template, session, redirect, request
# Importation du module os
import os
# Importation du module os
import random
# Import de la classe Pendu
from pendu import Pendu

# Création de l'instance de l'app Flask
app = Flask("Jeu du Pendu")
# Création d'une clef secrete
app.secret_key = os.urandom(24)

# Premier route -> première page affichée lorsqu'on arrive sur l'application web 
# Rénitialiser le jeu
@app.route("/")
def accueil():
    # Liste de mots possibles
    liste_de_mots = ["ordinateur", "clavier", "magic", "araignée", "souris", "fenêtre", "papier", "arbre", "fleur"]
    # On choisit un mot au hasard
    mot_a_deviner = random.choice(liste_de_mots)
    # On définit le nombre de vies
    vies = 6
    # On crée une instance du Pendu
    session["etat_du_jeu"] = Pendu.initialisation(mot_a_deviner ,vies)

    return redirect("/jeu")

# Route jeu -> affiche le jeu
@app.route("/jeu")
def jeu():
    # On affiche notre page html
    return render_template("index.html", etat_du_jeu = session["etat_du_jeu"])

# On crée un route pour l'entree d'utilisateur 
@app.route("/deviner", methods=["POST"])
def deviner():
    # On récupère l'entrée de l'utilisateur
    entree = request.form["entree"]
    # On met à jour le jeu grâce à notre la méthode deviner
    session["etat_du_jeu"] = Pendu.deviner(session["etat_du_jeu"], entree)
    # On redirige vers l'affichage du jeu
    return redirect("/jeu")

# Exécution
app.run(host="0.0.0.0", port = 81)