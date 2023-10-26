import sys
from PySide6 import QtWidgets

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from new_transaction import Ui_Dialog
from PySide6.QtSql import QSqlTableModel

from connection import Data


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = Data()
        self.view_data()
        
        self.ui.btn_new_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_edit_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_delete_transaction.clicked.connect(self.delete_current_transaction)
        
        
    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.model.select()
        self.ui.tableView.setModel(self.model)
        
        
    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        
        sender = self.sender()
        
        if sender.text() == "Новая транзакция":
            self.ui_window.btn_new_transaction.cliked.connect(self.add_new_transaction)
        else:
            self.ui_window.btn_new_transaction.clicked.connect(self.edit_current_transaction)
        
        
    def add_new_transaction(self):
        date = self.ui_window.dateEdit.text()
        category = self.ui_window.cb_choose_category.currentText()
        description = self.ui_windows.le_description.text()
        balance = self.ui.window.le_balance.text()
        status = self.ui_window.cb_status.cureentText()
        
        self.connection.add_new_transaction_query(date, category, description, balance, status)
        
        self.view_data()
        self.new_window.close()
        
        
    def edit_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().dat(index))
        
        date = self.ui_window.dateEdit.text()
        category = self.ui_window.cb_choose_category.currentText()
        description = self.ui_windows.le_description.text()
        balance = self.ui.window.le_balance.text()
        status = self.ui_window.cb_status.cureentText()
        
        self.connection.update_transaction_query(date, category, description, balance, status, id)
        
        self.view_data()
        self.new_window.close()
        
    
    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().dat(index))
        
        self.connection.delete_transaction_query(id)
        
        self.view_data()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    
    sys.exit(app.exec())
    