from PyQt5 import QtCore, QtGui, QtWidgets
from view.operations.initial_page import InitialPage
from view.operations.registration_page import RegistrationPage
from view.operations.edition_page import EditionPage
from view.operations.deletion_page import DeletionPage
from view.visualizations.lists_page import ListsPage
from view.visualizations.purchase_list_with_filters import PurchaseListPage
from view.visualizations.sale_list_with_filters import SaleListPage


class AppMainWindow(QtWidgets.QMainWindow):

    navigation_signal = QtCore.pyqtSignal(int)
    back_signal = QtCore.pyqtSignal()

    def __init__(self, *args):
        super(AppMainWindow, self).__init__(*args)

        self.navigation_signal.connect(self.open_page)
        self.back_signal.connect(self.set_page)

        # Declaring main objects
        self.central_widget = QtWidgets.QWidget(self, *args)
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.stacked_widget = QtWidgets.QStackedWidget(self.central_widget)

        # Declaring pages
        self.initial_page = InitialPage(self.navigation_signal)
        self.pages = [
            RegistrationPage(self.back_signal),
            EditionPage(self.back_signal),
            DeletionPage(self.back_signal),
            ListsPage(self.back_signal),
            SaleListPage(self.back_signal),
            PurchaseListPage(self.back_signal)
        ]

        # Building UI
        self.setup_ui()
        self.translate_ui()
        self.create_structure()

    def setup_ui(self):
        self.setObjectName('MainWindow')
        self.setStyleSheet('background-color:white;')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/market_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.initial_page.setFont(font)
        self.initial_page.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        for page in self.pages:
            page.setFont(font)
            page.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))

        self.setFont(font)
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate('MainWindow', 'Dois irmãos'))

    def create_structure(self):
        self.stacked_widget.addWidget(self.initial_page)
        for page in self.pages:
            self.stacked_widget.addWidget(page)

        self.grid_layout.addWidget(self.stacked_widget, 0, 1, 1, 1)
        self.setCentralWidget(self.central_widget)
        self.stacked_widget.setCurrentIndex(0)

    @QtCore.pyqtSlot(int)
    def open_page(self, page):
        self.pages[page-1].clear()
        self.stacked_widget.setCurrentIndex(page)

    @QtCore.pyqtSlot()
    def set_page(self):
        self.stacked_widget.setCurrentIndex(0)
