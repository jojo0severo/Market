import re
import locale
locale.setlocale(locale.LC_MONETARY, '')
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from controller.edition_controller import EditionController


class EditionPage(QtWidgets.QWidget):
    def __init__(self, back_signal, *args):
        super(EditionPage, self).__init__(*args)

        self.controller = EditionController()
        self.back_signal = back_signal
        self.dialog = QtWidgets.QMessageBox(self)
        self.dialog.setWindowTitle('Aviso')

        # Declaring main objects
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.form = QtWidgets.QWidget(self, *args)
        self.form_layout = QtWidgets.QVBoxLayout(self.form)

        self.purchase_sale_widget = QtWidgets.QWidget(self.form, *args)
        self.purchase_sale_layout = QtWidgets.QHBoxLayout(self.purchase_sale_widget)

        self.old_value_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.old_value_layout = QtWidgets.QHBoxLayout(self.old_value_horizontalWidget)

        self.new_value_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.new_value_layout = QtWidgets.QHBoxLayout(self.new_value_horizontalWidget)

        self.bottom_buttons_horizontalWidget = QtWidgets.QWidget(self, *args)
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout(self.bottom_buttons_horizontalWidget)

        # Declaring Labels
        self.page_title = QtWidgets.QLabel(self)
        self.purchase_sale_label = QtWidgets.QLabel(self.form)
        self.date_label = QtWidgets.QLabel(self.form)
        self.old_value_label = QtWidgets.QLabel(self.form)
        self.coin_label_1 = QtWidgets.QLabel(self.old_value_horizontalWidget)
        self.new_value_label = QtWidgets.QLabel(self.form)
        self.coin_label_2 = QtWidgets.QLabel(self.new_value_horizontalWidget)

        # Declaring buttons
        self.edit_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)
        self.back_button = QtWidgets.QPushButton(self.bottom_buttons_horizontalWidget)

        # Declaring inputs
        self.purchase_option = QtWidgets.QRadioButton(self.purchase_sale_widget)
        self.sale_option = QtWidgets.QRadioButton(self.purchase_sale_widget)
        self.date_option = QtWidgets.QDateEdit(self.form)
        self.old_value_option = QtWidgets.QTextEdit(self.old_value_horizontalWidget)
        self.new_value_option = QtWidgets.QTextEdit(self.new_value_horizontalWidget)

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()
        self.define_actions()

    def setup_ui(self):
        # Main
        self.form.setMinimumSize(QtCore.QSize(0, 500))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        size_policy.setHeightForWidth(self.old_value_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.old_value_horizontalWidget.setSizePolicy(size_policy)

        self.purchase_sale_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))

        size_policy.setHeightForWidth(self.new_value_horizontalWidget.sizePolicy().hasHeightForWidth())
        self.new_value_horizontalWidget.setSizePolicy(size_policy)

        self.bottom_buttons_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 70))

        # Labels
        self.page_title.setMaximumSize(QtCore.QSize(16777215, 70))
        self.purchase_sale_label.setMaximumSize(QtCore.QSize(610, 16777215))
        self.date_label.setMaximumSize(QtCore.QSize(610, 16777215))
        self.old_value_label.setMaximumSize(QtCore.QSize(610, 16777215))
        self.new_value_label.setMaximumSize(QtCore.QSize(610, 16777215))

        size_policy.setHeightForWidth(self.coin_label_2.sizePolicy().hasHeightForWidth())
        self.coin_label_2.setSizePolicy(size_policy)

        # Buttons
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.edit_button.setFont(font)
        self.edit_button.setMinimumSize(QtCore.QSize(160, 50))
        self.edit_button.setMaximumSize(QtCore.QSize(180, 80))
        self.edit_button.setStyleSheet("QPushButton {\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    border: 2px solid #E5C442;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover:!pressed {\n"
                                       "    background-color: #E5C442;\n"
                                       "    color: white;\n"
                                       "    font-weight: bold;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #E5C442;\n"
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
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHeightForWidth(self.purchase_option.sizePolicy().hasHeightForWidth())
        self.purchase_option.setSizePolicy(size_policy)
        self.purchase_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHeightForWidth(self.sale_option.sizePolicy().hasHeightForWidth())
        self.sale_option.setSizePolicy(size_policy)
        self.sale_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHeightForWidth(self.date_option.sizePolicy().hasHeightForWidth())
        self.date_option.setSizePolicy(size_policy)
        self.date_option.setMinimumSize(QtCore.QSize(120, 0))
        self.date_option.setMaximumSize(QtCore.QSize(180, 50))
        self.date_option.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        self.date_option.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        self.old_value_option.setMaximumSize(QtCore.QSize(220, 35))
        self.old_value_option.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.old_value_option.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.new_value_option.setMaximumSize(QtCore.QSize(220, 35))
        self.new_value_option.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.new_value_option.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.purchase_sale_label.setText(_translate("MainWindow", "Marque a opção correspondente à transação:"))
        self.purchase_option.setText(_translate("MainWindow", "Compra"))
        self.sale_option.setText(_translate("MainWindow", "Venda"))
        self.date_label.setText(_translate("MainWindow", "Informe a data da transação:"))
        self.old_value_label.setText(_translate("MainWindow", "Informe o valor incorreto da transação (o valor registrado atualmente):"))
        self.coin_label_1.setText(_translate("MainWindow", "R$"))
        self.old_value_option.setPlaceholderText(_translate("MainWindow", "0,00"))
        self.new_value_label.setText(_translate("MainWindow", "Informe o novo valor da transação (o valor correto):"))
        self.coin_label_2.setText(_translate("MainWindow", "R$"))
        self.new_value_option.setPlaceholderText(_translate("MainWindow", "0,00"))
        self.edit_button.setText(_translate("MainWindow", "Editar"))
        self.back_button.setText(_translate("MainWindow", "Voltar"))
        self.page_title.setText(_translate("MainWindow", "Nesta área você irá alterar o valor de uma Compra OU Venda"))

    def create_structure(self):
        self.purchase_sale_layout.addWidget(self.purchase_option)
        self.purchase_sale_layout.addWidget(self.sale_option)

        self.old_value_layout.addWidget(self.coin_label_1)
        self.old_value_layout.addWidget(self.old_value_option)

        self.new_value_layout.addWidget(self.coin_label_2)
        self.new_value_layout.addWidget(self.new_value_option)

        self.form_layout.addWidget(self.purchase_sale_label)
        self.form_layout.addWidget(self.purchase_sale_widget)
        self.form_layout.addWidget(self.date_label)
        self.form_layout.addWidget(self.date_option, 0, QtCore.Qt.AlignHCenter)
        self.form_layout.addWidget(self.old_value_label)
        self.form_layout.addWidget(self.old_value_horizontalWidget)
        self.form_layout.addWidget(self.new_value_label)
        self.form_layout.addWidget(self.new_value_horizontalWidget)
        self.form_layout.addItem(QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.bottom_buttons_layout.addItem(QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.bottom_buttons_layout.addWidget(self.edit_button)
        self.bottom_buttons_layout.addWidget(self.back_button)

        self.gridLayout.addWidget(self.page_title, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.form, 1, 0, 2, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.bottom_buttons_horizontalWidget, 12, 0, 1, 1)

    def define_actions(self):
        self.old_value_option.keyPressEvent = self.handle_key_pressed
        self.new_value_option.keyPressEvent = self.handle_key_pressed
        self.edit_button.clicked.connect(self.edit_transaction)
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

    def edit_transaction(self):
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

        old_value = self.old_value_option.toPlainText()
        old_value = re.sub('\A0*', '0', old_value.replace('.', '').replace(',', '.'))
        if not old_value or old_value == '0.0':
            self.dialog.setText('\nNenhum valor antigo foi informado. Insira o valor cadastrado atualmente e tente novamente.\t\t\n')
            self.dialog.exec()
            return

        info['transaction_old_value'] = float(old_value)

        new_value = self.new_value_option.toPlainText()
        new_value = re.sub('\A0*', '0', new_value.replace('.', '').replace(',', '.'))
        if not new_value or new_value == '0.0':
            self.dialog.setText('\nNenhum valor novo foi informado. Insira o novo valor e tente novamente.\t\t\n')
            self.dialog.exec()
            return

        info['transaction_new_value'] = float(new_value)

        message = self.controller.edit(info)
        self.dialog.setText('\n{}\t\t\n'.format(message))
        self.dialog.exec()

    def clear(self):
        self.sale_option.setAutoExclusive(False)
        self.purchase_option.setAutoExclusive(False)

        self.sale_option.setChecked(False)
        self.purchase_option.setChecked(False)

        self.sale_option.setAutoExclusive(True)
        self.purchase_option.setAutoExclusive(True)

        self.old_value_option.clear()
        self.new_value_option.clear()
        self.date_option.setDate(QtCore.QDate(datetime.now().year, datetime.now().month, datetime.now().day))
