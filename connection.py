from PySide6 import QtWidgets, QtSql


class Data:
    
    
    def __init__(self) -> None:
        super(Data, self).__init__()
        
        
    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')
        
        if not db.open():
            QtWidgets.QFontComboBox.critical(None, "Не могу открыть базу данных",
                                             "Нажмите «Отмена», чтобы выйти.", QtWidgets.QMessageBox.Cancel)
            return False
        
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Dete VARCHAR(20),"
                   "Category VARCHAR(20), Description VARCHAR(20), Balance REAL, Status VARCHAR(20))")
        return True
    
    
    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        
        query.exec()