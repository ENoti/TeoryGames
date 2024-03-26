from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QRegularExpressionValidator)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget, QTextEdit, QComboBox)

class FunctionParamsrender:
    def __init__(self, parentLayout: QHBoxLayout) -> None:
        self.parent = parentLayout


    def render_choice(self, choices: list[str]) -> None:
        choices_widget = QComboBox()
        choices_widget.addItems(choices)
        self.parent.addWidget(choices_widget)
    
    def render_buffer_button(self, func) -> None:
        buffer_button = QPushButton()
        buffer_button.setObjectName(u"ConfirmParamsButton")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(False)
        buffer_button.setFont(font1)
        buffer_button.setCheckable(True)
        buffer_button.toggled.connect(func)
        self.parent.addWidget(buffer_button)
    
    def clear_widgets(self) -> None:
        print(self.parent.children())