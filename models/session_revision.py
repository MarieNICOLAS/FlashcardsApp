class SessionRevision:

    def __init__(self, id_session, date_session, score, utilisateur):
        self.id_session = id_session
        self.date_session = date_session
        self.score = score
        self.utilisateur = utilisateur
    
    def demarrer_session(self):
        pass

    def calculer_score(self, id_session):
        pass

    def ajouter_flashcard_session(self, id_flashcard):
        pass