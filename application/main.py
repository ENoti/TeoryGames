import sys
from abc import abstractmethod

import matrix

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QFileDialog, QGridLayout, QLabel
from PySide6.QtGui import QRegularExpressionValidator
from ui_MainWindow import Ui_mainWindow

       
class ManyStateButton:
    def __init__(self, actions: list[object]) -> None:
        self.state = 0
        self._actions = actions
    
    def __call__(self) -> None:
        self._actions[self.state]()
        
        self.state = (self.state + 1) % len(self._actions)
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cur_matrix = None 

        self._ui = Ui_mainWindow()
        self._ui.setupUi(self)

        self._ui.actionOpen.triggered.connect(self.open_file_option)
        self._ui.ConfirmParamsButton.toggled.connect(self.button_params)
        int_validator = QRegularExpressionValidator("[1-9][0-9]*", self)
        self._ui.Option1Edit.setValidator(int_validator)
        self._ui.Option2Edit.setValidator(int_validator)
          
    def enable_params_widgets(self, flag: bool) -> None:
        self._ui.Name1Edit.setEnabled(flag)
        self._ui.Name2Edit.setEnabled(flag)
        self._ui.Option1Edit.setEnabled(flag)
        self._ui.Option2Edit.setEnabled(flag)
        self._ui.BiMatrixButton.setEnabled(flag)

    def button_params(self, flag):
        self.enable_params_widgets(not flag)
        self._ui.ConfirmMatrixButton.setEnabled(flag)
        if flag:
            self._ui.ConfirmParamsButton.setText("Изменить параметры")
            self.render_matix(int(self._ui.Option1Edit.text()), int(self._ui.Option2Edit.text()))
        else:
            self._ui.ConfirmParamsButton.setText("Подтвердить параметры")

    def button_matrix_data(self):
        for i in range(int(self._ui.Option1Edit.text())):
            for j in range(int(self._ui.Option2Edit.text())):
                pass
 
    def render_matix(self, n: int, m: int) -> None:
        name_layout = QGridLayout(self)
        name1 = QLabel(self)
        name1.setText(self._ui.Name1Edit.text())
        name1.setAlignment(Qt.AlignBottom)
        name2 = QLabel(self)
        name2.setText(self._ui.Name2Edit.text())
        name2.setAlignment(Qt.AlignRight)
        name_layout.addWidget(name1, 2, 0)
        name_layout.addWidget(name2, 0, 2)
        self._ui.MatrixInputLayout.addLayout(name_layout, 0, 0)
        for i in range(1, n + 1):
            self._ui.MatrixInputLayout.addWidget(QTextEdit(), i, 0)
        for j in range(1, m + 1):
            self._ui.MatrixInputLayout.addWidget(QTextEdit(), 0, j)

        if self._ui.BiMatrixButton.isChecked():
            validator = QRegularExpressionValidator("-?[1-9][0-9]*, -?[1-9][0-9]*", self)
        else:
            validator = QRegularExpressionValidator("-?[1-9][0-9]*", self)
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                int_cell = QLineEdit()
                int_cell.setValidator(validator)
                self._ui.MatrixInputLayout.addWidget(int_cell, i, j)

    def create_file_dialog(self) -> list[str] | None:
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Текстовые файлы (*.txt)")
        if dialog.exec():
            return dialog.selectedFiles()
        else:
            return None

    def open_file_option(self) -> None: 
        files = self.create_file_dialog()
        if files is not None:
            self.cur_matrix = matrix.Matrix.input_from_file(files[0])

            self._ui.Option1Edit.setText(str(self.cur_matrix.n))
            self._ui.Option2Edit.setText(str(self.cur_matrix.m))
            self._ui.Name1Edit.setText(self.cur_matrix.first_player)
            self._ui.Name2Edit.setText(self.cur_matrix.second_player)
            self._ui.BiMatrixButton.setChecked(self.cur_matrix.bi_matrix)

            self.render_matix(self.cur_matrix.n, self.cur_matrix.m)
            for i, strategy_name in enumerate(self.cur_matrix.first_player_strategies, 1):
                cur_cell =(QTextEdit)(self._ui.MatrixInputLayout.itemAtPosition(0, i).widget())
                cur_cell.setText(strategy_name)
            for i, strategy_name in enumerate(self.cur_matrix.second_player_strategies, 1):
                cur_cell =(QTextEdit)(self._ui.MatrixInputLayout.itemAtPosition(i, 0).widget())
                cur_cell.setText(strategy_name)

            if self.cur_matrix.bi_matrix:
                for i, row in enumerate(self.cur_matrix.matrix, 1):
                    for j, val in enumerate(row, 1):
                        cur_cell =(QTextEdit)(self._ui.MatrixInputLayout.itemAtPosition(i, j).widget())
                        cur_cell.setText(f"{val[0]}, {val[1]}")
            else:
                for i, row in enumerate(self.cur_matrix.matrix, 1):
                    for j, val in enumerate(row, 1):
                        cur_cell =(QTextEdit)(self._ui.MatrixInputLayout.itemAtPosition(i, j).widget())
                        cur_cell.setText(str(val))

                    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
