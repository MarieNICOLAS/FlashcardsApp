from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Flashcards App")
        self.setGeometry(100, 100, 400, 300)

        # Layout principal
        layout = QVBoxLayout()

        # Champs pour ajouter une carte
        self.label_question = QLabel("Question:")
        self.input_question = QLineEdit()

        self.label_answer = QLabel("Réponse:")
        self.input_answer = QLineEdit()

        self.button_add = QPushButton("Ajouter la flashcard")
        self.button_add.clicked.connect(self.add_flashcard)

        # Ajout des widgets au layout
        layout.addWidget(self.label_question)
        layout.addWidget(self.input_question)
        layout.addWidget(self.label_answer)
        layout.addWidget(self.input_answer)
        layout.addWidget(self.button_add)

        self.setLayout(layout)

    def add_flashcard(self):
        """Action pour enregistrer une flashcard (on connectera ça à la BDD après)."""
        question = self.input_question.text()
        answer = self.input_answer.text()

        print(f"Ajout de la flashcard : {question} -> {answer}")  # Debug pour l’instant

        # Nettoyage des champs après ajout
        self.input_question.clear()
        self.input_answer.clear()

# Lancer l'application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
