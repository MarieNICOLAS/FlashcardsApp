import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../database.db")

# SGBD SQLite - simplifier les requêtes
class Database:

    @staticmethod
    def execute_query(query, params=(), fetch_one=False, fetch_all=False, commit=False):
        """Exécute une requête SQL et retourne le résultat si nécessaire."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    
        print(f"🟢 EXEC SQL: {query}")  # ✅ Debug : Affiche la requête SQL
        print(f"🟢 PARAMS: {params}")  # ✅ Debug : Affiche les valeurs passées à SQLite
    
        cursor.execute(query, params)

        result = None  
        if fetch_one:
            result = cursor.fetchone()
        elif fetch_all:
            result = cursor.fetchall()
        
        if commit:
            conn.commit()
        
        conn.close()
        return result
