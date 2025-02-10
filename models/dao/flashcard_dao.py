import sqlite3
from models.flashcard import Flashcard
from models.database import Database

class FlashcardDAO:

    @staticmethod
    def add_flashcard(question, reponse, categorie, utilisateur):
        query = "INSERT INTO flashcards (question, answer, category) VALUES (?, ?, ?)"
        params = (question, reponse, categorie.nom)
        Database.execute_query(query, params, commit=True)
    
    @staticmethod
    def get_flashcard():
        query = "SELECT id, question, answer, category FROM flashcards"
        rows = Database.execute_query(query, fetch_all=True)

        flashcards = []
        for row in rows:
            flashcards.append(Flashcard(*row, None))
        return flashcards
    
    @staticmethod
    def update_flashcard(id_flashcard, question, reponse, categorie):
        query = "UPDATE flashcards SET question = ?, answer = ?, category = ? WHERE id = ?"
        params = (question, reponse, categorie.nom, id_flashcard)
        Database.execute_query(query, params, commit=True)
    
    @staticmethod
    def delete_flashcard(id_flashcard):
        query = "DELETE FROM flashcards WHERE id = ?"
        Database.execute_query(query,(id_flashcard,), commit=True)