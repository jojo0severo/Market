from PyQt5 import QtCore, QtGui, QtWidgets
from view.visualizations.generic_graphic import Widget


class SalesGraphicPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(SalesGraphicPage, self).__init__(*args)