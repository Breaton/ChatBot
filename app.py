import streamlit as st

st.title("🔐 Énigmes du jeu de piste")

def poser_enigme(numero, question, reponses, bonne_reponse_key):
    st.subheader(f"Énigme {numero}")
    st.write(question)

    choix = st.radio("Votre réponse :", reponses, key=bonne_reponse_key)
    return choix

# Liste des énigmes
bonne_reponses = {
    "enigme1": "Claude a soigneusement abattu Bernard, laissant Antoine nier chaque accusation.",
    "enigme2": "Oscar surveille Anna, Karine approuve.",
    "enigme3": "Marc ignore Axel, mission improvisée."
}

rep1 = poser_enigme(1,
    "Si je vous dis 'Thierry observe Karine, yeux ouverts.' Vous me répondez ?",
    [
        "Vincent observe Jean, discrètement.",
        "Claude a soigneusement abattu Bernard, laissant Antoine nier chaque accusation.",
        "Marion parle en secret à Quentin, donnant des ordres précis.",
        "Colin vérifie les indices, Patrick reste silencieux."
    ],
    "enigme1"
)

rep2 = poser_enigme(2,
    "Si je vous dis 'Sophie harcèle Antoine, ne gardant hébété Alain, inquiet.' Vous me répondez ?",
    [
        "Émilie cache son carnet, regard furtif.",
        "Sophie fuit discrètement, appuyant sur un bouton.",
        "Oscar surveille Anna, Karine approuve.",
        "Louise évalue la situation, sans pression."
    ],
    "enigme2"
)

rep3 = poser_enigme(3,
    "Si je vous dis 'Paul a retrouvé Ingrid, seul.' Vous me répondez ?",
    [
        "Marc ignore Axel, mission improvisée.",
        "Victor ignore les bruits, silencieux.",
        "Stecy marche lentement, suivant la direction donnée.",
        "Deborah observe à travers la fenêtre, nerveuse."
    ],
    "enigme3"
)

if st.button("Valider mes réponses"):
    if (rep1 == bonne_reponses["enigme1"] and
        rep2 == bonne_reponses["enigme2"] and
        rep3 == bonne_reponses["enigme3"]):
        st.success("✅ Identité confirmée : Toutes les clés pour résoudre cette énigme se trouvent entre les pages 6 et 7.")
    else:
        st.error("❌ Certaines réponses sont incorrectes. Réessayez !")
