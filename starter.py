import sys
from PyQt5 import QtWidgets
from interface.screens.initial import InitialScreen
from handler import main_handler

# Número de linhas do projeto
# 1442


def wrapper():
    app.exec()
    main_handler.close()


if __name__ == '__main__':
    main_handler.drop_all()
    print(main_handler.load())

    app = QtWidgets.QApplication(sys.argv)
    i = InitialScreen()
    i.showFullScreen()
    sys.exit(wrapper())
