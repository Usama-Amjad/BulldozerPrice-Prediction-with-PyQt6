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
        self.Price = QtWidgets.QLineEdit(parent=Dialog)
        self.Price.setGeometry(QtCore.QRect(270, 110, 121, 41))
        self.Price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Price.setClearButtonEnabled(True)
        self.Price.setObjectName("Price")
        self.estimatedPrice = QtWidgets.QLabel(parent=Dialog)
        self.estimatedPrice.setGeometry(QtCore.QRect(240, 50, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.estimatedPrice.setFont(font)
        self.estimatedPrice.setObjectName("estimatedPrice")
        self.goBack = QtWidgets.QPushButton(parent=Dialog)
        self.goBack.setGeometry(QtCore.QRect(280, 180, 93, 28))
        self.goBack.setObjectName("goBack")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.estimatedPrice.setText(_translate("Dialog", "Estimated Price"))
        self.goBack.setText(_translate("Dialog", "Go Back"))
