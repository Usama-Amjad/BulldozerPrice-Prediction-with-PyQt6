# Form implementation generated from reading ui file 'e:\Semester 5\Artificial Intelligence\Bulldozer_Price_Prediction_with_PyQt6_Interface\userInterface\priceOutput.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 595)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 641, 601))
        self.widget.setStyleSheet("background-image: url(C:/Users/Dell/Downloads/priceoutput.jpg);background-size: 150px;\n"
"    ")
        self.widget.setObjectName("widget")
        self.estimatedPrice = QtWidgets.QLabel(parent=self.widget)
        self.estimatedPrice.setGeometry(QtCore.QRect(230, 70, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.estimatedPrice.setFont(font)
        self.estimatedPrice.setObjectName("estimatedPrice")
        self.goBack = QtWidgets.QPushButton(parent=self.widget)
        self.goBack.setGeometry(QtCore.QRect(270, 200, 93, 28))
        self.goBack.setObjectName("goBack")
        self.Price = QtWidgets.QLineEdit(parent=self.widget)
        self.Price.setGeometry(QtCore.QRect(260, 130, 121, 41))
        self.Price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Price.setClearButtonEnabled(True)
        self.Price.setObjectName("Price")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.estimatedPrice.setText(_translate("Dialog", "Estimated Price"))
        self.goBack.setText(_translate("Dialog", "Go Back"))
