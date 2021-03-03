import csv
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import main_ui
import main as functions


class App(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        RBCos = self.RBCos
        RBCos.name_function = "cos"
        RBCos.toggled.connect(self.on_clicked_rb)
        RBSin = self.RBSin
        RBSin.name_function = "sin"
        RBSin.toggled.connect(self.on_clicked_rb)
        RBExp = self.RBExp
        RBExp.name_function = "exp"
        RBExp.toggled.connect(self.on_clicked_rb)
        RBCustom = self.RBCustom
        RBCustom.name_function = "custom"
        RBCustom.toggled.connect(self.on_clicked_rb)

        BtnCreate = self.BtnCreate
        BtnCreate.name = 'linear'
        BtnCreate.clicked.connect(self.on_btn_clicked)

        BtnSpline = self.BtnSpline
        BtnSpline.name = 'spline'
        BtnSpline.clicked.connect(self.on_btn_clicked)

        BtnFilerChooser = self.BtnChooseFile
        BtnFilerChooser.clicked.connect(self.open_file_name_dialog)
        RBFileChooserMode = self.RBChoseFileMode
        RBFileChooserMode.toggled.connect(self.rb_mode)
        RBCustomMode = self.RBCustomMode
        RBCustomMode.toggled.connect(self.rb_mode)

        self.model = QtGui.QStandardItemModel(self)

        self.array_from_file = list()
        self.array_convert_data = list()

    def rb_mode(self):
        if self.RBChoseFileMode.isChecked():
            self.field_is_enabled(False)
        if self.RBCustomMode.isChecked():
            self.field_is_enabled(True)

    def field_is_enabled(self, isEnable: bool):
        self.TEAfter.setEnabled(isEnable)
        self.TEBefore.setEnabled(isEnable)
        self.TEHeight.setEnabled(isEnable)
        if self.RBCustom.isChecked() and self.RBCustomMode.isChecked():
            self.TEFunc.setEnabled(True)
        else:
            self.TEFunc.setEnabled(False)
        self.RBSin.setEnabled(isEnable)
        self.RBExp.setEnabled(isEnable)
        self.RBCos.setEnabled(isEnable)
        self.RBCustom.setEnabled(isEnable)

        self.BtnChooseFile.setEnabled(not isEnable)
        self.BtnCreate.setEnabled(isEnable)
        self.BtnSpline.setEnabled(isEnable)

    def on_clicked_rb(self):
        RB = self.sender()
        if RB.isChecked():
            if RB.name_function == "custom":
                self.TEFunc.setEnabled(True)

            else:
                self.TEFunc.setEnabled(False)

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.TEFileName.setText(fileName)
            self.BtnSpline.setEnabled(True)
            self.BtnCreate.setEnabled(True)
            self.load_csv(fileName)

    def load_csv(self, file_name):
        with open(file_name, "r") as fileInput:
            try:
                for row in csv.reader(fileInput, delimiter=';'):
                    self.array_from_file.append(row)
                print(self.array_from_file)
            except:
                self.show_dialog_error("Ошибка чтения файла")

    def on_btn_clicked(self):
        x_before = self.TEBefore.text()
        x_after = self.TEAfter.text()
        x_height = self.TEHeight.text()
        btn_name = self.sender().name
        custom_function = self.TEFunc.text()
        print(self.TEAfter.text())
        if self.RBCustomMode.isChecked():
            if x_after == '' or x_before == '' or x_height == '':
                if self.TEAfter.text() == '':
                    self.TEAfter.setStyleSheet("border: 1px solid red;")
                if self.TEBefore.text() == '':
                    self.TEBefore.setStyleSheet("border: 1px solid red;")
                if self.TEHeight.text() == '':
                    self.TEHeight.setStyleSheet("border: 1px solid red;")
                self.show_dialog_error("Заполните поля")
            elif self.RBCustom.isChecked():
                functions.create_function_from_text(btn_name=btn_name, function=custom_function,
                                                    x_before=float(x_before), x_after=float(x_after),
                                                    x_height=int(x_height))
            else:
                if self.RBSin.isChecked():
                    functions.choose_function(btn_name=btn_name, function_name="sin", x_before=float(x_before),
                                              x_after=float(x_after),
                                              x_height=int(x_height))
                elif self.RBCos.isChecked():
                    functions.choose_function(btn_name=btn_name, function_name="cos", x_before=float(x_before),
                                              x_after=float(x_after),
                                              x_height=int(x_height))
                else:
                    functions.choose_function(btn_name=btn_name, function_name="exp", x_before=float(x_before),
                                              x_after=float(x_after),
                                              x_height=int(x_height))
        elif self.RBChoseFileMode.isChecked():
            try:
                if self.array_from_file[0][0].lower() != 'x':
                    raise Exception("Отсутствует символ маркер \'x\'")
                if self.array_from_file[1][0].lower() != 'y':
                    raise Exception("Отсутствует символ маркер \'y\'")
                del self.array_from_file[0][0]
                del self.array_from_file[1][0]
                functions.get_data_from_file(btn_name, self.array_from_file[0], self.array_from_file[1],
                                             len(self.array_from_file[0]))
            except Exception as e:
                self.show_dialog_error(str(e))

    def show_dialog_error(self, textError):
        QMessageBox.critical(self, "Ошибка", textError)
        self.TEAfter.setStyleSheet("border: 1px solid black;")
        self.TEBefore.setStyleSheet("border: 1px solid black;")
        self.TEHeight.setStyleSheet("border: 1px solid black;")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
