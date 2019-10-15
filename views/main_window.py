from PyQt5 import QtCore, QtGui, QtWidgets
from views.initial_page import InitialPage
from views.registration_page import RegistrationPage
from views.edition_page import EditionPage
from views.deletion_page import DeletionPage
from views.lists_page import ListsPage
from views.profit_graphic_page import ProfitGraphicPage
from views.purchases_graphic_page import PurchasesGraphicPage
from views.sales_graphic_page import SalesGraphicPage


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        super(AppMainWindow, self).__init__(*args)

        # Declaring main objects
        self.central_widget = QtWidgets.QWidget(self, *args)
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.stacked_widget = QtWidgets.QStackedWidget(self.central_widget)

        # Declaring pages
        self.initial_page = InitialPage()
        self.registration_page = RegistrationPage()
        self.edition_page = EditionPage()
        self.deletion_page = DeletionPage()
        self.lists_page = ListsPage()
        self.profit_graphic_page = ProfitGraphicPage()
        self.purchases_graphic_page = PurchasesGraphicPage()
        self.sales_graphic_page = SalesGraphicPage()

        # Starting window
        self.setup_ui()
        self.create_structure()

    def setup_ui(self):
        self.setWindowTitle('Dois irmãos')
        self.setStyleSheet('background-color:white;')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("market_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)

        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.setFont(font)
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))

    def create_structure(self):
        self.stacked_widget.addWidget(self.initial_page)
        self.stacked_widget.addWidget(self.registration_page)
        self.stacked_widget.addWidget(self.edition_page)
        self.stacked_widget.addWidget(self.deletion_page)
        self.stacked_widget.addWidget(self.lists_page)
        self.stacked_widget.addWidget(self.profit_graphic_page)
        self.stacked_widget.addWidget(self.purchases_graphic_page)
        self.stacked_widget.addWidget(self.sales_graphic_page)
        self.grid_layout.addWidget(self.stacked_widget, 0, 1, 1, 1)
        self.setCentralWidget(self.central_widget)
        self.stacked_widget.setCurrentIndex(0)


if __name__ == '__main__':
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    app = AppMainWindow()
    app.show()
    sys.exit(APP.exec())
