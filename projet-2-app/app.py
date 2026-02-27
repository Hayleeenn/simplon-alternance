taches = []

def afficher_taches():
    if not taches:
        print("Aucune tâche pour le moment.")
    else:
        for i, t in enumerate(taches):
            print(f"{i+1}. {t}")

while True:
    print("\n1. Ajouter tâche\n2. Voir tâches\n3. Quitter")
    choix = input("Choix : ")
    if choix == "1":
        tache = input("Nom de la tâche : ")
        taches.append(tache)
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        break
    else:
        print("Choix invalide.")