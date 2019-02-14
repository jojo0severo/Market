"""Project developed to manage the profits, expenses and earnings of a store. Lines: 1442."""

import sys
import sqlite3
from PyQt5 import QtWidgets


if __name__ == '__main__':
    try:
        from interface.screens.initial import InitialScreen
        from handler import main_handler

        main_handler.load()

        app = QtWidgets.QApplication(sys.argv)
        i = InitialScreen()
        i.showFullScreen()
        sys.exit(app.exec())

    except sqlite3.OperationalError:
        app = QtWidgets.QApplication(sys.argv)
        aux = QtWidgets.QMessageBox()
        aux.setWindowTitle('Erro')
        aux.setText('Não foi possível conectar com o dispositivo de armazenamento. \nPor favor '
                    'verifique se o mesmo est;a conectado corretamente ao computador e inicie '
                    'novamente o programa.')
        aux.showNormal()
        sys.exit(app.exec())
