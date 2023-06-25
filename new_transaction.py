# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res-new-window-rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(387, 320)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-famaly: Noto Sans SC;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_new_transcription = QLabel(self.frame)
        self.lbl_new_transcription.setObjectName(u"lbl_new_transcription")
        self.lbl_new_transcription.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_new_transcription.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_new_transcription)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setStyleSheet(u"QComboBox{\n"
"font-size: 16px;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item{\n"
"color :black;\n"
"}")

        self.verticalLayout.addWidget(self.cb_category)

        self.data = QDateEdit(self.frame)
        self.data.setObjectName(u"data")
        self.data.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-text: 10px;")
        self.data.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.data.setDate(QDate(2023, 6, 25))

        self.verticalLayout.addWidget(self.data)

        self.le_description = QLineEdit(self.frame)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_description)

        self.le_balace = QLineEdit(self.frame)
        self.le_balace.setObjectName(u"le_balace")
        self.le_balace.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_balace)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"font-size: 16px;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item{\n"
"color :black;\n"
"}")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transcription.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0434\u043e\u0432\u043e\u043b\u044c\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0442\u043e\u0432\u0430\u0440\u044b", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("Dialog", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.le_balace.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
    # retranslateUi

