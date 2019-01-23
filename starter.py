"""Project developed to manage the profits, expenses and earnings of a store. Lines: 1442."""

import sys
from PyQt5 import QtWidgets
from interface.screens.initial import InitialScreen
from handler import main_handler


if __name__ == '__main__':
    # main_handler.drop_all()
    main_handler.load()

    app = QtWidgets.QApplication(sys.argv)
    i = InitialScreen()
    i.showFullScreen()
    sys.exit(app.exec())
