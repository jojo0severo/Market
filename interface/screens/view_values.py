from PyQt5 import QtCore, QtGui, QtWidgets
from handler import main_handler


class ViewValuesScreen(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # Column views
        self.sales_column = QtWidgets.QTableWidget(self)
        self.purchases_column = QtWidgets.QTableWidget(self)

        # Dynamic Text
        self.sales_text = QtWidgets.QLabel(self)
        self.purchases_text = QtWidgets.QLabel(self)

        # Spin box
        self.passed_registers = QtWidgets.QSpinBox(self)

        # Labels
        self.sales_total_label = QtWidgets.QLabel(self)
        self.purchases_total_label = QtWidgets.QLabel(self)
        self.spin_label = QtWidgets.QLabel(self)

        # Buttons
        self.back = QtWidgets.QPushButton(self)

        # Initialize
        self.setup_ui()
        self.translate_ui()
        self.set_functions()

    def setup_ui(self):
        """Handle all the styling of the components."""
        # Window
        self.resize(1558, 905)
        self.setStyleSheet("gridline-color: rgb(192, 255, 231);\n"
                           "selection-color: rgb(218, 255, 202);\n"
                           "background-color: rgb(255, 255, 255);")

        # ======================== Column Views Stylesheet ===============================

        # Purchases column with each date
        self.purchases_column.setGeometry(QtCore.QRect(680, 50, 361, 461))
        self.purchases_column.insertColumn(0)
        self.purchases_column.insertColumn(1)
        self.purchases_column.setHorizontalHeaderLabels(['Compra', 'Data'])
        self.purchases_column.horizontalHeader().setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch
        )
        self.purchases_column.horizontalHeader().setSectionResizeMode(
                1, QtWidgets.QHeaderView.Stretch
        )
        self.purchases_column.verticalHeader().setVisible(False)
        self.purchases_column.setAlternatingRowColors(True)
        self.purchases_column.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.purchases_column.cellClicked.connect(lambda x: self.purchases_column.clearSelection())

        # Sales column with each date
        self.sales_column.setGeometry(QtCore.QRect(120, 50, 361, 461))
        self.sales_column.insertColumn(0)
        self.sales_column.insertColumn(1)
        self.sales_column.setHorizontalHeaderLabels(['Venda', 'Data'])
        self.sales_column.horizontalHeader().setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch
        )
        self.sales_column.horizontalHeader().setSectionResizeMode(
                1, QtWidgets.QHeaderView.Stretch
        )
        self.sales_column.verticalHeader().setVisible(False)
        self.sales_column.setAlternatingRowColors(True)
        self.sales_column.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sales_column.cellClicked.connect(lambda x: self.sales_column.clearSelection())

        # ======================== Dynamic text Stylesheet ===============================

        # Label with the total amount of sales on the last 30 registers
        self.sales_text.setGeometry(QtCore.QRect(250, 520, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(17)
        self.sales_text.setFont(font)
        self.sales_text.setStyleSheet("""
                                        QLabel {
                                            border-top: 0px solid;
                                            border-left: 0px solid;
                                            border-right: 0px solid;
                                            border-bottom: 1px solid;
                                            font-family: "Dubai";
                                            font-size: 17pt;
                                        };
                                           """)

        # Label with the total amount of purchases on the last 30 registers
        self.purchases_text.setGeometry(QtCore.QRect(810, 520, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(17)
        self.purchases_text.setFont(font)
        self.purchases_text.setStyleSheet("""
                                            QLabel {
                                                border-top: 0px solid;
                                                border-left: 0px solid;
                                                border-right: 0px solid;
                                                border-bottom: 1px solid;
                                                font-family: "Dubai";
                                                font-size: 17pt;
                                            };
                                               """)

        # ======================== Spin Stylesheet ===============================

        # Spin box with the limit of registers returned
        self.passed_registers.setGeometry(QtCore.QRect(1070, 150, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(16)
        self.passed_registers.setFont(font)
        self.passed_registers.setMaximum(365)
        self.passed_registers.setMinimum(1)
        self.passed_registers.valueChanged.connect(self.update_tables)

        # ======================== Labels Stylesheet ===============================

        # Label to the sales
        self.sales_total_label.setGeometry(QtCore.QRect(680, 520, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(19)
        self.sales_total_label.setFont(font)

        # Label to the purchases
        self.purchases_total_label.setGeometry(QtCore.QRect(120, 520, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(19)
        self.purchases_total_label.setFont(font)

        # Label to the spin box
        self.spin_label.setGeometry(QtCore.QRect(1050, 50, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(17)
        self.spin_label.setFont(font)

        # ======================== Buttons Stylesheet ===============================

        # Button to go back one screen
        self.back.setGeometry(QtCore.QRect(1040, 620, 231, 111))
        font = QtGui.QFont()
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton\n"
                                "{\n"
                                "  background-color: white;\n"
                                "  color: black; \n"
                                "  border: none;\n"
                                "  margin: 4px 2px;\n"
                                "  text-align: center;\n"
                                "  font-size: 24px;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover:!pressed\n"
                                "{\n"
                                "background-color: #989898;\n"
                                "color: white;\n"
                                "font-weight: bold;\n"
                                "}")

    def translate_ui(self):
        """Assign names and formats to the components."""

        # ======================== Spin Stylesheet ===============================

        self.passed_registers.setValue(30)

        # ============================= Window ===========================================

        self.setWindowTitle("Dois irmãos")

        # ======================== Labels Stylesheet ===============================

        self.sales_total_label.setText("Total")
        self.purchases_total_label.setText("Total")
        self.spin_label.setText("Quantidade de registros a ser exibida")

        # ======================== Buttons Stylesheet ===============================

        self.back.setText("Voltar")

    def set_functions(self):
        """Assign functions to the buttons."""
        self.back.clicked.connect(self.back_function)

    def back_function(self):
        """Go back one screen."""
        self.close()

    def update_tables(self):
        total_sales, list_sale, list_date_sale = main_handler.consult_x_by_day(
                'sales', self.passed_registers.value())
        total_purchases, list_purchase, list_date_purchase = main_handler.consult_x_by_day(
                'purchases', self.passed_registers.value())

        self.sales_column.setRowCount(0)
        for sale, date in zip(list_sale, list_date_sale):
            row = self.sales_column.rowCount()
            self.sales_column.insertRow(row)
            sale_item = QtWidgets.QTableWidgetItem(sale)
            sale_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.sales_column.setItem(row, 0, sale_item)

            date_item = QtWidgets.QTableWidgetItem(date)
            date_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.sales_column.setItem(row, 1, date_item)

        self.sales_column.clearFocus()
        self.sales_column.clearSelection()

        self.purchases_column.setRowCount(0)
        for purchase, date in zip(list_purchase, list_date_purchase):
            row = self.purchases_column.rowCount()
            self.purchases_column.insertRow(row)
            purchase_item = QtWidgets.QTableWidgetItem(purchase)
            purchase_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.purchases_column.setItem(row, 0, purchase_item)

            date_item = QtWidgets.QTableWidgetItem(date)
            date_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.purchases_column.setItem(row, 1, date_item)

        self.purchases_column.clearFocus()
        self.purchases_column.clearSelection()

        # ======================== Dynamic texts Stylesheet ===============================

        self.sales_text.setText(str(total_sales))
        self.purchases_text.setText(str(total_purchases))
