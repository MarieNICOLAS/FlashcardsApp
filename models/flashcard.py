import sqlite3
import os
from database import Database

class Flashcard:
    def __init__(self, question, answer, category=None, card_id=None):
        self.id = card_id
        self.question = question
        self.answer = answer
        self.category = category
    
    # Add card in db
    def save(self):
       Database.execute_query(
            "INSERT INTO flashcards (question, answer, category) VALUES (?, ?, ?)",
            (self.question, self.answer, self.category),
            commit=True
        )
       print("✅ Carte ajoutée avec succès !")
    
    # Get All Cards
    @staticmethod
    def get_all():
        rows = Database.execute_query(
            "SELECT id, question, answer, category FROM flashcards",
            fetch_all=True
        )
        return[Flashcard(q, a, c, card_id=i) for i, q, a, c in rows]
    
    # Fetch Specific Card by id
    @staticmethod
    def get_by_id(card_id):
        row = Database.execute_query(
            "SELECT id, question, answer, category FROM flashcards WHERE id=?",
            (card_id,),
            fetch_one=True
        )
        return Flashcard(row[1], row[2], row[3], card_id=row[0]) if row else None

    # Update Card
    def update(self):
        if self.id is None:
            print("❌ Impossible de mettre à jour : ID manquant")
            return
        
        # Remplace None par une chaîne vide pour SQLite
        category_value = self.category if self.category is not None else ""

        Database.execute_query(
            "UPDATE flashcards SET question = ?, answer = ?, category = ? WHERE id=?",
            (self.question, self.answer, category_value, self.id),
            commit=True
        )
        print("✅ Carte mise à jour avec succès !")


    # Delete Card
    def delete(self):
        if self.id is None:
            print("❌ Impossible de supprimer : ID manquant")
            return

        Database.execute_query(
            "DELETE FROM flashcards WHERE id = ?",
            (self.id,),
            commit=True
        )
        print("✅ Carte supprimée avec succès !")

