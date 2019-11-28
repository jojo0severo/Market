import sys
import sqlite3
from PyQt5 import QtWidgets
from view.main_window import AppMainWindow


def setup_sql():
    try:
        db = sqlite3.connect('data/marketdb.db')
        db.executescript(open('resources/marketdb.sql', 'r').read())
        db.commit()

    except sqlite3.OperationalError:
        pass

    try:
        db = sqlite3.connect('data/webdb.db')
        db.executescript(open('resources/webdb.sql', 'r').read())
        db.commit()

    except sqlite3.OperationalError:
        pass


if __name__ == '__main__':
    setup_sql()

    APP = QtWidgets.QApplication(sys.argv)
    app = AppMainWindow()
    app.showMaximized()
    sys.exit(APP.exec())
