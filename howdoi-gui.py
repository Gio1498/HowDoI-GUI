from howdoi import howdoi
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide2.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("init")
        self.setWindowTitle("How Do I...?")
        self.setFixedSize(500, 500)

        # ask_button
        self.ask_button = QPushButton("Ask to How Do I")
        self.ask_button.clicked.connect(self.ask_to_howdoi)
        
        # question box
        self.question_input = QLineEdit()
        self.question_input.setPlaceholderText("Enter your question here")
        
        self.answer_label = QLabel("Ask me a question and I'll try to find the solution")
        self.answer_label.setAlignment(Qt.AlignLeft)
        
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.answer_label)
        layout.addWidget(self.question_input)
        layout.addWidget(self.ask_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        

    def ask_to_howdoi(self):
        question = self.question_input.text()
        if question:
            answer = howdoi.howdoi(question)
            self.answer_label.setText("Your question:\n" + question + "\n\nAnswer:\n\n" + answer)
            self.question_input.setText(None)
        else:
            QMessageBox.about(self, "Error", "Please enter a question")

    # def ask_to_howdoi(self):
    #     question = self.question_input.text()
    #     self.answer_label.setText(howdoi.howdoi(question))
    



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()



