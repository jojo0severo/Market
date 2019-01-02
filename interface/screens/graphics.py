from handler import main_handler
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GraphicsScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Dynamic text
        self.mpl = MplWidget(self)
        self.mean = QtWidgets.QLabel(self)

        # Label
        self.label_graphic = QtWidgets.QLabel(self)
        self.label_mean = QtWidgets.QLabel(self)
        self.label_mean_coin = QtWidgets.QLabel(self)

        # Buttons
        self.back = QtWidgets.QPushButton(self)

        # Initialization
        self.open = None
        self.setup_ui()
        self.retranslate_ui()
        self.set_functions()

    def setup_ui(self):
        """Handle all the styling of the components"""

        # Window
        self.resize(1883, 1027)
        self.setStyleSheet("gridline-color: rgb(192, 255, 231);\n"
                           "selection-color: rgb(218, 255, 202);\n"
                           "background-color: rgb(255, 255, 255);")

        # ======================== Dynamics Stylesheet ===============================

        # Graph
        self.mpl.setGeometry(QtCore.QRect(50, 135, 1350, 850))

        # Mean of the named months
        self.mean.setGeometry(QtCore.QRect(1390, 385, 450, 81))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        self.mean.setFont(font)

        # ======================== Label Stylesheet ===============================

        # Title to the graph
        self.label_graphic.setGeometry(QtCore.QRect(150, 80, 871, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(26)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_graphic.setFont(font)

        # Label of the mean of the profits during the named months
        self.label_mean.setGeometry(QtCore.QRect(1320, 270, 540, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_mean.setFont(font)

        # Label containing the correct coin to the mean
        self.label_mean_coin.setGeometry(QtCore.QRect(1335, 390, 50, 71))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(18)
        self.label_mean_coin.setFont(font)

        # ======================== Button Stylesheet ===============================

        # Button to go back one window
        self.back.setGeometry(QtCore.QRect(1550, 860, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(-1)
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
                                "}"
                                "QPushButton:pressed"
                                "{"
                                "background-color: #989898;\n"
                                "color: white;\n"
                                "font-weight: bold;\n"
                                "}")

    def retranslate_ui(self):
        """Assign names and formats to the components"""

        # Window
        self.setWindowTitle("Dois irmãos")

        # ======================== Label Stylesheet ===============================

        self.label_graphic.setText(
            "<html><head/><body><p>Gráfico com a relação de lucro por mês</p><p><br/></p></body></html>")

        self.label_mean.setText('Média do período de 12 meses')
        self.label_mean_coin.setText('R$')

        # ======================== Button Stylesheet ===============================

        self.back.setText("Voltar")

        # ======================== Dynamic Stylesheet ===============================

        x, y, z = main_handler.consult_profit_x_month()

        self.mpl.canvas.ax.plot(x, y)
        self.mpl.canvas.draw()

        self.mean.setText(z)

    def set_functions(self):
        """Assign functions to the buttons"""

        self.back.clicked.connect(self.back_function)

    def back_function(self):
        self.close()


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = plt.Figure()
        plt.style.use('bmh')
        plt.rcParams['xtick.labelsize'] = 14
        plt.rcParams['ytick.labelsize'] = 14

        self.ax = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

