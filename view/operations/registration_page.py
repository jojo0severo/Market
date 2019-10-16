from PyQt5 import QtCore, QtGui, QtWidgets


class RegistrationPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(RegistrationPage, self).__init__(*args)

        self.back_signal = back_signal

        # Declaring main objects
        self.grid_layout = QtWidgets.QGridLayout(self)

        self.form = QtWidgets.QWidget(self, *args)
        self.form_layout = QtWidgets.QGridLayout(self.form)

        self.purchase_sale_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.purchase_sale_layout = QtWidgets.QHBoxLayout(self.purchase_sale_horizontalWidget)

        self.coin_input_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.coin_input_layout = QtWidgets.QHBoxLayout(self.coin_input_horizontalWidget)

        self.bottom_buttons_horizontalWidget = QtWidgets.QWidget(self, *args)
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout(self.bottom_buttons_horizontalWidget)

        # Declaring Labels
        self.page_title = QtWidgets.QLabel(self)
        self.transaction_label = QtWidgets.QLabel(self.form)
        self.date_label = QtWidgets.QLabel(self.form)
        self.value_label = QtWidgets.QLabel(self.form)
        self.product_name_label = QtWidgets.QLabel(self.form)
        self.coin_label = QtWidgets.QLabel(self.coin_input_horizontalWidget)

        # Declaring buttons
        self.register_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)
        self.back_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)

        # Declaring inputs
        self.product_name_option = QtWidgets.QTextEdit(self.form)
        self.date_option = QtWidgets.QDateEdit(self.form)
        self.value_option = QtWidgets.QTextEdit(self.coin_input_horizontalWidget)
        self.sale_option = QtWidgets.QRadioButton(self.purchase_sale_horizontalWidget)
        self.purchase_option = QtWidgets.QRadioButton(self.purchase_sale_horizontalWidget)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        # Main
        self.form.setMinimumSize(QtCore.QSize(300, 500))
        self.purchase_sale_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.coin_input_horizontalWidget.setMaximumSize(QtCore.QSize(170, 70))
        self.bottom_buttons_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 70))

        # Labels
        self.page_title.setMaximumSize(QtCore.QSize(16777215, 70))
        self.transaction_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.value_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.product_name_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.date_label.setMaximumSize(QtCore.QSize(16777215, 70))

        # Buttons
        self.register_button.setMinimumSize(QtCore.QSize(150, 50))
        self.register_button.setMaximumSize(QtCore.QSize(180, 70))
        self.register_button.setStyleSheet("QPushButton {\n"
                                           "    background-color: white;\n"
                                           "    color: black;\n"
                                           "    border: 2px solid #4CAF50;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover:!pressed {\n"
                                           "    background-color: #4CAF50;\n"
                                           "    color: white;\n"
                                           "    font-weight: bold;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: #4CAF50;\n"
                                           "    color: white;\n"
                                           "    font-weight: bold;\n"
                                           "}")

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
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHeightForWidth(self.product_name_option.sizePolicy().hasHeightForWidth())
        self.product_name_option.setSizePolicy(size_policy)
        self.product_name_option.setMaximumSize(QtCore.QSize(16777215, 50))

        self.date_option.setMinimumSize(QtCore.QSize(120, 0))
        self.date_option.setMaximumSize(QtCore.QSize(180, 50))
        self.date_option.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.date_option.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_option.setDate(QtCore.QDate(2018, 1, 1))
        self.date_option.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        size_policy.setHeightForWidth(self.value_option.sizePolicy().hasHeightForWidth())
        self.value_option.setSizePolicy(size_policy)
        self.value_option.setMaximumSize(QtCore.QSize(160, 35))
        self.value_option.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.value_option.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        size_policy.setHeightForWidth(self.purchase_option.sizePolicy().hasHeightForWidth())
        self.purchase_option.setSizePolicy(size_policy)
        self.purchase_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        size_policy.setHeightForWidth(self.sale_option.sizePolicy().hasHeightForWidth())
        self.sale_option.setSizePolicy(size_policy)
        self.sale_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.page_title.setText(
            _translate("MainWindow", "Nesta área você irá cadastrar uma Compra OU Venda referente ao dia informado"))
        self.register_button.setText(_translate("MainWindow", "Cadastrar"))
        self.back_button.setText(_translate("MainWindow", "Voltar"))
        self.product_name_option.setPlaceholderText(_translate("MainWindow", "Nome do produto"))
        self.transaction_label.setText(_translate("MainWindow", "Marque a opção correspondente à transação:"))
        self.date_label.setText(_translate("MainWindow", "Informe a data da transação"))
        self.value_label.setText(_translate("MainWindow", "Informe o valor da transação"))
        self.product_name_label.setText(_translate("MainWindow", "Informe o nome do produto:"))
        self.coin_label.setText(_translate("MainWindow", "R$"))
        self.value_option.setPlaceholderText(_translate("MainWindow", "0,00"))
        self.sale_option.setText(_translate("MainWindow", "Compra"))
        self.purchase_option.setText(_translate("MainWindow", "Venda"))

    def create_structure(self):
        self.purchase_sale_layout.addWidget(self.purchase_option)
        self.purchase_sale_layout.addWidget(self.sale_option)

        self.coin_input_layout.addWidget(self.coin_label)
        self.coin_input_layout.addWidget(self.value_option)

        self.form_layout.addWidget(self.transaction_label, 0, 0, 1, 1)
        self.form_layout.addWidget(self.purchase_sale_horizontalWidget, 1, 0, 1, 1)
        self.form_layout.addWidget(self.date_label, 2, 0, 1, 1)
        self.form_layout.addWidget(self.date_option, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.form_layout.addWidget(self.product_name_label, 7, 0, 1, 1)
        self.form_layout.addWidget(self.product_name_option, 8, 0, 1, 1)
        self.form_layout.addWidget(self.value_label, 10, 0, 1, 1)
        self.form_layout.addWidget(self.coin_input_horizontalWidget, 11, 0, 1, 1)
        self.form_layout.addItem(QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum), 12, 0, 1, 1)

        self.bottom_buttons_layout.addItem(QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.bottom_buttons_layout.addWidget(self.register_button)
        self.bottom_buttons_layout.addWidget(self.back_button)

        self.grid_layout.addWidget(self.page_title, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.form, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.bottom_buttons_horizontalWidget, 2, 1, 1, 1)

    def define_actions(self):
        self.back_button.clicked.connect(self.back_signal.emit)


if __name__ == '__main__':
    import sys

    APP = QtWidgets.QApplication(sys.argv)
    app = RegistrationPage()
    app.show()
    sys.exit(APP.exec())
