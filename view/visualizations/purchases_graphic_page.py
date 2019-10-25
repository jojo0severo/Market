import locale
locale.setlocale(locale.LC_MONETARY, '')
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from view.visualizations.generic_graphic import Widget
from controller.graphic_controller import GraphicController


class PurchasesGraphicPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(PurchasesGraphicPage, self).__init__(*args)

        self.back_signal = back_signal
        self.controller = GraphicController()

        # Main
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.graphic = Widget(self)

        self.wrapper_verticalWidget = QtWidgets.QWidget(self, *args)
        self.wrapper_layout = QtWidgets.QVBoxLayout(self.wrapper_verticalWidget)
        self.mean_sales_verticalWidget = QtWidgets.QWidget(self, *args)
        self.mean_sales_layout = QtWidgets.QVBoxLayout(self.mean_sales_verticalWidget)

        # Labels
        self.mean_label = QtWidgets.QLabel(self.mean_sales_verticalWidget)
        self.mean_value_label = QtWidgets.QLabel(self.mean_sales_verticalWidget)

        # Buttons
        self.back_button = QtWidgets.QPushButton(self)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)

        # Main
        self.graphic.setFont(font)
        self.graphic.setMinimumSize(QtCore.QSize(640, 420))
        self.graphic.setMaximumSize(QtCore.QSize(1720, 1200))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHeightForWidth(self.mean_sales_verticalWidget.sizePolicy().hasHeightForWidth())
        self.mean_sales_verticalWidget.setSizePolicy(size_policy)
        self.mean_sales_verticalWidget.setMinimumSize(QtCore.QSize(460, 0))
        self.mean_sales_verticalWidget.setMaximumSize(QtCore.QSize(500, 180))

        # Labels
        self.mean_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.mean_value_label.setMaximumSize(QtCore.QSize(16777215, 70))

        # Buttons
        self.back_button.setMinimumSize(QtCore.QSize(190, 50))
        self.back_button.setMaximumSize(QtCore.QSize(190, 80))
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton {\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    border: 2px solid #C1C0C0;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover:!pressed {\n"
                                       "    background-color: #C1C0C0;\n"
                                       "    color: white;\n"
                                       "    font-weight: bold;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #C1C0C0;\n"
                                       "    color: white;\n"
                                       "    font-weight: bold;\n"
                                       "}")

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.back_button.setText(_translate("MainWindow", "Voltar"))
        self.mean_label.setText(_translate("MainWindow", "Média de compras dos últimos 12 meses"))
        self.mean_value_label.setText(_translate("MainWindow", "0,00"))

    def create_structure(self):
        self.wrapper_layout.addItem(QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum))
        self.mean_sales_layout.addWidget(self.mean_label)
        self.mean_sales_layout.addWidget(self.mean_value_label)
        self.mean_sales_layout.addItem(QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding))
        self.wrapper_layout.addWidget(self.mean_sales_verticalWidget)
        self.wrapper_layout.addItem(QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding))

        self.grid_layout.addWidget(self.graphic, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.wrapper_verticalWidget, 0, 1, 1, 1)
        self.grid_layout.addItem(QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed), 1, 0, 1, 1)
        self.grid_layout.addWidget(self.back_button, 1, 1, 1, 1, QtCore.Qt.AlignRight)

    def define_actions(self):
        self.back_button.clicked.connect(self.back_signal.emit)

    def format(self, value):
        return locale.currency(float(value), grouping=True)

    def clear(self):
        from_date = '/'.join(map(str, [1, 1, datetime.now().year - 1]))
        to_date = '/'.join(map(str, [31, datetime.now().month, datetime.now().year]))

        result, y_labels, x_labels, message = self.controller.get_purchases_by_date(from_date, to_date)
        if not result or not x_labels:
            return

        self.graphic.canvas.axis.plot(x_labels, y_labels)
        self.graphic.canvas.draw()

        mean = sum(y_labels) / len(y_labels)
        self.mean_value_label.setText(self.format(mean))
