import sys
from n import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtSql
import sqlite3
from pprint import pprint

class MainWindow_EXEC():
    
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
            
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        #-------------------------- 
        
        self.create_DB()
        self.ui.btnVer.clicked.connect(self.print_data)
        self.model = None
        self.ui.btnVer.clicked.connect(self.sql_tableview_model)
        self.ui.btnAgregar.clicked.connect(self.sql_add_row)
        self.ui.btnEliminar.clicked.connect(self.sql_delete_row)
        
        
        #-------------------------- 
       # self.init_tabs()
        
        self.MainWindow.show()
        sys.exit(app.exec_()) 
        
    #----------------------------------------------------------
    def sql_delete_row(self):
        if self.model:
            self.model.removeRow(self.ui.tblProductos.currentIndex().row())
        else:
            self.sql_tableview_model()       
                
    #----------------------------------------------------------
    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.sql_tableview_model()

    #----------------------------------------------------------
    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Producto.db')
        
        tableview = self.ui.tblProductos
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        
        self.model.setTable('Producto')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Cod_Cobro")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Me")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "cod_Concepto")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "precio")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Cantidad")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Total")        
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Fecha Cobro")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Cod_jornada")                          
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "cod_Empleado")  
    #----------------------------------------------------------
    def print_data(self):
        sqlite_file = 'Producto.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'Producto' ORDER BY Cod_Cobro")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       # not needed when only selecting data
        conn.close()        
        
    #----------------------------------------------------------
    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Producto.db')
        db.open()
        
        query = QtSql.QSqlQuery()
          
        query.exec_("create table Producto(Cod_Cobro int primary key, "
                    "Me int,cod_Concepto int,precio int,Cantidad int,Total int,Fecha Cobro varchar(20),Cod_jornada int,cod_Empleado int  )")
        query.exec_("insert into Producto values(1,1,1,25,2,50,'21/Enero/2019',1,1)")
        query.exec_("insert into Producto values(2,1,1,30,2,60,'21/Abril/2019',1,1)")
        query.exec_("insert into Producto values(3,1,1,40,2,80,'21/Mayo/2019',1,1)")
        query.exec_("insert into Producto values(4,1,1,50,2,1000,'21/Diciembre/2019',1,1)")

if __name__ == "__main__":
    MainWindow_EXEC()
