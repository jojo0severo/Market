from PyQt5 import QtCore, QtGui, QtWidgets


class InitialScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Buttons
        self.goto_register = QtWidgets.QPushButton(self)
        self.goto_graph = QtWidgets.QPushButton(self)
        self.goto_profit = QtWidgets.QPushButton(self)
        self.goto_delete = QtWidgets.QPushButton(self)

        # Initialization
        self.open = None
        self.setup_ui()
        self.retranslate_ui()
        self.set_functions()

    def setup_ui(self):
        """Handle all the styling of the components"""

        # Window
        self.setObjectName("Dois Irmãos")
        self.resize(1166, 1067)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("gridline-color: rgb(192, 255, 231);\n"
                           "selection-color: rgb(218, 255, 202);\n"
                           "background-color: rgb(255, 255, 255);")

        # ======================== Button Stylesheet ===============================

        # Button to go to the screen RegisterValuesScreen
        self.goto_register.setGeometry(QtCore.QRect(800, 110, 261, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goto_register.sizePolicy().hasHeightForWidth())
        self.goto_register.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
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
        self.goto_profit.setGeometry(QtCore.QRect(800, 320, 261, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goto_profit.sizePolicy().hasHeightForWidth())
        self.goto_profit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
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
        self.goto_graph.setGeometry(QtCore.QRect(800, 530, 261, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goto_graph.sizePolicy().hasHeightForWidth())
        self.goto_graph.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
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

        # Button to go to the Screen DeleteRegistersScreen
        self.goto_delete.setGeometry(QtCore.QRect(800, 740, 261, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goto_delete.sizePolicy().hasHeightForWidth())
        self.goto_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.goto_delete.setFont(font)
        self.goto_delete.setStyleSheet("QPushButton\n"
                                       "{\n"
                                       "  background-color: white;\n"
                                       "  color: black; \n"
                                       "  margin: 4px 2px;\n"
                                       "  text-align: center;\n"
                                       "  font-size: 24px;\n"
                                       "  border: 2px solid #ff6b6b;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover:!pressed\n"
                                       "{\n"
                                       "  background-color: #ff6b6b;\n"
                                       "color: white;\n"
                                       "font-weight:bold;\n"
                                       "}"
                                       "QPushButton:pressed"
                                       "{"
                                       "background-color: #ff6b6b;\n"
                                       "color: white;\n"
                                       "font-weight: bold;\n"
                                       "}"
                                       )

    def retranslate_ui(self):
        """Assign names and formats to the components"""

        self.setWindowTitle("Dois irmãos")

        # ======================== Button Stylesheet ===============================

        self.goto_register.setText("Cadastrar Valores")
        self.goto_graph.setText("Ver Gráfico")
        self.goto_profit.setText("Ver Lucro")
        self.goto_delete.setText("Apagar Registros")

    def set_functions(self):
        self.goto_register.clicked.connect(self.register_function)
        self.goto_profit.clicked.connect(self.profit_function)
        self.goto_graph.clicked.connect(self.graph_function)
        self.goto_delete.clicked.connect(self.delete_function)

    def register_function(self):
        from interface.screens.register_values import RegisterValuesScreen
        self.open = RegisterValuesScreen()
        self.open.showFullScreen()

    def profit_function(self):
        from interface.screens.profit import ProfitScreen
        self.open = ProfitScreen()
        self.open.showFullScreen()

    def graph_function(self):
        from interface.screens.graphics import GraphicsScreen
        self.open = GraphicsScreen()
        self.open.showFullScreen()

    def delete_function(self):
        from interface.screens.delete_registers import DeleteRegistersScreen
        self.open = DeleteRegistersScreen()
        self.open.showFullScreen()
