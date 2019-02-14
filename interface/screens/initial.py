"""This modules contains the initial screen that will always be running."""

import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from interface.screens.register_values import RegisterValuesScreen
from interface.screens.profit import ProfitScreen
from interface.screens.graphic import GraphicScreen
from interface.screens.view_values import ViewValuesScreen
from handler import main_handler


class InitialScreen(QtWidgets.QWidget):
    """Screen that will be always running and redirect to other selected screens."""

    def __init__(self):
        """Constructor."""
        super().__init__()

        # Buttons
        self.goto_register = QtWidgets.QPushButton(self)
        self.goto_graph = QtWidgets.QPushButton(self)
        self.goto_profit = QtWidgets.QPushButton(self)
        self.goto_view_values = QtWidgets.QPushButton(self)
        self.close_program = QtWidgets.QPushButton(self)
        self.turn_off = QtWidgets.QPushButton(self)

        # Load screens to RAM
        self.register_screen = RegisterValuesScreen()
        self.profit_screen = ProfitScreen()
        self.graphic_screen = GraphicScreen()
        self.view_values_screen = ViewValuesScreen()

        # Initialization
        self.setup_ui()
        self.translate_ui()
        self.set_functions()

    def setup_ui(self):
        """Handle all the styling of the components."""
        # Window
        self.setObjectName("Dois Irmãos")
        self.resize(1166, 1067)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                            QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setStyleSheet("gridline-color: rgb(192, 255, 231);\n"
                           "selection-color: rgb(218, 255, 202);\n"
                           "background-color: rgb(255, 255, 255);")

        # ======================== Button Stylesheet ===============================

        # Button to go to the screen RegisterValuesScreen
        self.goto_register.setGeometry(QtCore.QRect(480, 40, 281, 131))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                            QtWidgets.QSizePolicy.Maximum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.goto_register.sizePolicy().hasHeightForWidth())
        self.goto_register.setSizePolicy(size_policy)
        font = QtGui.QFont()
        self.goto_register.setFont(font)
        self.goto_register.setStyleSheet("QPushButton\n"
                                         "{\n"
                                         "  background-color: white;\n"
                                         "  color: black; \n"
                                         "  margin: 4px 2px;\n"
                                         "  text-align: center;\n"
                                         "  font-size: 24px;\n"
                                         "  border: 2px solid #4CAF50;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover:!pressed\n"
                                         "{\n"
                                         "background-color: #4CAF50;\n"
                                         "color: white;\n"
                                         "font-weight: bold;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed"
                                         "{"
                                         "background-color: #4CAF50;\n"
                                         "color: white;\n"
                                         "font-weight: bold;\n"
                                         "}")

        # Button to go to the screen ProfitScreen
        self.goto_profit.setGeometry(QtCore.QRect(480, 190, 281, 131))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.goto_profit.sizePolicy().hasHeightForWidth())
        self.goto_profit.setSizePolicy(size_policy)
        font = QtGui.QFont()
        self.goto_profit.setFont(font)
        self.goto_profit.setStyleSheet("QPushButton\n"
                                       "{\n"
                                       "  background-color: white;\n"
                                       "  color: black; \n"
                                       "  margin: 4px 2px;\n"
                                       "  text-align: center;\n"
                                       "  font-size: 24px;\n"
                                       "  border: 2px solid #d1f101;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover:!pressed\n"
                                       "{\n"
                                       "background-color: #d1f101;\n"
                                       "color: white;\n"
                                       "font-weight: bold;\n"
                                       "}"
                                       "QPushButton:pressed"
                                       "{"
                                       "background-color: #d1f101;\n"
                                       "color: white;\n"
                                       "font-weight: bold;\n"
                                       "}"
                                       )

        # Button to go to the screen GraphicsScreen
        self.goto_graph.setGeometry(QtCore.QRect(480, 340, 281, 131))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.goto_graph.sizePolicy().hasHeightForWidth())
        self.goto_graph.setSizePolicy(size_policy)
        font = QtGui.QFont()
        self.goto_graph.setFont(font)
        self.goto_graph.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "  background-color:  white;\n"
                                      "  color: black; \n"
                                      "  margin: 4px 2px;\n"
                                      "  text-align: center;\n"
                                      "  font-size: 24px;\n"
                                      "  border: 2px solid #6b7ce6;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover:!pressed\n"
                                      "{\n"
                                      "background-color: #6b7ce6;\n"
                                      "color: white;\n"
                                      "font-weight: bold;\n"
                                      "}"
                                      "QPushButton:pressed"
                                      "{"
                                      "background-color: #6b7ce6;\n"
                                      "color: white;\n"
                                      "font-weight: bold;\n"
                                      "}")

        # Button to go to the screen ViewValuesScreen
        self.goto_view_values.setGeometry(QtCore.QRect(480, 490, 281, 131))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.goto_view_values.sizePolicy().hasHeightForWidth())
        self.goto_view_values.setSizePolicy(size_policy)
        font = QtGui.QFont()
        self.goto_view_values.setFont(font)
        self.goto_view_values.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "  background-color:  white;\n"
                                            "  color: black; \n"
                                            "  margin: 4px 2px;\n"
                                            "  text-align: center;\n"
                                            "  font-size: 24px;\n"
                                            "  border: 2px solid #C86BCB;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover:!pressed\n"
                                            "{\n"
                                            "background-color: #C86BCB;\n"
                                            "color: white;\n"
                                            "font-weight: bold;\n"
                                            "}"
                                            "QPushButton:pressed"
                                            "{"
                                            "background-color: #C86BCB;\n"
                                            "color: white;\n"
                                            "font-weight: bold;\n"
                                            "}")

        # Button to close the program
        self.close_program.setGeometry(QtCore.QRect(1100, 600, 231, 111))
        font = QtGui.QFont()
        self.close_program.setFont(font)
        self.close_program.setStyleSheet("QPushButton\n"
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

        # Button to turn off computer
        self.turn_off.setGeometry(QtCore.QRect(860, 600, 231, 111))
        font = QtGui.QFont()
        self.turn_off.setFont(font)
        self.turn_off.setStyleSheet("QPushButton\n"
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
        self.turn_off.setDisabled(True)

    def translate_ui(self):
        """Assign names and formats to the components."""
        self.setWindowTitle("Dois irmãos")

        # ======================== Button Stylesheet ===============================

        self.goto_register.setText("Cadastrar Valores")
        self.goto_graph.setText("Ver Gráfico")
        self.goto_profit.setText("Ver Lucro")
        self.goto_view_values.setText("Ver Vendas e Compras")
        self.close_program.setText("Sair")
        self.turn_off.setText("Desligar")

    def set_functions(self):
        """Assign functions to each button."""
        self.goto_register.clicked.connect(self.register_function)
        self.goto_profit.clicked.connect(self.profit_function)
        self.goto_graph.clicked.connect(self.graph_function)
        self.goto_view_values.clicked.connect(self.view_values_function)
        self.close_program.clicked.connect(self.close_function)
        self.turn_off.clicked.connect(self.turn_off_function)

    def register_function(self):
        """Open the screen RegisterValues."""
        self.register_screen.sales_text.setText("")
        self.register_screen.purchases_text.setText("")
        self.register_screen.showFullScreen()

    def profit_function(self):
        """Open the screen Profit."""
        self.profit_screen.translate_ui()
        self.profit_screen.showFullScreen()

    def graph_function(self):
        """Open the screen Graphic."""
        self.graphic_screen.translate_ui()
        self.graphic_screen.showFullScreen()

    def view_values_function(self):
        self.view_values_screen.update_tables()
        self.view_values_screen.showFullScreen()

    def close_function(self):
        """Close the program"""
        main_handler.close()
        self.close()
        raise SystemExit

    def turn_off_function(self):
        """Turn off the computer"""
        main_handler.close()
        self.close()

        if sys.platform == 'win32':
            subprocess.call(["shutdown", "/s", "/t", "0"])
        else:
            subprocess.call(["shutdown", "-h", "now"])
