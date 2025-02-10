class Utilisateur:
    
    def __init__(self, id_utilisateur, nom, email, mot_de_passe, date_inscription):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.date_inscription = date_inscription
    
    def inscrire(self):
        # Enregistre utilisateur dans la DB
        pass

    def authentifier(self, email, mot_de_passe):
        #Vérifier si le user peut se connecter
        pass

    def obtenir_statistiques(self):
        #Retourne les staistiques de l'utilisateur
        pass
    