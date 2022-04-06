from howdoi import howdoi
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QScrollArea, QSlider
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt

class ScrollLabel(QScrollArea):

    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        layout = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        layout.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("How Do I...?")
        self.setMinimumSize(500, 500)

        # ask_button
        self.ask_button = QPushButton("Ask to How Do I")
        self.ask_button.clicked.connect(self.askToHowdoi)
        
        # question box
        self.question_input = QLineEdit()
        self.question_input.setPlaceholderText("Enter your question here")

        # make a slider to adjust text size
        self.slider_label = QLabel("Text Size")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(30)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged.connect(self.changeTextSize)
        

        self.answer_label = ScrollLabel()
        self.answer_label.setText("Ask me a question and I'll try to find the solution")
        self.answer_label_font = self.answer_label.font()
        
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.answer_label)
        layout.addWidget(self.question_input)
        layout.addWidget(self.ask_button)
        layout.addWidget(self.slider_label)
        layout.addWidget(self.slider)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def changeTextSize(self):
        size = self.slider.value()
        self.answer_label_font.setPointSize(size)
        self.answer_label.setFont(self.answer_label_font)

    

    def askToHowdoi(self):
        question = self.question_input.text()
        if question:
            answer = howdoi.howdoi(question)
            self.answer_label.setText("Your question:\n" + question + "\n\nAnswer:\n\n" + answer)
            self.question_input.setText(None)
        else:
            QMessageBox.about(self, "Error", "Please enter a question")

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()