# Form implementation generated from reading ui file 'e:\Semester 5\Artificial Intelligence\Bulldozer_Price_Prediction_with_PyQt6_Interface\userInterface\adminView.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 607)
        self.adminView = QtWidgets.QLabel(parent=Dialog)
        self.adminView.setGeometry(QtCore.QRect(280, 30, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.adminView.setFont(font)
        self.adminView.setTabletTracking(True)
        self.adminView.setObjectName("adminView")
        self.viewAllB = QtWidgets.QPushButton(parent=Dialog)
        self.viewAllB.setGeometry(QtCore.QRect(110, 419, 93, 28))
        self.viewAllB.setTabletTracking(True)
        self.viewAllB.setObjectName("viewAllB")
        self.updateB = QtWidgets.QPushButton(parent=Dialog)
        self.updateB.setGeometry(QtCore.QRect(530, 419, 93, 28))
        self.updateB.setTabletTracking(True)
        self.updateB.setObjectName("updateB")
        self.add = QtWidgets.QPushButton(parent=Dialog)
        self.add.setGeometry(QtCore.QRect(250, 419, 93, 28))
        self.add.setTabletTracking(True)
        self.add.setObjectName("add")
        self.delete_2 = QtWidgets.QPushButton(parent=Dialog)
        self.delete_2.setGeometry(QtCore.QRect(390, 419, 93, 28))
        self.delete_2.setTabletTracking(True)
        self.delete_2.setObjectName("delete_2")
        self.logOut = QtWidgets.QPushButton(parent=Dialog)
        self.logOut.setGeometry(QtCore.QRect(530, 489, 93, 28))
        self.logOut.setTabletTracking(True)
        self.logOut.setObjectName("logOut")
        self.searchByModelId = QtWidgets.QPushButton(parent=Dialog)
        self.searchByModelId.setGeometry(QtCore.QRect(110, 489, 93, 28))
        self.searchByModelId.setTabletTracking(True)
        self.searchByModelId.setObjectName("searchByModelId")
        self.searchID = QtWidgets.QLineEdit(parent=Dialog)
        self.searchID.setGeometry(QtCore.QRect(220, 490, 113, 31))
        self.searchID.setTabletTracking(True)
        self.searchID.setObjectName("searchID")
        self.adminTable = QtWidgets.QTableWidget(parent=Dialog)
        self.adminTable.setGeometry(QtCore.QRect(115, 100, 501, 291))
        self.adminTable.setColumnCount(4)
        self.adminTable.setObjectName("adminTable")
        self.adminTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.adminTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminTable.setHorizontalHeaderItem(3, item)
        self.adminTable.horizontalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.adminView.setText(_translate("Dialog", "Admin View"))
        self.viewAllB.setText(_translate("Dialog", "View All"))
        self.updateB.setText(_translate("Dialog", "Update"))
        self.add.setText(_translate("Dialog", "Add"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.logOut.setText(_translate("Dialog", "Log Out"))
        self.searchByModelId.setText(_translate("Dialog", "Search"))
        self.adminTable.setSortingEnabled(True)
        item = self.adminTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ModelID"))
        item = self.adminTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "YearMade"))
        item = self.adminTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "MeterReading"))
        item = self.adminTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Price"))
