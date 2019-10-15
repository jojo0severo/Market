from PyQt5 import QtCore, QtGui, QtWidgets


class RegistrationPage(QtWidgets.QWidget):
    def __init__(self, *args):
        super(RegistrationPage, self).__init__(*args)

        # Declaring main objects
        self.grid_layout = QtWidgets.QGridLayout(self)

        self.form = QtWidgets.QWidget(self, *args)
        self.form_layout = QtWidgets.QGridLayout(self.form)

        self.purchase_sale_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.purchase_sale_layout = QtWidgets.QHBoxLayout(self.purchase_sale_horizontalWidget)

        self.coin_input_horizontalWidget = QtWidgets.QWidget(self.form, *args)
        self.coin_input_list = QtWidgets.QHBoxLayout(self.coin_input_horizontalWidget)

        self.bottom_buttons_horizontalWidget = QtWidgets.QWidget(self, *args)
        self.bottom_buttons_list = QtWidgets.QHBoxLayout(self.bottom_buttons_horizontalWidget)

        # Declaring Labels
        self.page_title = QtWidgets.QLabel(self)
        self.transaction_label = QtWidgets.QLabel(self.form)
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

        # Spacers
        self.spacer = QtWidgets.QLabel(self.form)
        self.spacer1 = QtWidgets.QLabel(self.bottom_buttons_horizontalWidget)
        self.spacer2 = QtWidgets.QLabel(self.bottom_buttons_horizontalWidget)

    def setup_ui(self):
        self.page_title.setMaximumSize(QtCore.QSize(16777215, 70))

        self.grid_layout.addWidget(self.page_title, 0, 1, 1, 1)


        self.bottom_buttons_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 70))


        self.spacer1.setText("")


        self.bottom_buttons_list.addWidget(self.spacer1)


        self.spacer2.setText("")


        self.bottom_buttons_list.addWidget(self.spacer2)



        self.register_button.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.register_button.setFont(font)
        self.register_button.setStyleSheet("QPushButton {\n"
                                             "    background-color: white;\n"
                                             "    color: black;\n"
                                             "    border: 2px solid #4CAF50;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton : hover : !pressed {\n"
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



        self.bottom_buttons_list.addWidget(self.register_button)



        self.back_button.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton {\n"
                                       "    background-color: white;\n"
                                       "    color: black;\n"
                                       "    border: 2px solid #C1C0C0;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton : hover : !pressed {\n"
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


        self.bottom_buttons_list.addWidget(self.back_button)


        self.grid_layout.addWidget(self.bottom_buttons_horizontalWidget, 2, 1, 1, 1)



        self.form.setMinimumSize(QtCore.QSize(300, 500))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.form.setFont(font)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_name_option.sizePolicy().hasHeightForWidth())
        self.product_name_option.setSizePolicy(sizePolicy)
        self.product_name_option.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.product_name_option.setFont(font)
        self.product_name_option.setUndoRedoEnabled(False)


        self.form_layout.addWidget(self.product_name_option, 8, 0, 1, 1)


        self.transaction_label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.transaction_label.setFont(font)


        self.form_layout.addWidget(self.transaction_label, 0, 0, 1, 1)




        self.date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.date_label.setFont(font)


        self.form_layout.addWidget(self.date_label, 2, 0, 1, 1)


        self.date_option.setMinimumSize(QtCore.QSize(200, 0))
        self.date_option.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.date_option.setFont(font)
        self.date_option.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.date_option.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1990, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_option.setDate(QtCore.QDate(2018, 1, 1))


        self.form_layout.addWidget(self.date_option, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)


        self.value_label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.value_label.setFont(font)


        self.form_layout.addWidget(self.value_label, 10, 0, 1, 1)



        self.spacer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.spacer.setText("")


        self.form_layout.addWidget(self.spacer, 12, 0, 1, 1)



        self.product_name_label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.product_name_label.setFont(font)


        self.form_layout.addWidget(self.product_name_label, 7, 0, 1, 1)



        self.coin_input_horizontalWidget.setMaximumSize(QtCore.QSize(170, 70))



        self.coin_input_list.addWidget(self.coin_label)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_option.sizePolicy().hasHeightForWidth())
        self.value_option.setSizePolicy(sizePolicy)
        self.value_option.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.value_option.setFont(font)
        self.value_option.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.value_option.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)


        self.coin_input_list.addWidget(self.value_option)


        self.form_layout.addWidget(self.coin_input_horizontalWidget, 11, 0, 1, 1)



        self.purchase_sale_horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 50))




        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sale_option.sizePolicy().hasHeightForWidth())
        self.sale_option.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sale_option.setFont(font)


        self.purchase_sale_layout.addWidget(self.sale_option)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.purchase_option.sizePolicy().hasHeightForWidth())
        self.purchase_option.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.purchase_option.setFont(font)


        self.purchase_sale_layout.addWidget(self.purchase_option)


        self.form_layout.addWidget(self.purchase_sale_horizontalWidget, 1, 0, 1, 1)


        self.grid_layout.addWidget(self.form, 1, 1, 1, 1)
