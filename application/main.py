import sys
import copy
from abc import abstractmethod

import addons.matrix as matrix
import addons.algos as algos
import matix_render
import function_params_render

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QFileDialog, QGridLayout, QLabel, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from ui_MainWindow import Ui_mainWindow

      
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cur_matrix = None
        self.buf_matrix = None 

        self._ui = Ui_mainWindow()
        self._ui.setupUi(self)
        self._matrix_render = matix_render.MatrixRender(self._ui.MatrixInputLayout)
        self._info_message = QMessageBox(QMessageBox.Icon(0), "", "", parent=self)

        self._ui.actionOpen.triggered.connect(self.open_file_option)
        self._ui.actionMaxMin.triggered.connect(self.maxMin_option)
        self._ui.actionMinMax.triggered.connect(self.minMax_option)
        self._ui.actionDominant.triggered.connect(self.dominant_option)
        self._ui.actionWeaklyDominant.triggered.connect(self.weakly_dominant_option)
        self._ui.actionNesh.triggered.connect(self.nesh_option)

        self._ui.PlayerChoiceBox.addItems(["Игрок 1", "игрок 2"])

        self._ui.ConfirmParamsButton.toggled.connect(self.button_params)
        self._ui.ConfirmMatrixButton.toggled.connect(self.button_matrix_data)
        self._ui.BufferButton.toggled.connect(self.button_buffer)

        int_validator = QRegularExpressionValidator("[1-9][0-9]*", self)
        self._ui.Option1Edit.setValidator(int_validator)
        self._ui.Option2Edit.setValidator(int_validator)

    def show_message(self, icon: QMessageBox.Icon, title: str, text: str):
        self._info_message.setIcon(icon)
        self._info_message.setWindowTitle(title)
        self._info_message.setText(text)
        self._info_message.exec()
       
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
                self.show_message(QMessageBox.Icon.Critical, "Ошибка ввода", "Убедитесь, что все поля заполнены корректно")
                self._ui.ConfirmMatrixButton.setChecked(False)
        else:
            self._ui.ConfirmMatrixButton.setText("Подтвердить матрицу")

    def button_buffer(self, flag) -> None:
        if flag:
            if self.buf_matrix is not None:
                self._load_from_obj(self.buf_matrix)
            self._ui.BufferButton.setText("Изначальная матрица")
        else:
            if self.cur_matrix is not None:
                self._load_from_obj(self.cur_matrix)
            self._ui.BufferButton.setText("Посмотреть результат")

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
            self._load_from_obj(self.cur_matrix)

    def _load_from_obj(self, matrix: matrix.Matrix) -> None:
        self._ui.ConfirmParamsButton.setChecked(False)

        self._ui.Option1Edit.setText(str(matrix.n))
        self._ui.Option2Edit.setText(str(matrix.m))
        self._ui.Name1Edit.setText(matrix.first_player)
        self._ui.Name2Edit.setText(matrix.second_player)
        self._ui.BiMatrixButton.setChecked(matrix.bi_matrix)
        self._ui.ConfirmParamsButton.setChecked(True)

        for i, strategy_name in enumerate(matrix.first_player_strategies, 1):
            self._ui.MatrixInputLayout.itemAtPosition(i, 0).widget().setText(strategy_name)
        
        for i, strategy_name in enumerate(matrix.second_player_strategies, 1):
            self._ui.MatrixInputLayout.itemAtPosition(0, i).widget().setText(strategy_name)

            for i, row in enumerate(matrix.matrix, 1):
                for j, val in enumerate(row, 1):
                    cur_cell = self._ui.MatrixInputLayout.itemAtPosition(i, j).widget()
                    if matrix.bi_matrix:
                        cur_cell.setText(f"{val[0]}, {val[1]}")
                    else:
                        cur_cell.setText(str(val))
        self._ui.ConfirmMatrixButton.setChecked(True)

    def maxMin_option(self) -> None:
        if self.cur_matrix is not None:
            res = algos.maximin(self.cur_matrix, self._ui.PlayerChoiceBox.currentIndex())
            self.show_message(QMessageBox.Icon.Information, "Результат", str(res))

    def minMax_option(self) -> None:
        if self.cur_matrix is not None:
            res = algos.minimax(self.cur_matrix, self._ui.PlayerChoiceBox.currentIndex())
            self.show_message(QMessageBox.Icon.Information, "Результат", str(res))
        else:
            self.show_message(QMessageBox.Icon.Critical, "Ошибка ввода", "Убедитесь, что все поля заполнены корректно")

    def dominant_option(self) -> None:
        if self.cur_matrix is not None:
            self.buf_matrix = algos.dominant(self.cur_matrix, self._ui.PlayerChoiceBox.currentIndex())
        else:
            self.show_message(QMessageBox.Icon.Critical, "Ошибка ввода", "Убедитесь, что все поля заполнены корректно")

    def weakly_dominant_option(self) -> None:
        if self.cur_matrix is not None:
            self.buf_matrix = algos.weaklyDominant(self.cur_matrix, self._ui.PlayerChoiceBox.currentIndex())
        else:
            self.show_message(QMessageBox.Icon.Critical, "Ошибка ввода", "Убедитесь, что все поля заполнены корректно")

    def nesh_option(self) -> None:
        if self.cur_matrix is not None:
            res = algos.nesh(self.cur_matrix)
            if res is None:
                self.show_message(QMessageBox.Icon.Information, "Результат", "Равновесие по Нэшу не найдено")
            else:
                cel_val = self._ui.MatrixInputLayout.itemAtPosition(res[0] + 1, res[1] + 1).widget().text()
                self.show_message(QMessageBox.Icon.Information, "Результат", f"Равновесие по Нэшу - ({cel_val})")
        else:
            self.show_message(QMessageBox.Icon.Critical, "Ошибка ввода", "Убедитесь, что все поля заполнены корректно")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
