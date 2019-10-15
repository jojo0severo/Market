
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(926, 695)
        # MainWindow.setMaximumSize(QtCore.QSize(16777215, 763))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("market_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.stackedWidget.setObjectName("stackedWidget")

        self.registration_page = QtWidgets.QWidget()
        self.registration_page.setObjectName("registration_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.registration_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.page_title = QtWidgets.QLabel(self.registration_page)
        self.page_title.setMaximumSize(QtCore.QSize(16777215, 70))
        self.page_title.setObjectName("page_title")
        self.gridLayout_3.addWidget(self.page_title, 0, 1, 1, 1)
        self.horizontalWidget1 = QtWidgets.QWidget(self.registration_page)
        self.horizontalWidget1.setMaximumSize(QtCore.QSize(16777215, 70))
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spacer_2 = QtWidgets.QLabel(self.horizontalWidget1)
        self.spacer_2.setText("")
        self.spacer_2.setObjectName("spacer_2")
        self.horizontalLayout_5.addWidget(self.spacer_2)
        self.spacer_3 = QtWidgets.QLabel(self.horizontalWidget1)
        self.spacer_3.setText("")
        self.spacer_3.setObjectName("spacer_3")
        self.horizontalLayout_5.addWidget(self.spacer_3)
        self.register_button_3 = QtWidgets.QPushButton(self.horizontalWidget1)
        self.register_button_3.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.register_button_3.setFont(font)
        self.register_button_3.setStyleSheet("QPushButton {\n"
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
        self.register_button_3.setObjectName("register_button_3")
        self.horizontalLayout_5.addWidget(self.register_button_3)
        self.back_button = QtWidgets.QPushButton(self.horizontalWidget1)
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
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_5.addWidget(self.back_button)
        self.gridLayout_3.addWidget(self.horizontalWidget1, 2, 1, 1, 1)
        self.gridWidget = QtWidgets.QWidget(self.registration_page)
        self.gridWidget.setMinimumSize(QtCore.QSize(300, 500))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gridWidget.setFont(font)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.product_name_option = QtWidgets.QTextEdit(self.gridWidget)
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
        self.product_name_option.setObjectName("product_name_option")
        self.gridLayout_10.addWidget(self.product_name_option, 8, 0, 1, 1)
        self.transaction_label = QtWidgets.QLabel(self.gridWidget)
        self.transaction_label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.transaction_label.setFont(font)
        self.transaction_label.setObjectName("transaction_label")
        self.gridLayout_10.addWidget(self.transaction_label, 0, 0, 1, 1)
        self.date_label = QtWidgets.QLabel(self.gridWidget)
        self.date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.gridLayout_10.addWidget(self.date_label, 2, 0, 1, 1)
        self.date_option = QtWidgets.QDateEdit(self.gridWidget)
        self.date_option.setMinimumSize(QtCore.QSize(200, 0))
        self.date_option.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.date_option.setFont(font)
        self.date_option.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.date_option.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1990, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_option.setDate(QtCore.QDate(2018, 1, 1))
        self.date_option.setObjectName("date_option")
        self.gridLayout_10.addWidget(self.date_option, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.value_label = QtWidgets.QLabel(self.gridWidget)
        self.value_label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.value_label.setFont(font)
        self.value_label.setObjectName("value_label")
        self.gridLayout_10.addWidget(self.value_label, 10, 0, 1, 1)
        self.spacer = QtWidgets.QLabel(self.gridWidget)
        self.spacer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.spacer.setText("")
        self.spacer.setObjectName("spacer")
        self.gridLayout_10.addWidget(self.spacer, 12, 0, 1, 1)
        self.product_name_label = QtWidgets.QLabel(self.gridWidget)
        self.product_name_label.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.product_name_label.setFont(font)
        self.product_name_label.setObjectName("product_name_label")
        self.gridLayout_10.addWidget(self.product_name_label, 7, 0, 1, 1)
        self.horizontalWidget2 = QtWidgets.QWidget(self.gridWidget)
        self.horizontalWidget2.setMaximumSize(QtCore.QSize(170, 70))
        self.horizontalWidget2.setObjectName("horizontalWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.coin_label = QtWidgets.QLabel(self.horizontalWidget2)
        self.coin_label.setObjectName("coin_label")
        self.horizontalLayout_4.addWidget(self.coin_label)
        self.value_option = QtWidgets.QTextEdit(self.horizontalWidget2)
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
        self.value_option.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.value_option.setUndoRedoEnabled(False)
        self.value_option.setAcceptRichText(False)
        self.value_option.setObjectName("value_option")
        self.horizontalLayout_4.addWidget(self.value_option)
        self.gridLayout_10.addWidget(self.horizontalWidget2, 11, 0, 1, 1)
        self.purchase_sale_options = QtWidgets.QWidget(self.gridWidget)
        self.purchase_sale_options.setMaximumSize(QtCore.QSize(16777215, 50))
        self.purchase_sale_options.setObjectName("purchase_sale_options")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.purchase_sale_options)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sale_option = QtWidgets.QRadioButton(self.purchase_sale_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sale_option.sizePolicy().hasHeightForWidth())
        self.sale_option.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sale_option.setFont(font)
        self.sale_option.setObjectName("sale_option")
        self.horizontalLayout_3.addWidget(self.sale_option)
        self.purchase_option = QtWidgets.QRadioButton(self.purchase_sale_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.purchase_option.sizePolicy().hasHeightForWidth())
        self.purchase_option.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.purchase_option.setFont(font)
        self.purchase_option.setObjectName("purchase_option")
        self.horizontalLayout_3.addWidget(self.purchase_option)
        self.gridLayout_10.addWidget(self.purchase_sale_options, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.gridWidget, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.registration_page)













        self.edition_page = QtWidgets.QWidget()
        self.edition_page.setObjectName("edition_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.edition_page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalWidget = QtWidgets.QWidget(self.edition_page)
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 500))
        self.verticalWidget.setStyleSheet("")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.purchase_sale_label = QtWidgets.QLabel(self.verticalWidget)
        self.purchase_sale_label.setMaximumSize(QtCore.QSize(610, 16777215))
        self.purchase_sale_label.setObjectName("purchase_sale_label")
        self.verticalLayout_11.addWidget(self.purchase_sale_label)
        self.purchase_sale_options_2 = QtWidgets.QWidget(self.verticalWidget)
        self.purchase_sale_options_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.purchase_sale_options_2.setObjectName("purchase_sale_options_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.purchase_sale_options_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.purchase_option_2 = QtWidgets.QRadioButton(self.purchase_sale_options_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.purchase_option_2.sizePolicy().hasHeightForWidth())
        self.purchase_option_2.setSizePolicy(sizePolicy)
        self.purchase_option_2.setObjectName("purchase_option_2")
        self.horizontalLayout_7.addWidget(self.purchase_option_2)
        self.sale_option_2 = QtWidgets.QRadioButton(self.purchase_sale_options_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sale_option_2.sizePolicy().hasHeightForWidth())
        self.sale_option_2.setSizePolicy(sizePolicy)
        self.sale_option_2.setObjectName("sale_option_2")
        self.horizontalLayout_7.addWidget(self.sale_option_2)
        self.verticalLayout_11.addWidget(self.purchase_sale_options_2)
        self.date_label_2 = QtWidgets.QLabel(self.verticalWidget)
        self.date_label_2.setMaximumSize(QtCore.QSize(610, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.date_label_2.setFont(font)
        self.date_label_2.setObjectName("date_label_2")
        self.verticalLayout_11.addWidget(self.date_label_2)
        self.date_option_2 = QtWidgets.QDateEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_option_2.sizePolicy().hasHeightForWidth())
        self.date_option_2.setSizePolicy(sizePolicy)
        self.date_option_2.setMinimumSize(QtCore.QSize(200, 0))
        self.date_option_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.date_option_2.setDate(QtCore.QDate(2018, 1, 1))
        self.date_option_2.setObjectName("date_option_2")
        self.verticalLayout_11.addWidget(self.date_option_2, 0, QtCore.Qt.AlignHCenter)
        self.old_value_label = QtWidgets.QLabel(self.verticalWidget)
        self.old_value_label.setMaximumSize(QtCore.QSize(610, 16777215))
        self.old_value_label.setObjectName("old_value_label")
        self.verticalLayout_11.addWidget(self.old_value_label)
        self.horizontalWidget3 = QtWidgets.QWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget3.setSizePolicy(sizePolicy)
        self.horizontalWidget3.setObjectName("horizontalWidget3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalWidget3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.coin_label_3 = QtWidgets.QLabel(self.horizontalWidget3)
        self.coin_label_3.setObjectName("coin_label_3")
        self.horizontalLayout_9.addWidget(self.coin_label_3)
        self.old_value_option = QtWidgets.QTextEdit(self.horizontalWidget3)
        self.old_value_option.setMaximumSize(QtCore.QSize(160, 35))
        self.old_value_option.setObjectName("old_value_option")
        self.horizontalLayout_9.addWidget(self.old_value_option)
        self.verticalLayout_11.addWidget(self.horizontalWidget3)
        self.new_value_label = QtWidgets.QLabel(self.verticalWidget)
        self.new_value_label.setMaximumSize(QtCore.QSize(610, 16777215))
        self.new_value_label.setObjectName("new_value_label")
        self.verticalLayout_11.addWidget(self.new_value_label)
        self.horizontalWidget4 = QtWidgets.QWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget4.sizePolicy().hasHeightForWidth())
        self.horizontalWidget4.setSizePolicy(sizePolicy)
        self.horizontalWidget4.setObjectName("horizontalWidget4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.coin_label_2 = QtWidgets.QLabel(self.horizontalWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coin_label_2.sizePolicy().hasHeightForWidth())
        self.coin_label_2.setSizePolicy(sizePolicy)
        self.coin_label_2.setObjectName("coin_label_2")
        self.horizontalLayout_8.addWidget(self.coin_label_2)
        self.new_value_option = QtWidgets.QTextEdit(self.horizontalWidget4)
        self.new_value_option.setMaximumSize(QtCore.QSize(160, 35))
        self.new_value_option.setObjectName("new_value_option")
        self.horizontalLayout_8.addWidget(self.new_value_option)
        self.verticalLayout_11.addWidget(self.horizontalWidget4)
        self.spacer_6 = QtWidgets.QLabel(self.verticalWidget)
        self.spacer_6.setText("")
        self.spacer_6.setObjectName("spacer_6")
        self.verticalLayout_11.addWidget(self.spacer_6)
        self.gridLayout_4.addWidget(self.verticalWidget, 1, 0, 2, 1, QtCore.Qt.AlignHCenter)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.edition_page)
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.spacer_5 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.spacer_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.spacer_5.setText("")
        self.spacer_5.setObjectName("spacer_5")
        self.horizontalLayout_6.addWidget(self.spacer_5)
        self.spacer_4 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.spacer_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.spacer_4.setText("")
        self.spacer_4.setObjectName("spacer_4")
        self.horizontalLayout_6.addWidget(self.spacer_4)
        self.edit_button_3 = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.edit_button_3.setMaximumSize(QtCore.QSize(180, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.edit_button_3.setFont(font)
        self.edit_button_3.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #E5C442;\n"
"}\n"
"\n"
"QPushButton : hover : !pressed {\n"
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
        self.edit_button_3.setObjectName("edit_button_3")
        self.horizontalLayout_6.addWidget(self.edit_button_3)
        self.back_button_2 = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.back_button_2.setMaximumSize(QtCore.QSize(180, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.back_button_2.setFont(font)
        self.back_button_2.setStyleSheet("QPushButton {\n"
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
        self.back_button_2.setObjectName("back_button_2")
        self.horizontalLayout_6.addWidget(self.back_button_2)
        self.gridLayout_4.addWidget(self.horizontalWidget_2, 12, 0, 1, 1)
        self.page_title_2 = QtWidgets.QLabel(self.edition_page)
        self.page_title_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.page_title_2.setObjectName("page_title_2")
        self.gridLayout_4.addWidget(self.page_title_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.edition_page)
        self.deletion_page = QtWidgets.QWidget()
        self.deletion_page.setObjectName("deletion_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.deletion_page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.page_title_3 = QtWidgets.QLabel(self.deletion_page)
        self.page_title_3.setMinimumSize(QtCore.QSize(0, 70))
        self.page_title_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.page_title_3.setObjectName("page_title_3")
        self.gridLayout_5.addWidget(self.page_title_3, 0, 0, 1, 1)
        self.horizontalWidget5 = QtWidgets.QWidget(self.deletion_page)
        self.horizontalWidget5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalWidget5.setObjectName("horizontalWidget5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalWidget5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.spacer_8 = QtWidgets.QLabel(self.horizontalWidget5)
        self.spacer_8.setText("")
        self.spacer_8.setObjectName("spacer_8")
        self.horizontalLayout_10.addWidget(self.spacer_8)
        self.spacer_7 = QtWidgets.QLabel(self.horizontalWidget5)
        self.spacer_7.setText("")
        self.spacer_7.setObjectName("spacer_7")
        self.horizontalLayout_10.addWidget(self.spacer_7)
        self.delete_button_3 = QtWidgets.QPushButton(self.horizontalWidget5)
        self.delete_button_3.setMinimumSize(QtCore.QSize(0, 70))
        self.delete_button_3.setMaximumSize(QtCore.QSize(180, 70))
        self.delete_button_3.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #E25235;\n"
"}\n"
"\n"
"QPushButton : hover : !pressed {\n"
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
        self.delete_button_3.setObjectName("delete_button_3")
        self.horizontalLayout_10.addWidget(self.delete_button_3)
        self.back_button_3 = QtWidgets.QPushButton(self.horizontalWidget5)
        self.back_button_3.setMinimumSize(QtCore.QSize(0, 70))
        self.back_button_3.setMaximumSize(QtCore.QSize(180, 16777215))
        self.back_button_3.setStyleSheet("QPushButton {\n"
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
        self.back_button_3.setObjectName("back_button_3")
        self.horizontalLayout_10.addWidget(self.back_button_3)
        self.gridLayout_5.addWidget(self.horizontalWidget5, 3, 0, 1, 1)
        self.gridWidget1 = QtWidgets.QWidget(self.deletion_page)
        self.gridWidget1.setObjectName("gridWidget1")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridWidget1)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_4 = QtWidgets.QLabel(self.gridWidget1)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_13.addWidget(self.label_4, 6, 0, 1, 1)
        self.horizontalWidget6 = QtWidgets.QWidget(self.gridWidget1)
        self.horizontalWidget6.setMaximumSize(QtCore.QSize(180, 40))
        self.horizontalWidget6.setObjectName("horizontalWidget6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalWidget6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget6)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalWidget6)
        self.textEdit.setMaximumSize(QtCore.QSize(150, 35))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_12.addWidget(self.textEdit)
        self.gridLayout_13.addWidget(self.horizontalWidget6, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridWidget1)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label_2.setObjectName("label_2")
        self.gridLayout_13.addWidget(self.label_2, 4, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridWidget1)
        self.dateEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dateEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_13.addWidget(self.dateEdit, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridWidget1)
        self.label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label.setObjectName("label")
        self.gridLayout_13.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalWidget7 = QtWidgets.QWidget(self.gridWidget1)
        self.horizontalWidget7.setMaximumSize(QtCore.QSize(16777215, 70))
        self.horizontalWidget7.setObjectName("horizontalWidget7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalWidget7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalWidget7)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_11.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalWidget7)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_11.addWidget(self.radioButton)
        self.gridLayout_13.addWidget(self.horizontalWidget7, 1, 0, 1, 1)
        self.purchase_sale_label_2 = QtWidgets.QLabel(self.gridWidget1)
        self.purchase_sale_label_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.purchase_sale_label_2.setObjectName("purchase_sale_label_2")
        self.gridLayout_13.addWidget(self.purchase_sale_label_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.gridWidget1, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.deletion_page)
        self.lists_page = QtWidgets.QWidget()
        self.lists_page.setObjectName("lists_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.lists_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalWidget1 = QtWidgets.QWidget(self.lists_page)
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.from_date_label = QtWidgets.QLabel(self.verticalWidget1)
        self.from_date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.from_date_label.setObjectName("from_date_label")
        self.verticalLayout.addWidget(self.from_date_label)
        self.from_date_option = QtWidgets.QDateEdit(self.verticalWidget1)
        self.from_date_option.setDate(QtCore.QDate(2018, 1, 1))
        self.from_date_option.setObjectName("from_date_option")
        self.verticalLayout.addWidget(self.from_date_option)
        self.to_date_label = QtWidgets.QLabel(self.verticalWidget1)
        self.to_date_label.setMaximumSize(QtCore.QSize(16777215, 70))
        self.to_date_label.setObjectName("to_date_label")
        self.verticalLayout.addWidget(self.to_date_label)
        self.to_date_option = QtWidgets.QDateEdit(self.verticalWidget1)
        self.to_date_option.setDate(QtCore.QDate(2018, 2, 1))
        self.to_date_option.setObjectName("to_date_option")
        self.verticalLayout.addWidget(self.to_date_option)
        spacerItem = QtWidgets.QSpacerItem(20, 460, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_6.addWidget(self.verticalWidget1, 0, 1, 1, 1)
        self.gridWidget2 = QtWidgets.QWidget(self.lists_page)
        self.gridWidget2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridWidget2.setObjectName("gridWidget2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridWidget2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.purchases_label = QtWidgets.QLabel(self.gridWidget2)
        self.purchases_label.setObjectName("purchases_label")
        self.gridLayout_11.addWidget(self.purchases_label, 0, 0, 1, 1)
        self.sales_label = QtWidgets.QLabel(self.gridWidget2)
        self.sales_label.setObjectName("sales_label")
        self.gridLayout_11.addWidget(self.sales_label, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem1, 1, 1, 1, 1)
        self.purchases_table = QtWidgets.QTableWidget(self.gridWidget2)
        self.purchases_table.setObjectName("purchases_table")
        self.purchases_table.setColumnCount(0)
        self.purchases_table.setRowCount(0)
        self.gridLayout_11.addWidget(self.purchases_table, 1, 0, 1, 1)
        self.sales_table = QtWidgets.QTableWidget(self.gridWidget2)
        self.sales_table.setMaximumSize(QtCore.QSize(400, 16777215))
        self.sales_table.setObjectName("sales_table")
        self.sales_table.setColumnCount(0)
        self.sales_table.setRowCount(0)
        self.gridLayout_11.addWidget(self.sales_table, 1, 2, 1, 1)
        self.gridLayout_6.addWidget(self.gridWidget2, 0, 0, 1, 1)
        self.spacer_9 = QtWidgets.QLabel(self.lists_page)
        self.spacer_9.setText("")
        self.spacer_9.setObjectName("spacer_9")
        self.gridLayout_6.addWidget(self.spacer_9, 1, 0, 1, 1)
        self.back_button_4 = QtWidgets.QPushButton(self.lists_page)
        self.back_button_4.setMinimumSize(QtCore.QSize(180, 70))
        self.back_button_4.setMaximumSize(QtCore.QSize(180, 70))
        self.back_button_4.setStyleSheet("QPushButton {\n"
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
        self.back_button_4.setObjectName("back_button_4")
        self.gridLayout_6.addWidget(self.back_button_4, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.lists_page)
        self.profit_graphic_page = QtWidgets.QWidget()
        self.profit_graphic_page.setObjectName("profit_graphic_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.profit_graphic_page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graphicsView = QtWidgets.QGraphicsView(self.profit_graphic_page)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_7.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.profit_graphic_page)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.profit_graphic_page)
        self.purchases_graphic_page = QtWidgets.QWidget()
        self.purchases_graphic_page.setObjectName("purchases_graphic_page")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.purchases_graphic_page)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.purchases_graphic_page)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_8.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.purchases_graphic_page)
        self.sales_graphic_page = QtWidgets.QWidget()
        self.sales_graphic_page.setObjectName("sales_graphic_page")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.sales_graphic_page)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.sales_graphic_page)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_9.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.sales_graphic_page)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dois irmãos"))
        self.page_title.setText(_translate("MainWindow", "Nesta área você irá cadastrar uma Compra OU Venda referente ao dia informado"))
        self.register_button_3.setText(_translate("MainWindow", "Cadastrar"))
        self.back_button.setText(_translate("MainWindow", "Voltar"))
        self.product_name_option.setPlaceholderText(_translate("MainWindow", "Nome do produto"))
        self.transaction_label.setText(_translate("MainWindow", "Marque a opção correspondente à transação:"))
        self.date_label.setText(_translate("MainWindow", "Informe a data da transação"))
        self.value_label.setText(_translate("MainWindow", "Informe o valor da transação"))
        self.product_name_label.setText(_translate("MainWindow", "Informe o nome do produto:"))
        self.coin_label.setText(_translate("MainWindow", "R$"))
        self.value_option.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.value_option.setPlaceholderText(_translate("MainWindow", "0,00"))
        self.sale_option.setText(_translate("MainWindow", "Compra"))
        self.purchase_option.setText(_translate("MainWindow", "Venda"))
        self.purchase_sale_label.setText(_translate("MainWindow", "Marque a opção correspondente à transação:"))
        self.purchase_option_2.setText(_translate("MainWindow", "Compra"))
        self.sale_option_2.setText(_translate("MainWindow", "Venda"))
        self.date_label_2.setText(_translate("MainWindow", "Informe a data da transação:"))
        self.old_value_label.setText(_translate("MainWindow", "Informe o valor incorreto da transação (o valor registrado atualmente):"))
        self.coin_label_3.setText(_translate("MainWindow", "R$"))
        self.old_value_option.setPlaceholderText(_translate("MainWindow", "0,00"))
        self.new_value_label.setText(_translate("MainWindow", "Informe o novo valor da transação (o valor correto):"))
        self.coin_label_2.setText(_translate("MainWindow", "R$"))
        self.new_value_option.setPlaceholderText(_translate("MainWindow", "0,00"))
        self.edit_button_3.setText(_translate("MainWindow", "Editar"))
        self.back_button_2.setText(_translate("MainWindow", "Voltar"))
        self.page_title_2.setText(_translate("MainWindow", "Nesta área você irá alterar o valor de uma Compra OU Venda"))
        self.page_title_3.setText(_translate("MainWindow", "Nesta área você poderá excluir uma transação previamente cadastrada"))
        self.delete_button_3.setText(_translate("MainWindow", "Excluir"))
        self.back_button_3.setText(_translate("MainWindow", "Voltar"))
        self.label_3.setText(_translate("MainWindow", "R$"))
        self.label_2.setText(_translate("MainWindow", "Informe o valor da transação:"))
        self.label.setText(_translate("MainWindow", "Informe a data da transação:"))
        self.radioButton_2.setText(_translate("MainWindow", "Compra"))
        self.radioButton.setText(_translate("MainWindow", "Venda"))
        self.purchase_sale_label_2.setText(_translate("MainWindow", "Marque a opção correspondente à transação:"))
        self.from_date_label.setText(_translate("MainWindow", "Desde"))
        self.to_date_label.setText(_translate("MainWindow", "Até"))
        self.purchases_label.setText(_translate("MainWindow", "Compras"))
        self.sales_label.setText(_translate("MainWindow", "Vendas"))
        self.back_button_4.setText(_translate("MainWindow", "Voltar"))
        self.pushButton.setText(_translate("MainWindow", "Voltar"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
