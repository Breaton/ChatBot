# Fonction pour poser une énigme et vérifier la réponse
def poser_enigme(question, reponses, bonne_reponse):
    print(question)
    for i, reponse in enumerate(reponses, 1):
        print(f"{i}. {reponse}")
    
    # Demander à l'utilisateur de choisir une réponse
    choix = int(input("Votre réponse (choisissez un numéro) : "))
    
    if reponses[choix - 1] == bonne_reponse:
        print("Bonne réponse !")
        return True
    else:
        print("Mauvaise réponse. Essayez encore !")
        return False

def main():
    # Suivi des bonnes réponses
    bonne_reponse_1 = False
    bonne_reponse_2 = False
    bonne_reponse_3 = False

    # Enigme 1
    enigme_1 = "Si je vous dis 'Thierry observe Karine, yeux ouverts.' Vous me répondez ?"
    reponses_1 = [
        "Vincent observe Jean, discrètement.",
        "Claude a soigneusement abattu Bernard, laissant Antoine nier chaque accusation.",
        "Marion parle en secret à Quentin, donnant des ordres précis.",
        "Colin vérifie les indices, Patrick reste silencieux."
    ]
    bonne_reponse_1 = "Claude a soigneusement abattu Bernard, laissant Antoine nier chaque accusation."
    
    if poser_enigme(enigme_1, reponses_1, bonne_reponse_1):
        bonne_reponse_1 = True
    
    # Enigme 2
    enigme_2 = "Si je vous dis 'Sophie harcèle Antoine, ne gardant hébété Alain, inquiet.' Vous me répondez ?"
    reponses_2 = [
        "Émilie cache son carnet, regard furtif.",
        "Sophie fuit discrètement, appuyant sur un bouton.",
        "Oscar surveille Anna, Karine approuve.",
        "Louise évalue la situation, sans pression."
    ]
    bonne_reponse_2 = "Oscar surveille Anna, Karine approuve."
    
    if poser_enigme(enigme_2, reponses_2, bonne_reponse_2):
        bonne_reponse_2 = True
    
    # Enigme 3
    enigme_3 = "Si je vous dis 'Paul a retrouvé Ingrid, seul.' Vous me répondez ?"
    reponses_3 = [
        "Marc ignore Axel, mission improvisée.",
        "Victor ignore les bruits, silencieux.",
        "Stecy marche lentement, suivant la direction donnée.",
        "Deborah observe à travers la fenêtre, nerveuse."
    ]
    bonne_reponse_3 = "Marc ignore Axel, mission improvisée."
    
    if poser_enigme(enigme_3, reponses_3, bonne_reponse_3):
        bonne_reponse_3 = True
    
    # Vérification si toutes les réponses étaient correctes
    if bonne_reponse_1 and bonne_reponse_2 and bonne_reponse_3:
        print("\nIdentité confirmée : Toutes les clés pour résoudre cette énigme se trouvent entre les pages 6 et 7.")
    else:
        print("\nVous n'avez pas encore toutes les bonnes réponses. Réessayez.")

# Lancer le chatbot
if __name__ == "__main__":
    main()

