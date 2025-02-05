import sqlite3
import os

#Chemin où sera stockée la bdd
DB_PATH = os.path.join(os.path.dirname(__file__), "../database.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    #Création de la table flashcards
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS flashcards (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   question TEXT NOT NULL,
                   answer TEXT NOT NULL,
                   category TEXT
                )
    ''')
    conn.commit()
    conn.close()
    print("📂 Base de données SQLite initialisée !")

if __name__ == "__main__":
    init_db()