import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = Canvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)


class Canvas(FigureCanvas):
    def __init__(self):
        self.fig = plt.Figure()
        plt.style.use('bmh')
        plt.rcParams['xtick.labelsize'] = 12
        plt.rcParams['ytick.labelsize'] = 12

        self.axis = self.fig.add_subplot(111)
        self.axis.set_facecolor('xkcd:white')

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        FigureCanvas.updateGeometry(self)
