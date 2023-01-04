from src.classes.FillWindow import FillWindow, QtWidgets
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = FillWindow(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
