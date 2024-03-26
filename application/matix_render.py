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
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget, QTextEdit)


class MatrixNamesCell(QGridLayout):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        name1Label = QLabel()
        name1Label.setAlignment(Qt.AlignBottom)
        self.addWidget(name1Label, 2, 0)
        name2Label = QLabel()
        name2Label.setAlignment(Qt.AlignRight)
        self.addWidget(name2Label, 0, 2)

  
    def set_state(self, name1: str, name2: str) -> None:
        self.itemAtPosition(2, 0).widget().setText(name1)
        self.itemAtPosition(0, 2).widget().setText(name2)


class MatrixStrategiesCell(QTextEdit):
    def __ini__(self) -> None:
        super.__init__()


class MatrixNumCell(QLineEdit):
    MATR_VALIDATOR = QRegularExpressionValidator("-?[0-9]*")
    BIMATR_VALIDATOR = QRegularExpressionValidator("-?[0-9]*, -?[0-9]*")

    def __init__(self, is_bi: bool) -> None:
        super().__init__()
        self.set_state(is_bi)

    def _obj_set_state(self, validator: QRegularExpressionValidator) -> None:
        self.setText("")
        self.setValidator(validator)

    def set_state(self, is_bi: bool) -> None:
        if is_bi:
            self._obj_set_state(MatrixNumCell.BIMATR_VALIDATOR)
        else:
            self._obj_set_state(MatrixNumCell.MATR_VALIDATOR)
    

class MatrixRender(object):
    def __init__(self, parentLayout: QGridLayout) -> None:
        self.matrixLayout = parentLayout
        self.matrixLayout.addLayout(MatrixNamesCell(None), 0, 0)
        self.is_bi = True
        self.rows = 1
        self.columns = 1
    
    def _add_columns(self, columns: int) -> None:
        for j in range(self.columns, columns):
            self.matrixLayout.addWidget(MatrixStrategiesCell(), 0, j)

        for i in range(1, self.rows):
            for j in range(self.columns, columns):
                self.matrixLayout.addWidget(MatrixNumCell(self.is_bi), i, j)

    def _delete_columns(self, columns: int) -> None:
        for j in range(columns, self.columns):
            self.matrixLayout.itemAtPosition(0, j).widget().deleteLater()

        for i in range(1, self.rows):
            for j in range(columns, self.columns):
                self.matrixLayout.itemAtPosition(i, j).widget().deleteLater()

    def _add_rows(self, rows: int) -> None:
        for i in range(self.rows, rows):
            self.matrixLayout.addWidget(MatrixStrategiesCell(), i, 0)

        for i in range(self.rows, rows):
            for j in range(1, self.columns):
                self.matrixLayout.addWidget(MatrixNumCell(self.is_bi), i, j)
    
    def _delete_rows(self, rows: int) -> None:
        for i in range(rows, self.rows):
            self.matrixLayout.itemAtPosition(i, 0).widget().deleteLater()

        for i in range(rows, self.rows):
            for j in range(1, self.columns):
                self.matrixLayout.itemAtPosition(i, j).widget().deleteLater()

    def _remake(self) -> None:
        for i in range(1, self.matrixLayout.rowCount()):
            self.matrixLayout.itemAtPosition(i, 0).widget().setText("")

        for j in range(1, self.matrixLayout.columnCount()):
            self.matrixLayout.itemAtPosition(0, j).widget().setText("")

        for i in range(1, self.matrixLayout.rowCount()):
            for j in range(1, self.matrixLayout.columnCount()):
                self.matrixLayout.itemAtPosition(i, j).widget().set_state(self.is_bi)

    def render(self, name1: str, name2: str, is_bi: bool, rows: int, columns: int) -> None:
        # self.matrixLayout.itemAtPosition(0,0).layout().set_state(name1, name2)
        self.matrixLayout.children()[0].set_state(name1, name2)
        
        if self.columns > columns:
            self._delete_columns(columns)
        elif self.columns < columns:
            self._add_columns(columns)
        self.columns = columns

        if self.rows > rows:
            self._delete_rows(rows)
        elif self.rows < rows:
            self._add_rows(rows)
        self.rows = rows

        if is_bi is not self.is_bi:
            self.is_bi = is_bi
            self._remake()

    def get_strategies(self) -> list[list[str]]:
        return [
            [self.matrixLayout.itemAtPosition(i, 0).widget().toPlainText() for i in range(1, self.rows)],
            [self.matrixLayout.itemAtPosition(0, j).widget().toPlainText() for j in range(1, self.columns)]
        ]

    def get_weights(self):
        res = [None] * (self.rows - 1)
        for i in range(1, self.rows):
            line = [None] * (self.columns - 1)
            for j in range(1, self.columns):
                if self.is_bi:
                    line[j - 1] = [int(val) for val in self.matrixLayout.itemAtPosition(i, j).widget().text().split(", ")]
                else:
                    line[j - 1] = int(self.matrixLayout.itemAtPosition(i, j).widget().text())
            res[i - 1] = line
        
        return res