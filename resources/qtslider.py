# slide Bar Range example.
# max min interval + date example.

from PyQt5 import QtCore, QtGui, QtWidgets


MAXVAL = 650000


class QRangeSlider(QtWidgets.QWidget):

    def __init__(self, parent, *args):
        super(QRangeSlider, self).__init__(parent=parent, *args)

        self.sliders_box_layout = QtWidgets.QHBoxLayout(self)

        self.start_slider = QtWidgets.QSlider(self)
        self.end_slider = QtWidgets.QSlider(self)

        self.create_structure()

    def create_structure(self):
        self.setMinimumSize(QtCore.QSize(0, 45))
        self.setMaximumSize(QtCore.QSize(16777215, 55))

        self.start_slider.setOrientation()

        self.sliders_box_layout.setContentsMargins(0, 0, 0, 0)
        self.sliders_box_layout.setSpacing(0)
        self.sliders_box_layout.addWidget(self.start_slider, alignment=QtCore.Qt.AlignRight)
        self.sliders_box_layout.addWidget(self.end_slider, alignment=QtCore.Qt.AlignLeft)

        # self.s