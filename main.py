import sys
from PySide6 import QtWidgets

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from new_transaction import Ui_Dialog

from connection import Data


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = Data()
        
        
    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        
        
    def add_new_transaction(self):
        date = self.ui_window.dateEdit.text()
        category = self.ui_window.cb_choose_category.currentText()
        description = self.ui_windows.le_description.text()
        balance = self.ui.window.le_balance.text()
        status = self.ui_window.cb_status.cureentText()
        
        self.connection.add_new_transaction_query(date, category, description, balance, status)
        
        self.new_window.close()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    
    sys.exit(app.exec())
    