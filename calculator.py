import sys

from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QStatusBar, QWidget, QMainWindow, QLabel, QAction, QToolBar, QCheckBox, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, QSize

# This code was written by me, Sean Shea on 1/27/21


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.executable = ''
        self.setWindowTitle("Baller Mafuckin App")

        self.setFixedSize(280, 350)

        toolbar = QToolBar('Main Toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('calculator.svg'), 'Your button', self)
        button_action.setStatusTip("Sweet PNG")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addWidget(QLabel("Calculator"))

        self.setStatusBar(QStatusBar(self))

        button_list = ["C", "+/-", "%", "/", 7, 8, 9, "X", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "=", ":)"]

        full_layout = QVBoxLayout()
        self.show_work = QLabel("type...")
        full_layout.addWidget(self.show_work)

        layout = QGridLayout()
        buttons = self.create_buttons(button_list)

        count = 0
        for row in range(5):
            for column in range(4):
                layout.addWidget(buttons[count], row, column)
                count += 1

        full_layout.addLayout(layout)

        widget = QWidget()
        widget.setLayout(full_layout)
        self.setCentralWidget(widget)

    def onMyToolBarButtonClick(self, s):
        print('hello programmer', s)

    def b1(self):
        self.executable = ''
        self.show_work.setText(self.executable)

    def b2(self):
        if self.executable == '':
            pass
        elif self.executable[0] == '-':
            self.executable = self.executable[1:]
        else:
            self.executable = '-' + self.executable

        self.show_work.setText(self.executable)

    def b3(self):
        self.executable += '%'
        self.show_work.setText(self.executable)

    def b4(self):
        if self.executable == '':
            pass
        else:
            self.executable += '/'
        self.show_work.setText(self.executable)

    def b5(self):
        self.executable += '7'
        self.show_work.setText(self.executable)

    def b6(self):
        self.executable += '8'
        self.show_work.setText(self.executable)

    def b7(self):
        self.executable += '9'
        self.show_work.setText(self.executable)

    def b8(self):
        self.executable += '*'
        self.show_work.setText(self.executable)

    def b9(self):
        self.executable += '4'
        self.show_work.setText(self.executable)

    def b10(self):
        self.executable += '5'
        self.show_work.setText(self.executable)

    def b11(self):
        self.executable += '6'
        self.show_work.setText(self.executable)

    def b12(self):
        self.executable += '-'
        self.show_work.setText(self.executable)

    def b13(self):
        self.executable += '1'
        self.show_work.setText(self.executable)

    def b14(self):
        self.executable += '2'
        self.show_work.setText(self.executable)

    def b15(self):
        self.executable += '3'
        self.show_work.setText(self.executable)

    def b16(self):
        self.executable += '+'
        self.show_work.setText(self.executable)

    def b17(self):
        self.executable += '0'
        self.show_work.setText(self.executable)

    def b18(self):
        self.executable += '.'
        self.show_work.setText(self.executable)

    def b19(self):
        print(eval(self.executable))
        answer = str(eval(self.executable))
        self.show_work.setText(answer)

    def b20(self):
        print("pass")
        self.show_work.setText(self.executable)

    def create_buttons(self, list):

        finished_list = []

        button1 = QPushButton(str(list[0]))
        button1.setStyleSheet("background-color: red")
        button1.clicked.connect(self.b1)
        finished_list.append(button1)

        button2 = QPushButton(str(list[1]))
        button2.setStyleSheet("background-color: #34abeb;")
        button2.clicked.connect(self.b2)
        finished_list.append(button2)

        button3 = QPushButton(str(list[2]))
        button3.setStyleSheet("background-color: #34abeb;")
        button3.clicked.connect(self.b3)
        finished_list.append(button3)

        button4 = QPushButton(str(list[3]))
        button4.setStyleSheet("background-color: #f5bf42;")
        button4.clicked.connect(self.b4)
        finished_list.append(button4)

        button5 = QPushButton(str(list[4]))
        button5.setStyleSheet("background-color: #34abeb;")
        button5.clicked.connect(self.b5)
        finished_list.append(button5)

        button6 = QPushButton(str(list[5]))
        button6.setStyleSheet("background-color: #34abeb;")
        button6.clicked.connect(self.b6)
        finished_list.append(button6)

        button7 = QPushButton(str(list[6]))
        button7.setStyleSheet("background-color: #34abeb;")
        button7.clicked.connect(self.b7)
        finished_list.append(button7)

        button8 = QPushButton(str(list[7]))
        button8.setStyleSheet("background-color: #f5bf42;")
        button8.clicked.connect(self.b8)
        finished_list.append(button8)

        button9 = QPushButton(str(list[8]))
        button9.setStyleSheet("background-color: #34abeb;")
        button9.clicked.connect(self.b9)
        finished_list.append(button9)

        button10 = QPushButton(str(list[9]))
        button10.setStyleSheet("background-color: #34abeb;")
        button10.clicked.connect(self.b10)
        finished_list.append(button10)

        button11 = QPushButton(str(list[10]))
        button11.setStyleSheet("background-color: #34abeb;")
        button11.clicked.connect(self.b11)
        finished_list.append(button11)

        button12 = QPushButton(str(list[11]))
        button12.setStyleSheet("background-color: #f5bf42;")
        button12.clicked.connect(self.b12)
        finished_list.append(button12)

        button13 = QPushButton(str(list[12]))
        button13.setStyleSheet("background-color: #34abeb;")
        button13.clicked.connect(self.b13)
        finished_list.append(button13)

        button14 = QPushButton(str(list[13]))
        button14.setStyleSheet("background-color: #34abeb;")
        button14.clicked.connect(self.b14)
        finished_list.append(button14)

        button15 = QPushButton(str(list[14]))
        button15.setStyleSheet("background-color: #34abeb;")
        button15.clicked.connect(self.b15)
        finished_list.append(button15)

        button16 = QPushButton(str(list[15]))
        button16.setStyleSheet("background-color: #f5bf42;")
        button16.clicked.connect(self.b16)
        finished_list.append(button16)

        button17 = QPushButton(str(list[16]))
        button17.setStyleSheet("background-color: #34abeb;")
        button17.clicked.connect(self.b17)
        finished_list.append(button17)

        button18 = QPushButton(str(list[17]))
        button18.setStyleSheet("background-color: #34abeb;")
        button18.clicked.connect(self.b18)
        finished_list.append(button18)

        button19 = QPushButton(str(list[18]))
        button19.setStyleSheet("background-color: #f5bf42;")
        button19.clicked.connect(self.b19)
        finished_list.append(button19)

        button20 = QPushButton(str(list[19]))
        button20.setStyleSheet("background-color: #f5bf42;")
        button20.clicked.connect(self.b20)
        finished_list.append(button20)

        return finished_list


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

