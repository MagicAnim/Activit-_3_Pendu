# On importe la fonction unidecode pour éviter les soucis d'accents et de majuscule
from unidecode import unidecode 

# Création de la classe Pendu = tous les attributs et méthodes nécessaires pour le jeu
class Pendu : 
    # On crée les attributs de base pour le jeu
    vies = 0
    mot_a_deviner = ""
    mot_a_afficher = ""
    # Une liste des lettres que l'utilisateur a tenté
    lettres_proposees = []

    ##################################################
    #    1e METHODE : Initialisation du jeu          #
    ##################################################
    def initialisation(mot_a_deviner , vies):
        mot_a_deviner = unidecode(mot_a_deviner).upper()

        data_etat_du_jeu = {
            "vies" : vies,
            "mot_a_deviner" : mot_a_deviner,
            "mot_a_afficher" : "-" * len(mot_a_deviner),
            "defaite" : False,
            "victoire" : False,
            "entree" : "",
            "lettres_proposees" : []
        }
        
        return data_etat_du_jeu
    

    ##################################################
    #              2e METHODE : Deviner              #
    ##################################################
    # On crée notre méthode deviner qui va permettre de réaliser le fonctionnement général du jeu
    def deviner(etat_du_jeu, entree):
        # On récupère toutes nos variables pour les mettre à jour
        global vies 
        global mot_a_deviner
        global mot_a_afficher 
        global lettres_proposees

        # On met à jour toutes les variables de notre classe
        vies = etat_du_jeu["vies"]
        mot_a_deviner = etat_du_jeu["mot_a_deviner"]
        mot_a_afficher = etat_du_jeu["mot_a_afficher"]
        lettres_proposees =etat_du_jeu["lettres_proposees"]

        # Donnéees retournées par deviner()
        data_retour = {
            "victoire" : False,
            "defaite" : False,
            "derniere_entree" : ""
        }

        # On vérifie si l'utilisateur a tenté un mot ou une lettre
        if len(entree) == 1 :
            message = Pendu.deviner_lettre(entree)
        else: 
            message = Pendu.deviner_mot(entree)

        # ...




    ##################################################
    #          3e METHODE : Deviner Lettre           #
    ##################################################
    def deviner_lettre(entree):
        global lettres_proposees
        global mot_a_deviner
        global vies
        
        # On vérifie si la lettre a déjà été proposée
        if entree in lettres_proposees:
            return "Tu as déjà proposé cette lettre !!!"
        # Sinon on l'ajoute à liste des lettres proposées
        # On vérifie si elle appartient au mot
        # Si oui on actualise le mot à afficher
        # Sinon on enlève une vie
        else:
            lettres_proposees.append(entree)
            if entree in mot_a_deviner:
                Pendu.actualisation_mot_a_afficher(entree)
                return "Bonne pioche, le mot contient cette lettre !!!"
            else:
                vies -= 1
                return "Oups, cette lettre n'est pas dans le mot !!!"

    ##################################################
    #          4e METHODE : Deviner Lettre           #
    ##################################################
    def deviner_mot(entree):
        global mot_a_deviner
        global vies
        global mot_a_afficher

        # On vérifie que l'entree correspond bien au mot à deviner
        if entree == mot_a_deviner:
            mot_a_afficher = entree 
            return "Bravo, tu as trouvé le bon mot !"
        else :
            vies -= 1
            return "Dommage, ce n'est pas le bon mot !"

    ##################################################
    #   5e METHODE : Actualisation du mot à afficher  #
    ##################################################
    # On vérifie si chaque lettre du mot == à l'entrée
    def actualisation_mot_a_afficher(lettre):
        global mot_a_deviner
        global mot_a_afficher
        # On parcourt grâce à une boucle notre mot_a_deviner
        for i in range(len(mot_a_deviner)):
            # On vérifie dans mot_a_deviner si la lettre est à position i
            if lettre == mot_a_deviner[i] :
                # On passe par une liste car les str sont immuables 
                mot_tmp = list(mot_a_deviner)
                # On ajoute à lettre à la bonne position donc i
                mot_tmp[i] = lettre 
                # On recupe la str avec la methode join
                mot_a_afficher = "".join(mot_tmp)



