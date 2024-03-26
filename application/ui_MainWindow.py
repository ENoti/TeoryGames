# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 628)
        font = QFont()
        font.setFamilies([u"Arial"])
        mainWindow.setFont(font)
        self.actionOpen = QAction(mainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionMinMax = QAction(mainWindow)
        self.actionMinMax.setObjectName(u"actionMinMax")
        self.actionMaxMin = QAction(mainWindow)
        self.actionMaxMin.setObjectName(u"actionMaxMin")
        self.actionDominant = QAction(mainWindow)
        self.actionDominant.setObjectName(u"actionDominant")
        self.actionWeaklyDominant = QAction(mainWindow)
        self.actionWeaklyDominant.setObjectName(u"actionWeaklyDominant")
        self.actionNesh = QAction(mainWindow)
        self.actionNesh.setObjectName(u"actionNesh")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MatrInitLayout = QVBoxLayout()
        self.MatrInitLayout.setSpacing(10)
        self.MatrInitLayout.setObjectName(u"MatrInitLayout")
        self.MatrInitLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.MatrInitLayout.setContentsMargins(10, 10, 10, 10)
        self.ConfirmParamsButton = QPushButton(self.centralwidget)
        self.ConfirmParamsButton.setObjectName(u"ConfirmParamsButton")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.ConfirmParamsButton.setFont(font1)
        self.ConfirmParamsButton.setCheckable(True)

        self.MatrInitLayout.addWidget(self.ConfirmParamsButton)

        self.MatrixParamsHLayout = QHBoxLayout()
        self.MatrixParamsHLayout.setSpacing(5)
        self.MatrixParamsHLayout.setObjectName(u"MatrixParamsHLayout")
        self.MatrixParamsHLayout.setContentsMargins(0, 0, 0, 0)
        self.MatrixParamsVLayout = QVBoxLayout()
        self.MatrixParamsVLayout.setSpacing(10)
        self.MatrixParamsVLayout.setObjectName(u"MatrixParamsVLayout")
        self.MatrixParamsVLayout.setContentsMargins(0, -1, -1, -1)
        self.PlayerNameLayout = QHBoxLayout()
        self.PlayerNameLayout.setSpacing(10)
        self.PlayerNameLayout.setObjectName(u"PlayerNameLayout")
        self.PlayerNameLayout.setContentsMargins(-1, -1, 10, -1)
        self.PlayerLabel = QLabel(self.centralwidget)
        self.PlayerLabel.setObjectName(u"PlayerLabel")
        self.PlayerLabel.setFont(font)
        self.PlayerLabel.setTextFormat(Qt.AutoText)

        self.PlayerNameLayout.addWidget(self.PlayerLabel)

        self.Name1Edit = QLineEdit(self.centralwidget)
        self.Name1Edit.setObjectName(u"Name1Edit")

        self.PlayerNameLayout.addWidget(self.Name1Edit)

        self.Name2Edit = QLineEdit(self.centralwidget)
        self.Name2Edit.setObjectName(u"Name2Edit")

        self.PlayerNameLayout.addWidget(self.Name2Edit)


        self.MatrixParamsVLayout.addLayout(self.PlayerNameLayout)

        self.SizeLayout = QHBoxLayout()
        self.SizeLayout.setSpacing(10)
        self.SizeLayout.setObjectName(u"SizeLayout")
        self.SizeLayout.setContentsMargins(-1, -1, 10, -1)
        self.OptionLabel = QLabel(self.centralwidget)
        self.OptionLabel.setObjectName(u"OptionLabel")
        self.OptionLabel.setFont(font)

        self.SizeLayout.addWidget(self.OptionLabel)

        self.Option1Edit = QLineEdit(self.centralwidget)
        self.Option1Edit.setObjectName(u"Option1Edit")
        self.Option1Edit.setStyleSheet(u"QLineEdit {\n"
"	border-color: rgb(255, 25, 55);\n"
"	border-width: 10px;\n"
"}")

        self.SizeLayout.addWidget(self.Option1Edit)

        self.Option2Edit = QLineEdit(self.centralwidget)
        self.Option2Edit.setObjectName(u"Option2Edit")

        self.SizeLayout.addWidget(self.Option2Edit)


        self.MatrixParamsVLayout.addLayout(self.SizeLayout)


        self.MatrixParamsHLayout.addLayout(self.MatrixParamsVLayout)

        self.BiMatrixButton = QRadioButton(self.centralwidget)
        self.BiMatrixButton.setObjectName(u"BiMatrixButton")
        self.BiMatrixButton.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        self.BiMatrixButton.setFont(font2)
        self.BiMatrixButton.setChecked(False)

        self.MatrixParamsHLayout.addWidget(self.BiMatrixButton)


        self.MatrInitLayout.addLayout(self.MatrixParamsHLayout)

        self.ConfirmMatrixButton = QPushButton(self.centralwidget)
        self.ConfirmMatrixButton.setObjectName(u"ConfirmMatrixButton")
        self.ConfirmMatrixButton.setEnabled(False)
        font3 = QFont()
        font3.setPointSize(16)
        self.ConfirmMatrixButton.setFont(font3)
        self.ConfirmMatrixButton.setCheckable(True)

        self.MatrInitLayout.addWidget(self.ConfirmMatrixButton)

        self.FunctionHLayout = QHBoxLayout()
        self.FunctionHLayout.setSpacing(10)
        self.FunctionHLayout.setObjectName(u"FunctionHLayout")
        self.FunctionHLayout.setContentsMargins(10, 10, 10, 10)
        self.PlayerChoiceBox = QComboBox(self.centralwidget)
        self.PlayerChoiceBox.setObjectName(u"PlayerChoiceBox")

        self.FunctionHLayout.addWidget(self.PlayerChoiceBox)

        self.BufferButton = QPushButton(self.centralwidget)
        self.BufferButton.setObjectName(u"BufferButton")
        self.BufferButton.setCheckable(True)

        self.FunctionHLayout.addWidget(self.BufferButton)


        self.MatrInitLayout.addLayout(self.FunctionHLayout)


        self.verticalLayout.addLayout(self.MatrInitLayout)

        self.MatrixInputLayout = QGridLayout()
        self.MatrixInputLayout.setSpacing(10)
        self.MatrixInputLayout.setObjectName(u"MatrixInputLayout")
        self.MatrixInputLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.MatrixInputLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.MatrixInputLayout)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAlgorithms = QMenu(self.menubar)
        self.menuAlgorithms.setObjectName(u"menuAlgorithms")
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAlgorithms.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuAlgorithms.addAction(self.actionMinMax)
        self.menuAlgorithms.addAction(self.actionMaxMin)
        self.menuAlgorithms.addAction(self.actionDominant)
        self.menuAlgorithms.addAction(self.actionWeaklyDominant)
        self.menuAlgorithms.addAction(self.actionNesh)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u041c\u0430\u0442\u0440\u0438\u0447\u043d\u044b\u0435 \u0438\u0433\u0440\u044b", None))
        self.actionOpen.setText(QCoreApplication.translate("mainWindow", u"Open", None))
        self.actionMinMax.setText(QCoreApplication.translate("mainWindow", u"\u041c\u0438\u043d\u041c\u0430\u043a\u0441", None))
        self.actionMaxMin.setText(QCoreApplication.translate("mainWindow", u"\u041c\u0430\u043a\u0441\u041c\u0438\u043d", None))
        self.actionDominant.setText(QCoreApplication.translate("mainWindow", u"\u0421\u0442\u0440\u043e\u0433\u043e \u0434\u043e\u043c\u0438\u043d\u0438\u0440\u0443\u0435\u043c\u0430\u044f", None))
        self.actionWeaklyDominant.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043b\u0430\u0431\u043e \u0434\u043e\u043c\u0438\u043d\u0438\u0440\u0443\u0435\u043c\u0430\u044f", None))
        self.actionNesh.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0430\u0432\u043d\u043e\u0432\u0435\u0441\u0438\u0435 \u043f\u043e \u041d\u044d\u0448\u0443", None))
        self.ConfirmParamsButton.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.PlayerLabel.setText(QCoreApplication.translate("mainWindow", u"\u0418\u043c\u0435\u043d\u0430 \u0418\u0433\u0440\u043e\u043a\u043e\u0432:          ", None))
        self.OptionLabel.setText(QCoreApplication.translate("mainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u041e\u043f\u0446\u0438\u0439:", None))
        self.BiMatrixButton.setText(QCoreApplication.translate("mainWindow", u"\u0411\u0438\u043c\u0430\u0442\u0440\u0438\u0447\u043d\u0430\u044f", None))
        self.ConfirmMatrixButton.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u0443", None))
        self.BufferButton.setText(QCoreApplication.translate("mainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"File", None))
        self.menuAlgorithms.setTitle(QCoreApplication.translate("mainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u044b", None))
    # retranslateUi

