# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(807, 472)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 778, 380))
        self.MatrixInputLayout = QGridLayout(self.gridLayoutWidget)
        self.MatrixInputLayout.setSpacing(10)
        self.MatrixInputLayout.setObjectName(u"MatrixInputLayout")
        self.MatrixInputLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.MatrixInputLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.MatrixInputLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.MatrixInputLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.textEdit_5 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_5.setObjectName(u"textEdit_5")

        self.MatrixInputLayout.addWidget(self.textEdit_5, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.MatrixInputLayout.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.textEdit_4 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.MatrixInputLayout.addWidget(self.textEdit_4, 1, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.MatrixInputLayout.addWidget(self.textEdit_2, 0, 2, 1, 1)

        self.textEdit_3 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.MatrixInputLayout.addWidget(self.textEdit_3, 0, 3, 1, 1)

        self.textEdit_6 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_6.setObjectName(u"textEdit_6")

        self.MatrixInputLayout.addWidget(self.textEdit_6, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

