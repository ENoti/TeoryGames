import sys
from abc import abstractmethod

import addons.matrix as matrix
import matix_render

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QFileDialog, QGridLayout, QLabel, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from ui_MainWindow import Ui_mainWindow

      
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cur_matrix = None 

        self._ui = Ui_mainWindow()
        self._ui.setupUi(self)
        self._matrix_render = matix_render.MatrixRender(self._ui.MatrixInputLayout)

        self._ui.actionOpen.triggered.connect(self.open_file_option)
        self._ui.ConfirmParamsButton.toggled.connect(self.button_params)
        self._ui.ConfirmMatrixButton.toggled.connect(self.button_matrix_data)
        int_validator = QRegularExpressionValidator("[1-9][0-9]*", self)
        self._ui.Option1Edit.setValidator(int_validator)
        self._ui.Option2Edit.setValidator(int_validator)
          
    def enable_params_widgets(self, flag: bool) -> None:
        self._ui.Name1Edit.setEnabled(flag)
        self._ui.Name2Edit.setEnabled(flag)
        self._ui.Option1Edit.setEnabled(flag)
        self._ui.Option2Edit.setEnabled(flag)
        self._ui.BiMatrixButton.setEnabled(flag)

    def button_params(self, flag) -> None:
        self.enable_params_widgets(not flag)
        self._ui.ConfirmMatrixButton.setEnabled(flag)
        if flag:
            self._ui.ConfirmParamsButton.setText("Изменить параметры")
            self._matrix_render.render(self._ui.Name1Edit.text(),
                                    self._ui.Name2Edit.text(),
                                    self._ui.BiMatrixButton.isChecked(), 
                                    int(self._ui.Option1Edit.text()) + 1,
                                    int(self._ui.Option2Edit.text()) + 1)
        else:
            self._ui.ConfirmParamsButton.setText("Подтвердить параметры")
            self._ui.ConfirmMatrixButton.setChecked(False)

    def button_matrix_data(self, flag) -> None:
        if flag:
            self._ui.ConfirmMatrixButton.setText("Изменить матрицу")
            strategies = self._matrix_render.get_strategies()
            try:
                self.cur_matrix = matrix.Matrix(int(self._ui.Option1Edit.text()),
                                                int(self._ui.Option2Edit.text()),
                                                self._ui.BiMatrixButton.isChecked(),
                                                self._matrix_render.get_weights(),
                                                self._ui.Name1Edit.text(),
                                                self._ui.Name2Edit.text(),
                                                strategies[0],
                                                strategies[1])
            except Exception as e:
                errMessge = QMessageBox(QMessageBox.Icon(2), "Ошибка ввода", "Убедитесь, что все поля заполнены корректно.", parent=self)
                errMessge.exec()
                self._ui.ConfirmMatrixButton.setChecked(False)
        else:
            self._ui.ConfirmMatrixButton.setText("Подтвердить матрицу")

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
            self._ui.ConfirmParamsButton.setChecked(True)

            for i, strategy_name in enumerate(self.cur_matrix.first_player_strategies, 1):
                cur_cell = self._ui.MatrixInputLayout.itemAtPosition(0, i).widget().setText(strategy_name)
            for i, strategy_name in enumerate(self.cur_matrix.second_player_strategies, 1):
                cur_cell = self._ui.MatrixInputLayout.itemAtPosition(i, 0).widget().setText(strategy_name)

                for i, row in enumerate(self.cur_matrix.matrix, 1):
                    for j, val in enumerate(row, 1):
                        cur_cell =self._ui.MatrixInputLayout.itemAtPosition(i, j).widget()
                        if self.cur_matrix.bi_matrix:
                            cur_cell.setText(f"{val[0]}, {val[1]}")
                        else:
                            cur_cell.setText(str(val))
            self._ui.ConfirmMatrixButton.setChecked(True)

                       
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
