from PyQt5 import QtCore, QtGui, QtWidgets
from view.visualizations.generic_graphic import Widget


class PurchasesGraphicPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(PurchasesGraphicPage, self).__init__(*args)