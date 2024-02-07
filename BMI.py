import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.resize(400, 200)

        # add main window background colour
        self.setStyleSheet("background-color: #DBEBF3;")



        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.weight_label = QLabel("WEIGHT (kg):")
        self.weight = QLineEdit()
        self.weight.setFixedWidth(55)
        self.height_label = QLabel("HEIGHT (m):")
        self.height = QLineEdit()
        self.height.setFixedWidth(55)
        self.result_label = QLabel("BMI:")
        self.result = QLineEdit()
        self.result.setFixedWidth(55) 
        self.result.setReadOnly(True)

        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result)

        self.calc_button = QPushButton("Calculate")
        layout.addWidget(self.calc_button)
        self.calc_button.setFixedWidth(80)
        self.calc_button.setStyleSheet("background-color: ##99A3A4; color: white; border: #; padding: 5px 10px;")
        self.calc_button.clicked.connect(self.add_numbers)



        self.clear_button = QPushButton("Clear")
        layout.addWidget(self.clear_button)
        self.clear_button.setFixedWidth(55)
        self.clear_button.setStyleSheet("background-color: #99A3A4; color: white; border: #; padding: 5px 10px;")
        self.clear_button.clicked.connect(self.clear_funct)

        #set background image using css
        #central_widget.setStyleSheet("background-image: url('C:/Users/fse024/Downloads/edgar-chaparro-sHfo3WOgGTU-unsplash.jpg.jpg'); background-repeat: no-repeat; background-position: center;")

    def add_numbers(self):

        try:
            weight = float(self.weight.text())
            height = float(self.weight.text())
            result =(weight*703)/(height*height)
            self.result.setText(str(result))
        except ValueError:
            self.result.setText("Invalid input")


    def clear_funct(self):
        self.weight.clear()
        self.height.clear()
        self.result.clear()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




