# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ksce.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 91, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 67, 17))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 67, 17))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 201, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 201, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 100, 201, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 140, 201, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 180, 201, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 250, 141, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 250, 111, 25))
        self.pushButton.clicked.connect(self.marksAdder)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.destroy)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(76, 319, 191, 41))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEdit.textEdited['QString'].connect(self.lineEdit.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kcpe"))
        self.label.setText(_translate("MainWindow", "English"))
        self.label_2.setText(_translate("MainWindow", "Science"))
        self.label_3.setText(_translate("MainWindow", "Mathematics"))
        self.label_5.setText(_translate("MainWindow", "Kiswahili"))
        self.label_6.setText(_translate("MainWindow", "G.H.C.R.E"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "english marks"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Science marks"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "mathematics marks"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Kiswahili marks"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "social studies "))
        self.pushButton.setText(_translate("MainWindow", "View the Results"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancels"))
        self.label_7.setText(_translate("MainWindow", "Your Total marks is"))
    
    def marksAdder(self):
        '''Getting the text from the qlineedit'''
        englishMarks = int(self.lineEdit.text())
        scienceMarks = int(self.lineEdit_2.text())
        mathMarks = int(self.lineEdit_3.text())
        kiswahiliMarks = int(self.lineEdit_4.text())
        socialMarks = int(self.lineEdit_5.text())

        TotalMarks = englishMarks + scienceMarks + mathMarks + kiswahiliMarks + socialMarks
        
        strTotalmarks = str(TotalMarks)
        self.label_7.setText("Your marks is " + strTotalmarks)
    def destroy(self):
        exit(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

