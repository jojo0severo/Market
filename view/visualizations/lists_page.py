from PyQt5 import QtCore, QtGui, QtWidgets
from view.visualizations.generic_graphic import Widget


class ListsPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(ListsPage, self).__init__(*args)

        self.back_signal = back_signal

        # Main
        self.grid_layout = QtWidgets.QGridLayout(self)

        self.date_input_verticalWidget = QtWidgets.QWidget(self, *args)
        self.date_input_layout = QtWidgets.QVBoxLayout(self.date_input_verticalWidget)

        self.tables_gridWidget = QtWidgets.QWidget(self, *args)
        self.tables_layout = QtWidgets.QGridLayout(self.tables_gridWidget)

        self.purchases_table = QtWidgets.QTableWidget(self.tables_gridWidget)
        self.sales_table = QtWidgets.QTableWidget(self.tables_gridWidget)

        self.total_purchases_horizontalWidget = QtWidgets.QWidget(self.tables_gridWidget, *args)
        self.total_purchases_layout = QtWidgets.QHBoxLayout(self.total_purchases_horizontalWidget)

        self.total_sales_horizontalWidget = QtWidgets.QWidget(self.tables_gridWidget, *args)
        self.total_sales_layout = QtWidgets.QHBoxLayout(self.total_sales_horizontalWidget)

        # Labels
        self.from_date_label = QtWidgets.QLabel(self.date_input_verticalWidget)
        self.to_date_label = QtWidgets.QLabel(self.date_input_verticalWidget)

        self.purchases_label = QtWidgets.QLabel(self.tables_gridWidget)
        self.sales_label = QtWidgets.QLabel(self.tables_gridWidget)

        self.total_purchases_label = QtWidgets.QLabel(self.total_purchases_horizontalWidget)
        self.total_purchases_value_label = QtWidgets.QLabel(self.total_purchases_horizontalWidget)

        self.total_sales_label = QtWidgets.QLabel(self.total_sales_horizontalWidget)
        self.total_sales_value_label = QtWidgets.QLabel(self.total_sales_horizontalWidget)

        # Buttons
        self.back_button = QtWidgets.QPushButton(self)

        # Inputs
        self.from_date_option = QtWidgets.QDateEdit(self.date_input_verticalWidget)
        self.to_date_option = QtWidgets.QDateEdit(self.date_input_verticalWidget)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        # Main
        self.tables_gridWidget.setMinimumSize(QtCore.QSize(400, 450))
        self.purchases_table.setMaximumSize(QtCore.QSize(400, 1080))
        self.sales_table.setMaximumSize(QtCore.QSize(400, 1080))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHeightForWidth(self.total_purchases_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.total_purchases_horizontalWidget.setSizePolicy(size_policy)
        self.total_purchases_horizontalWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.total_purchases_horizontalWidget.setMaximumSize(QtCore.QSize(250, 70))

        size_policy.setHeightForWidth(self.total_sales_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.total_sales_horizontalWidget.setSizePolicy(size_policy)
        self.total_sales_horizontalWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.total_sales_horizontalWidget.setMaximumSize(QtCore.QSize(250, 70))

        # Labels
        self.from_date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.to_date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.total_purchases_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.total_purchases_value_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.total_sales_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.total_sales_value_label.setMaximumSize(QtCore.QSize(16777215, 70))

        # Buttons
        self.back_button.setMinimumSize(QtCore.QSize(150, 50))
        self.back_button.setMaximumSize(QtCore.QSize(180, 70))
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

        # Inputs
        self.from_date_option.setMinimumSize(QtCore.QSize(170, 50))
        self.from_date_option.setMaximumSize(QtCore.QSize(190, 70))
        self.from_date_option.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.from_date_option.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.from_date_option.setDate(QtCore.QDate(2018, 1, 1))
        self.from_date_option.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.from_date_option.setDate(QtCore.QDate(2018, 1, 1))

        self.to_date_option.setMinimumSize(QtCore.QSize(170, 50))
        self.to_date_option.setMaximumSize(QtCore.QSize(190, 70))
        self.to_date_option.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.to_date_option.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.to_date_option.setDate(QtCore.QDate(2018, 2, 1))
        self.to_date_option.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.from_date_label.setText(_translate("MainWindow", "Desde"))
        self.to_date_label.setText(_translate("MainWindow", "Até"))
        self.purchases_label.setText(_translate("MainWindow", "Compras"))
        self.sales_label.setText(_translate("MainWindow", "Vendas"))
        self.back_button.setText(_translate("MainWindow", "Voltar"))
        self.total_purchases_label.setText(_translate("MainWindow", "Total de Compras:     R$"))
        self.total_purchases_value_label.setText(self.get_purchases_total())
        self.total_sales_label.setText(_translate("MainWindow", "Total de Vendas:     R$"))
        self.total_sales_value_label.setText(self.get_sales_total())

    def create_structure(self):
        self.date_input_layout.addWidget(self.from_date_label)
        self.date_input_layout.addWidget(self.from_date_option)
        self.date_input_layout.addWidget(self.to_date_label)
        self.date_input_layout.addWidget(self.to_date_option)
        self.date_input_layout.addItem(
            QtWidgets.QSpacerItem(20, 460, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred))

        self.total_purchases_layout.addWidget(self.total_purchases_label)
        self.total_purchases_layout.addWidget(self.total_purchases_value_label)
        self.total_sales_layout.addWidget(self.total_sales_label)
        self.total_sales_layout.addWidget(self.total_sales_value_label)

        self.tables_layout.addWidget(self.purchases_label, 0, 0, 1, 1)
        self.tables_layout.addWidget(self.purchases_table, 1, 0, 1, 1)
        self.tables_layout.addWidget(self.total_purchases_horizontalWidget, 2, 0, 1, 1)
        self.tables_layout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum), 1, 1, 1, 1)
        self.tables_layout.addWidget(self.sales_label, 0, 2, 1, 1)
        self.tables_layout.addWidget(self.sales_table, 1, 2, 1, 1)
        self.tables_layout.addWidget(self.total_sales_horizontalWidget, 2, 2, 1, 1)

        self.grid_layout.addWidget(self.tables_gridWidget, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.date_input_verticalWidget, 0, 1, 1, 1)
        self.grid_layout.addItem(
            QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred), 1, 0, 1,
            1)
        self.grid_layout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred), 2, 0, 1, 1)
        self.grid_layout.addWidget(self.back_button, 2, 1, 1, 1)

    def define_actions(self):
        self.back_button.clicked.connect(self.back_signal.emit)

    def get_purchases_total(self):
        return '0,00'

    def get_sales_total(self):
        return '0,00'


if __name__ == '__main__':
    import sys

    APP = QtWidgets.QApplication(sys.argv)
    app = ListsPage()
    app.show()
    sys.exit(APP.exec())
