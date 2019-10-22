# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevo.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(10, 290, 75, 23))
        self.btnAgregar.setObjectName("btnAgregar")
        self.btnVer = QtWidgets.QPushButton(self.centralwidget)
        self.btnVer.setGeometry(QtCore.QRect(170, 290, 75, 23))
        self.btnVer.setObjectName("btnVer")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(90, 290, 75, 23))
        self.btnEliminar.setObjectName("btnEliminar")
        self.tblProductos = QtWidgets.QTableView(self.centralwidget)
        self.tblProductos.setGeometry(QtCore.QRect(0, 0, 581, 281))
        self.tblProductos.setObjectName("tblProductos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
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
        self.btnAgregar.setText(_translate("MainWindow", "Agregar"))
        self.btnVer.setText(_translate("MainWindow", "Ver"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
