# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from widget11 import Ui_Form  
from widget12 import Ui_Form
from widget13 import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 40, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(390, 150, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 150, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 180, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(390, 180, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check_selection)
        self.pushButton.clicked.connect(self.check_selection1)
        self.pushButton.clicked.connect(self.check_selection2)
        self.pushButton.clicked.connect(self.check_bank_selection)



        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 250, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(390, 210, 95, 20))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(450, 210, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 210, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 110, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "         წიგნები"))
        self.comboBox.setCurrentText(_translate("MainWindow", "რომანი"))
        self.comboBox.setItemText(0, _translate("MainWindow", "რომანი"))
        self.comboBox.setItemText(1, _translate("MainWindow", "პოეზია"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ფანტასტიკა"))
        self.label_2.setText(_translate("MainWindow", "აირჩიეთ ჟანრი:"))
        self.label_3.setText(_translate("MainWindow", "აირჩიეთ ასაკი:"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "0-6"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "0-6"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "6-12"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "12-18"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "18+"))
        self.pushButton.setText(_translate("MainWindow", "არჩევა"))
        self.label_5.setText(_translate("MainWindow", "გასაგრძელებლად დააჭირეთ \"არჩევა\"-ს"))
        self.radioButton.setText(_translate("MainWindow", "BOG"))
        self.radioButton_2.setText(_translate("MainWindow", "TBC"))
        self.label_4.setText(_translate("MainWindow", "აირჩიეთ ბანკი: "))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-style:italic; text-decoration: underline;\">       წიგნის შესაძენათ შეავსეთ ფორმა</span></p></body></html>"))

    def check_selection(self):
        selected_genre = self.comboBox.currentText()
        selected_age = self.comboBox_2.currentText()
        if selected_genre == "რომანი" and selected_age in ["0-6", "6-12", "12-18", "18+"]:
            self.open_table_window()

    def check_selection1(self):
        selected_genre = self.comboBox.currentText()
        selected_age = self.comboBox_2.currentText()
        if selected_genre == "პოეზია" and selected_age in ["0-6", "6-12" ,"12-18", "18+"]:
            self.open_table_window()

    def check_selection2(self):
        selected_genre = self.comboBox.currentText()
        selected_age = self.comboBox_2.currentText()
        if selected_genre == "ფანტასტიკა" and selected_age in ["0-6", "6-12" ,"12-18", "18+"]:
            self.open_table_window()

    def check_bank_selection(self):
        if not (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            self.label_5.setText("გთხოვთ აირჩიოთ ერთ-ერთი")
        else:
            self.label_5.setText("გასაგრძელებლად დააჭირეთ \"არჩევა\"-ს")

    def open_table_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


