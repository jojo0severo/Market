import re
import locale
locale.setlocale(locale.LC_MONETARY, '')
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from controller.deletion_controller import DeletionController


class DeletionPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(DeletionPage, self).__init__(*args)

        self.controller = DeletionController()
        self.back_signal = back_signal
        self.dialog = QtWidgets.QMessageBox(self)
        self.dialog.setWindowTitle('Aviso')

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
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.delete_button.setFont(font)
        self.delete_button.setMinimumSize(QtCore.QSize(160, 50))
        self.delete_button.setMaximumSize(QtCore.QSize(180, 80))
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

        self.back_button.setFont(font)
        self.back_button.setMinimumSize(QtCore.QSize(160, 50))
        self.back_button.setMaximumSize(QtCore.QSize(180, 80))
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
        self.date_option.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))
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
        self.value_option.keyPressEvent = self.handle_key_pressed
        self.delete_button.clicked.connect(self.delete_transaction)
        self.back_button.clicked.connect(self.back_signal.emit)

    def handle_key_pressed(self, event):
        text = self.value_option.toPlainText().replace('.', '').replace(',', '')
        text = re.sub('\A0*', '', text)
        key = event.key()
        if 57 >= key >= 48:
            new_char = chr(key)
            self.format(text, new_char)

        elif key == QtCore.Qt.Key_Backspace or key == QtCore.Qt.Key_Delete:
            text = text[1:]
            self.format(text, '')

    def format(self, text, new_char):
        text = text + new_char

        if len(text) == 0:
            text = '0.0'

        elif len(text) == 1:
            text = '0.0' + text

        elif len(text) == 2:
            text = '0.' + text

        else:
            text = text[:-2] + '.' + text[-2:]

        a = locale.currency(float(text), grouping=True).split(' ')[1]
        self.value_option.setText(a)

    def delete_transaction(self):
        info = {}

        if self.purchase_option.isChecked():
            info['transaction_type'] = 'purchase'

        elif self.sale_option.isChecked():
            info['transaction_type'] = 'sale'

        else:
            self.dialog.setText('\nA transação não foi classificada em Compra ou Venda. Classifique e tente novamente.\t\t\n')
            self.dialog.exec()
            return

        info['transaction_date'] = self.date_option.text()

        value = self.value_option.toPlainText()
        value = re.sub('\A0*', '0', value.replace('.', '').replace(',', '.'))
        if not value or value == '0.0':
            self.dialog.setText('\nNenhum valor de transação foi informado. Insira um valor e tente novamente.\t\t\n')
            self.dialog.exec()
            return

        info['transaction_value'] = float(value)

        message = self.controller.delete(info)
        self.dialog.setText('\n{}\t\t\n'.format(message))
        self.dialog.exec()

    def clear(self):
        self.sale_option.setAutoExclusive(False)
        self.purchase_option.setAutoExclusive(False)

        self.sale_option.setChecked(False)
        self.purchase_option.setChecked(False)

        self.sale_option.setAutoExclusive(True)
        self.purchase_option.setAutoExclusive(True)

        self.value_option.clear()
        self.date_option.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))
