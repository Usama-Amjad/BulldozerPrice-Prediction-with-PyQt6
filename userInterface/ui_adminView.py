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
        Dialog.resize(687, 493)
        self.adminTable = QtWidgets.QTableWidget(parent=Dialog)
        self.adminTable.setGeometry(QtCore.QRect(100, 80, 501, 291))
        self.adminTable.setAlternatingRowColors(True)
        self.adminTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.adminTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
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
        self.adminTable.horizontalHeader().setVisible(True)
        self.adminTable.horizontalHeader().setCascadingSectionResizes(False)
        self.adminLabelView = QtWidgets.QLabel(parent=Dialog)
        self.adminLabelView.setGeometry(QtCore.QRect(260, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.adminLabelView.setFont(font)
        self.adminLabelView.setObjectName("adminLabelView")
        self.viewAll = QtWidgets.QPushButton(parent=Dialog)
        self.viewAll.setGeometry(QtCore.QRect(100, 390, 93, 28))
        self.viewAll.setObjectName("viewAll")
        self.delete_2 = QtWidgets.QPushButton(parent=Dialog)
        self.delete_2.setGeometry(QtCore.QRect(240, 390, 93, 28))
        self.delete_2.setObjectName("delete_2")
        self.add = QtWidgets.QPushButton(parent=Dialog)
        self.add.setGeometry(QtCore.QRect(380, 390, 93, 28))
        self.add.setObjectName("add")
        self.update = QtWidgets.QPushButton(parent=Dialog)
        self.update.setGeometry(QtCore.QRect(510, 390, 93, 28))
        self.update.setObjectName("update")
        self.searchByModelId = QtWidgets.QPushButton(parent=Dialog)
        self.searchByModelId.setGeometry(QtCore.QRect(100, 440, 121, 31))
        self.searchByModelId.setObjectName("searchByModelId")
        self.searchID = QtWidgets.QLineEdit(parent=Dialog)
        self.searchID.setGeometry(QtCore.QRect(240, 440, 113, 31))
        self.searchID.setObjectName("searchID")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.adminTable.setSortingEnabled(True)
        item = self.adminTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ModelID"))
        item = self.adminTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "YearMade"))
        item = self.adminTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "MeterReading"))
        item = self.adminTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Price"))
        self.adminLabelView.setText(_translate("Dialog", "Admin View"))
        self.viewAll.setText(_translate("Dialog", "ViewAll"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.add.setText(_translate("Dialog", "Add"))
        self.update.setText(_translate("Dialog", "Update"))
        self.searchByModelId.setText(_translate("Dialog", "Search by ModelID"))
