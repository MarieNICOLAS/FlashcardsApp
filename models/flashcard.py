class Flashcard:

    def __init__(self, id_flashcard, question, reponse, categorie, utilisateur):
        self.id_flashcard = id_flashcard
        self.question = question
        self.reponse = reponse
        self.categorie = categorie
        self.utilisateur = utilisateur
    
    def afficher(self):
        print(f"Question: {self.question} | Réponse: {self.reponse}")

    def verifier_reponse(self, reponse_utilisateur):
        return self.reponse.lower() == reponse_utilisateur.lower()