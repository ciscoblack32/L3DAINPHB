import random

# Liste des régions et leurs chefs-lieux
regions = {
    "Grands ponts": "Dabou",
    "Iffou": "Daoukro",
    "Bounkani": "Bouna",
    "Tchologo": "Ferkessédougou",
    "San-Pédro": "San-Pédro",
    "Guémon": "Duékoué",
    "Lôh-Djiboua": "Divo",
    "Kabadougou": "Odienné",
    "Hambol": "Katiola",
    "N’Zi": "Dimbokro",
}

# Liste pour les meilleurs scores
meilleurs_scores = []

# Fonction principale du jeu
def jeu():
    print("\nBienvenue au jeu des régions de Côte d'Ivoire !")
    print("Vous devez répondre à 10 questions. Bonne chance !\n")

    # Mélanger les questions et en choisir 10
    questions = list(regions.items())
    random.shuffle(questions)
    questions = questions[:10]  # Prendre 10 questions aléatoires

    # Initialisation du score
    score = 0

    # Poser les questions
    for region, chef_lieu in questions:
        print(f"Quel est le chef-lieu de la région {region}?")
        reponse = input("Votre réponse : ").strip()

        if reponse.lower() == chef_lieu.lower():  # Vérifier la réponse
            print("Bonne réponse !\n")
            score += 10
        else:
            print(f"Faux ! Le chef-lieu de {region} est {chef_lieu}.\n")

    # Afficher le score final
    print(f"Votre score final est : {score} points.\n")

    # Ajouter le score aux meilleurs scores
    print("Entrez votre nom pour enregistrer votre score :")
    nom = input("Votre nom : ").strip()
    meilleurs_scores.append({"nom": nom, "score": score})

    # Afficher les meilleurs scores
    print("\nMeilleurs scores :")
    for score in meilleurs_scores:
        print(f"{score['nom']} - {score['score']} points")

    # Demander si le joueur veut rejouer
    rejouer = input("\nVoulez-vous rejouer ? (o/n) : ").strip().lower()
    if rejouer == "o":
        jeu()
    else:
        print("\nMerci d'avoir joué ! À bientôt !")

# Lancer le jeu
jeu()
