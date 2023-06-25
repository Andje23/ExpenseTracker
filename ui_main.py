# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1006, 856)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-famaly: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lebel_current_balance = QLabel(self.balance_frame)
        self.lebel_current_balance.setObjectName(u"lebel_current_balance")
        self.lebel_current_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20 pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lebel_current_balance)

        self.lebel_balance = QLabel(self.balance_frame)
        self.lebel_balance.setObjectName(u"lebel_balance")
        self.lebel_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lebel_balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_up_arrow = QLabel(self.balance_frame)
        self.icon_up_arrow.setObjectName(u"icon_up_arrow")
        self.icon_up_arrow.setMaximumSize(QSize(24, 16777215))
        self.icon_up_arrow.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_up_arrow.setPixmap(QPixmap(u":/icon/icons/north_west_white_24dp.svg"))

        self.horizontalLayout.addWidget(self.icon_up_arrow)

        self.label_income = QLabel(self.balance_frame)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.label_income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.income_balance = QLabel(self.balance_frame)
        self.income_balance.setObjectName(u"income_balance")
        self.income_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.income_balance)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.balance_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(24, 16777215))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_6.setPixmap(QPixmap(u":/icon/icons/call_received_white_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_outcome = QLabel(self.balance_frame)
        self.label_outcome.setObjectName(u"label_outcome")
        self.label_outcome.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.utcome_balance = QLabel(self.balance_frame)
        self.utcome_balance.setObjectName(u"utcome_balance")
        self.utcome_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.utcome_balance)


        self.horizontalLayout_7.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 0)
        self.label_expense_tracker = QLabel(self.categories_frame)
        self.label_expense_tracker.setObjectName(u"label_expense_tracker")
        self.label_expense_tracker.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20 pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_expense_tracker)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_groceries = QLabel(self.categories_frame)
        self.icon_groceries.setObjectName(u"icon_groceries")
        self.icon_groceries.setMaximumSize(QSize(24, 16777215))
        self.icon_groceries.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_groceries.setPixmap(QPixmap(u":/icon/icons/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.icon_groceries)

        self.label_groceries = QLabel(self.categories_frame)
        self.label_groceries.setObjectName(u"label_groceries")
        self.label_groceries.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.label_groceries)

        self.balance_groceries = QLabel(self.categories_frame)
        self.balance_groceries.setObjectName(u"balance_groceries")
        self.balance_groceries.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.balance_groceries)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_entertainment = QLabel(self.categories_frame)
        self.icon_entertainment.setObjectName(u"icon_entertainment")
        self.icon_entertainment.setMaximumSize(QSize(24, 16777215))
        self.icon_entertainment.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_entertainment.setPixmap(QPixmap(u":/icon/icons/sports_esports_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.icon_entertainment)

        self.label_14 = QLabel(self.categories_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.balance_entertainment = QLabel(self.categories_frame)
        self.balance_entertainment.setObjectName(u"balance_entertainment")
        self.balance_entertainment.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.balance_entertainment)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_products = QLabel(self.categories_frame)
        self.icon_products.setObjectName(u"icon_products")
        self.icon_products.setMaximumSize(QSize(24, 16777215))
        self.icon_products.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_products.setPixmap(QPixmap(u":/icon/icons/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.icon_products)

        self.label_products = QLabel(self.categories_frame)
        self.label_products.setObjectName(u"label_products")
        self.label_products.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_products)

        self.balance_product = QLabel(self.categories_frame)
        self.balance_product.setObjectName(u"balance_product")
        self.balance_product.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.balance_product)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_other = QLabel(self.categories_frame)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setMaximumSize(QSize(24, 16777215))
        self.icon_other.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_other.setPixmap(QPixmap(u":/icon/icons/list_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.icon_other)

        self.label_others = QLabel(self.categories_frame)
        self.label_others.setObjectName(u"label_others")
        self.label_others.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.label_others)

        self.balance_others = QLabel(self.categories_frame)
        self.balance_others.setObjectName(u"balance_others")
        self.balance_others.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.balance_others)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_new_transaction = QPushButton(self.centralwidget)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255,255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255,255, 60);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255,255, 90);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_new_transaction)

        self.btn_edit_transaction = QPushButton(self.centralwidget)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255,255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255,255, 60);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255,255, 90);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_transaction.setIcon(icon1)
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_edit_transaction)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255,255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255,255, 60);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255,255, 90);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView{\n"
"	border-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-bottom-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"	background-color: rgba(53, 53, 53);\n"
"	color: white;\n"
"	border: none;\n"
"	height: 50px;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item{\n"
"	border-style: none;\n"
"	border-bottom: rgba(255, 255 , 255, 50);\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgba(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u043e\u0432", None))
        self.lebel_current_balance.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.lebel_balance.setText(QCoreApplication.translate("MainWindow", u"2000 \u0440\u0443\u0431", None))
        self.icon_up_arrow.setText("")
        self.label_income.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.income_balance.setText(QCoreApplication.translate("MainWindow", u"2000 \u0440\u0443\u0431", None))
        self.label_6.setText("")
        self.label_outcome.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))
        self.utcome_balance.setText(QCoreApplication.translate("MainWindow", u"2000 \u0440\u0443\u0431", None))
        self.label_expense_tracker.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0440\u0430\u0441\u0445\u043e\u0434\u043e\u0432", None))
        self.icon_groceries.setText("")
        self.label_groceries.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.balance_groceries.setText(QCoreApplication.translate("MainWindow", u"1000 \u0440\u0443\u0431", None))
        self.icon_entertainment.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435", None))
        self.balance_entertainment.setText(QCoreApplication.translate("MainWindow", u"1000 \u0440\u0443\u0431", None))
        self.icon_products.setText("")
        self.label_products.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.balance_product.setText(QCoreApplication.translate("MainWindow", u"1000 \u0440\u0443\u0431", None))
        self.icon_other.setText("")
        self.label_others.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u0438\u0435", None))
        self.balance_others.setText(QCoreApplication.translate("MainWindow", u"1000 \u0440\u0443\u0431", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
    # retranslateUi

