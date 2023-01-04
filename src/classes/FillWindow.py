from src.classes.MainWindowUI import Ui_MainWindow, QtWidgets
from PyQt5 import QtCore, QtGui
from src.classes.calculate_formulas import *


class FillWindow(Ui_MainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(main_window)
        self.chb = [chb for chb in self.centralwidget.children()
                    if isinstance(chb, QtWidgets.QCheckBox)]
        self.validate_text_field()
        self.connect_widgets()

    def connect_widgets(self):
        for item in self.centralwidget.children():
            if isinstance(item, QtWidgets.QLineEdit):
                item.textChanged.connect(self.set_button_enabled)
            if isinstance(item, QtWidgets.QCheckBox):
                item.clicked.connect(self.set_button_enabled)
        self.pushButton.clicked.connect(self.fill_output_by_click)
        self.pushButton_2.clicked.connect(self.reset_window)

    def set_button_enabled(self):
        if True in [x.isChecked() for x in self.chb] and \
                [x.hasAcceptableInput() for x in self.centralwidget.children()
                 if isinstance(x, QtWidgets.QLineEdit)] == [True, True]:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    def validate_text_field(self):
        for field in self.centralwidget.children():
            if isinstance(field, QtWidgets.QLineEdit):
                rx = QtCore.QRegExp('\d+[.]\d{0,3}|\d+')
                val = QtGui.QRegExpValidator(rx)
                field.setValidator(val)

    def fill_output_by_click(self):
        for item in [x for x in self.chb if x.isChecked()]:
            calculated = calculate(item.text(), get_const(item.text()),
                                   float(self.lineEdit.text()), float(self.lineEdit_2.text()))
            if calculated not in self.textBrowser.toPlainText():
                self.textBrowser.append(calculated)

    def reset_window(self):
        for field in self.centralwidget.children():
            if isinstance(field, (QtWidgets.QLineEdit, QtWidgets.QTextBrowser)):
                field.clear()
            if isinstance(field, QtWidgets.QCheckBox):
                field.setCheckState(False)