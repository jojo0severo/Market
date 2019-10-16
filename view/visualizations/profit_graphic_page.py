from PyQt5 import QtCore, QtGui, QtWidgets
from view.visualizations.generic_graphic import Widget


class ProfitGraphicPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(ProfitGraphicPage, self).__init__(*args)

        self.back_signal = back_signal

        # Main
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.graphics_view = QtWidgets.QGraphicsView(self)

        # Buttons
        self.back_button = QtWidgets.QPushButton(self)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        pass

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.back_button.setText(_translate("MainWindow", "Voltar"))

    def create_structure(self):
        self.grid_layout.addWidget(self.graphics_view, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.back_button, 1, 0, 1, 1)

    def define_actions(self):
        self.back_button.clicked.connect(self.back_signal.emit)
