from PyQt5 import QtCore, QtGui, QtWidgets


class DeletionPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(DeletionPage, self).__init__(*args)

        self.back_signal = back_signal

        # Main
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.form = QtWidgets.QWidget(self, *args)
        self.form_layout = QtWidgets.QGridLayout(self.form)
        self.value_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.value_layout = QtWidgets.QHBoxLayout(self.value_horizontalWidget)
        self.purchase_sale_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.purchase_sale_layout = QtWidgets.QHBoxLayout(self.purchase_sale_horizontalWidget)
        self.bottom_buttons_horizontalWidget = QtWidgets.QWidget(self, *args)
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout(self.bottom_buttons_horizontalWidget)

        # Labels
        self.page_title = QtWidgets.QLabel(self)
        self.purchase_sale_label = QtWidgets.QLabel(self.form)
        self.date_label = QtWidgets.QLabel(self.form)
        self.coin_label = QtWidgets.QLabel(self.value_horizontalWidget)
        self.value_label = QtWidgets.QLabel(self.form)

        # Buttons
        self.delete_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)
        self.back_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)

        # Inputs
        self.purchase_option = QtWidgets.QRadioButton(self.purchase_sale_horizontalWidget)
        self.sale_option = QtWidgets.QRadioButton(self.purchase_sale_horizontalWidget)
        self.date_option = QtWidgets.QDateEdit(self.form)
        self.value_option = QtWidgets.QTextEdit(self.value_horizontalWidget)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        # Main
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHeightForWidth(self.value_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.value_horizontalWidget.setSizePolicy(size_policy)
        self.value_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 60))

        self.purchase_sale_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.bottom_buttons_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 70))

        # Labels
        self.page_title.setMaximumSize(QtCore.QSize(16777215, 70))

        self.purchase_sale_label.setMinimumSize(QtCore.QSize(310, 0))
        self.purchase_sale_label.setMaximumSize(QtCore.QSize(16777215, 60))

        self.date_label.setMaximumSize(QtCore.QSize(16777215, 60))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        size_policy.setHeightForWidth(self.coin_label.sizePolicy().hasHeightForWidth())
        self.coin_label.setSizePolicy(size_policy)

        self.value_label.setMinimumSize(QtCore.QSize(300, 50))
        self.value_label.setMaximumSize(QtCore.QSize(350, 70))

        # Buttons
        self.delete_button.setMinimumSize(QtCore.QSize(150, 50))
        self.delete_button.setMaximumSize(QtCore.QSize(180, 70))
        self.delete_button.setStyleSheet("QPushButton {\n"
                                         "    background-color: white;\n"
                                         "    color: black;\n"
                                         "    border: 2px solid #E25235;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover:!pressed {\n"
                                         "    background-color: #E25235;\n"
                                         "    color: white;\n"
                                         "    font-weight: bold;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: #E25235;\n"
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
        self.purchase_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sale_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHeightForWidth(self.value_option.sizePolicy().hasHeightForWidth())
        self.value_option.setSizePolicy(size_policy)
        self.value_option.setMinimumSize(QtCore.QSize(160, 35))
        self.value_option.setMaximumSize(QtCore.QSize(160, 35))
        self.value_option.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.value_option.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.date_option.setMinimumSize(QtCore.QSize(120, 0))
        self.date_option.setMaximumSize(QtCore.QSize(180, 50))
        self.date_option.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.date_option.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_option.setDate(QtCore.QDate(2018, 1, 1))
        self.date_option.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.page_title.setText(_translate("MainWindow", "Nesta área você poderá excluir uma transação previamente cadastrada"))
        self.purchase_sale_label.setText(_translate("Form", "Marque a opção correspondente a transação"))
        self.date_label.setText(_translate("MainWindow", "Informe a data da transação"))
        self.coin_label.setText(_translate("MainWindow", "R$"))
        self.value_option.setPlaceholderText(_translate("MainWindow", "0,00"))
        self.purchase_option.setText(_translate("MainWindow", "Compra"))
        self.sale_option.setText(_translate("MainWindow", "Venda"))
        self.value_label.setText(_translate("MainWindow", "Informe o valor da transação"))
        self.delete_button.setText(_translate("MainWindow", "Excluir"))
        self.back_button.setText(_translate("MainWindow", "Voltar"))

    def create_structure(self):
        self.purchase_sale_layout.addWidget(self.purchase_option)
        self.purchase_sale_layout.addWidget(self.sale_option)

        self.value_layout.addWidget(self.coin_label)
        self.value_layout.addWidget(self.value_option)

        self.form_layout.addWidget(self.purchase_sale_label, 1, 0, 1, 1)
        self.form_layout.addWidget(self.date_label, 3, 0, 1, 1)
        self.form_layout.addWidget(self.value_horizontalWidget, 6, 0, 1, 1)
        self.form_layout.addWidget(self.purchase_sale_horizontalWidget, 2, 0, 1, 1)
        self.form_layout.addWidget(self.date_option, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.form_layout.addWidget(self.value_label, 5, 0, 1, 1)
        self.form_layout.addItem(QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum), 7, 0, 1, 1)

        self.bottom_buttons_layout.addItem(QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.bottom_buttons_layout.addWidget(self.delete_button)
        self.bottom_buttons_layout.addWidget(self.back_button)

        self.grid_layout.addWidget(self.page_title, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.form, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.bottom_buttons_horizontalWidget, 2, 0, 1, 1)

    def define_actions(self):
        self.back_button.clicked.connect(self.back_signal.emit)


if __name__ == '__main__':
    import sys

    APP = QtWidgets.QApplication(sys.argv)
    app = DeletionPage(None)
    app.show()
    sys.exit(APP.exec())
