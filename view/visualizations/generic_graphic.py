import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.canvas = Canvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas, *args)
        self.setLayout(self.vbl)


class Canvas(FigureCanvas):
    def __init__(self):
        self.fig = plt.Figure()
        plt.style.use('bmh')
        plt.rcParams['xtick.labelsize'] = 14
        plt.rcParams['ytick.labelsize'] = 14

        self.axis = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
