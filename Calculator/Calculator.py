from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(540, 471)
        mainWindow.setMinimumSize(QtCore.QSize(540, 471))
        mainWindow.setMaximumSize(QtCore.QSize(540, 471))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/calcicon/calc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255)\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(0, 0, 541, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.tab.setFont(font)
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet("")
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab.setElideMode(QtCore.Qt.ElideNone)
        self.tab.setDocumentMode(False)
        self.tab.setTabsClosable(False)
        self.tab.setMovable(False)
        self.tab.setTabBarAutoHide(False)
        self.tab.setObjectName("tab")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setAccessibleName("")
        self.tab1.setAutoFillBackground(False)
        self.tab1.setStyleSheet("background-color: #06283D;RR")
        self.tab1.setObjectName("tab1")
        self.btnAdd_1 = QtWidgets.QPushButton(self.tab1)
        self.btnAdd_1.setGeometry(QtCore.QRect(260, 270, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnAdd_1.setFont(font)
        self.btnAdd_1.setStyleSheet("QPushButton{\n"
                                    "background: #256D85;\n"
                                    "color:white;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color:#47B5FF;\n"
                                     "}")
        self.btnAdd_1.setObjectName("btnAdd_1")
        self.btnSubtract_1 = QtWidgets.QPushButton(self.tab1)
        self.btnSubtract_1.setGeometry(QtCore.QRect(390, 270, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnSubtract_1.setFont(font)
        self.btnSubtract_1.setStyleSheet("QPushButton{\n"
                                         "background: #256D85;\n"
                                         "color:white;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color:#47B5FF;\n"
                                         "}")
        self.btnSubtract_1.setObjectName("btnSubtract_1")
        self.btnMulti_1 = QtWidgets.QPushButton(self.tab1)
        self.btnMulti_1.setGeometry(QtCore.QRect(390, 210, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnMulti_1.setFont(font)
        self.btnMulti_1.setStyleSheet("QPushButton{\n"
                                      "background: #256D85;\n"
                                      "color:white;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:#47B5FF;\n"
                                      "}")
        self.btnMulti_1.setObjectName("btnMulti_1")
        self.btndiv_1 = QtWidgets.QPushButton(self.tab1)
        self.btndiv_1.setGeometry(QtCore.QRect(260, 210, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btndiv_1.setFont(font)
        self.btndiv_1.setStyleSheet("QPushButton{\n"
                                    "background: #256D85;\n"
                                    "color:white;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:#47B5FF;\n"
                                    "}")
        self.btndiv_1.setObjectName("btndiv_1")
        self.btnEqual_1 = QtWidgets.QPushButton(self.tab1)
        self.btnEqual_1.setGeometry(QtCore.QRect(260, 330, 260, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnEqual_1.setFont(font)
        self.btnEqual_1.setStyleSheet("QPushButton{\n"
                                      "background:#7FBCD2;\n"
                                      "color:white;\n"
                                      "border-bottom-left-radius : 20px;\n"
                                      "border-bottom-right-radius : 20px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:#3AB4F2;\n"
                                      "}")
        self.btnEqual_1.setObjectName("btnEqual_1")
        self.btn7_1 = QtWidgets.QPushButton(self.tab1)
        self.btn7_1.setGeometry(QtCore.QRect(20, 150, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn7_1.setFont(font)
        self.btn7_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn7_1.setObjectName("btn7_1")
        self.btn8_1 = QtWidgets.QPushButton(self.tab1)
        self.btn8_1.setGeometry(QtCore.QRect(90, 150, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn8_1.setFont(font)
        self.btn8_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn8_1.setObjectName("btn8_1")
        self.btn9_1 = QtWidgets.QPushButton(self.tab1)
        self.btn9_1.setGeometry(QtCore.QRect(160, 150, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn9_1.setFont(font)
        self.btn9_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn9_1.setObjectName("btn9_1")
        self.btn4_1 = QtWidgets.QPushButton(self.tab1)
        self.btn4_1.setGeometry(QtCore.QRect(20, 210, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn4_1.setFont(font)
        self.btn4_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn4_1.setObjectName("btn4_1")
        self.btn5_1 = QtWidgets.QPushButton(self.tab1)
        self.btn5_1.setGeometry(QtCore.QRect(90, 210, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn5_1.setFont(font)
        self.btn5_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn5_1.setObjectName("btn5_1")
        self.btn6_1 = QtWidgets.QPushButton(self.tab1)
        self.btn6_1.setGeometry(QtCore.QRect(160, 210, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn6_1.setFont(font)
        self.btn6_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn6_1.setObjectName("btn6_1")
        self.btn1_1 = QtWidgets.QPushButton(self.tab1)
        self.btn1_1.setGeometry(QtCore.QRect(20, 270, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn1_1.setFont(font)
        self.btn1_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn1_1.setObjectName("btn1_1")
        self.btn2_1 = QtWidgets.QPushButton(self.tab1)
        self.btn2_1.setGeometry(QtCore.QRect(90, 270, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn2_1.setFont(font)
        self.btn2_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn2_1.setObjectName("btn2_1")
        self.btn3_1 = QtWidgets.QPushButton(self.tab1)
        self.btn3_1.setGeometry(QtCore.QRect(160, 270, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn3_1.setFont(font)
        self.btn3_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn3_1.setObjectName("btn3_1")
        self.btn00_1 = QtWidgets.QPushButton(self.tab1)
        self.btn00_1.setGeometry(QtCore.QRect(90, 330, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn00_1.setFont(font)
        self.btn00_1.setStyleSheet("QPushButton{\n"
                                   "background: #256D85;\n"
                                   "color:white;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:#47B5FF;\n"
                                   "}")
        self.btn00_1.setObjectName("btn00_1")
        self.btnDot_1 = QtWidgets.QPushButton(self.tab1)
        self.btnDot_1.setGeometry(QtCore.QRect(160, 330, 70, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnDot_1.setFont(font)
        self.btnDot_1.setStyleSheet("QPushButton{\n"
                                    "background: #256D85;\n"
                                    "color:white;\n"
                                    "border-bottom-right-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:#47B5FF;;\n"
                                    "}")
        self.btnDot_1.setObjectName("btnDot_1")
        self.btn0_1 = QtWidgets.QPushButton(self.tab1)
        self.btn0_1.setGeometry(QtCore.QRect(20, 330, 70, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn0_1.setFont(font)
        self.btn0_1.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "border-bottom-left-radius : 20px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;;\n"
                                  "}")
        self.btn0_1.setObjectName("btn0_1")
        self.lineEditScreen = QtWidgets.QLineEdit(self.tab1)
        self.lineEditScreen.setGeometry(QtCore.QRect(20, 10, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEditScreen.setFont(font)
        self.lineEditScreen.setStyleSheet("background: #DFF6FF ;\n"
                                          "border-radius : 5px;\n"
                                          "\n"
                                          "")
        self.lineEditScreen.setReadOnly(True)
        self.lineEditScreen.setObjectName("lineEditScreen")
        self.btnLeftBracket_1 = QtWidgets.QPushButton(self.tab1)
        self.btnLeftBracket_1.setGeometry(QtCore.QRect(20, 90, 70, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnLeftBracket_1.setFont(font)
        self.btnLeftBracket_1.setStyleSheet("QPushButton{\n"
                                            "background: #256D85;\n"
                                            "color:white;\n"
                                            "border-top-left-radius : 20px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color:#47B5FF;\n"
                                            "}")
        self.btnLeftBracket_1.setObjectName("btnLeftBracket_1")
        self.btnANS_1 = QtWidgets.QPushButton(self.tab1)
        self.btnANS_1.setGeometry(QtCore.QRect(160, 90, 70, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.btnANS_1.setFont(font)
        self.btnANS_1.setStyleSheet("QPushButton{\n"
                                    "background: #256D85;\n"
                                    "color:white;\n"
                                    "border-top-right-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:#47B5FF;;\n"
                                    "}")
        self.btnANS_1.setObjectName("btnANS_1")
        self.btnRightBracket_1 = QtWidgets.QPushButton(self.tab1)
        self.btnRightBracket_1.setGeometry(QtCore.QRect(90, 90, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnRightBracket_1.setFont(font)
        self.btnRightBracket_1.setStyleSheet("QPushButton{\n"
                                             "background: #256D85;\n"
                                             "color:white;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color:#47B5FF;\n"
                                             "}")
        self.btnRightBracket_1.setObjectName("btnRightBracket_1")
        self.btnAC_1 = QtWidgets.QPushButton(self.tab1)
        self.btnAC_1.setGeometry(QtCore.QRect(260, 90, 130, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnAC_1.setFont(font)
        self.btnAC_1.setStyleSheet("QPushButton{\n"
                                   "background: rgb(207, 0, 3);\n"
                                   "color:white;\n"
                                   "border-top-left-radius : 20px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:rgb(235, 6, 10);\n"
                                   "}")
        self.btnAC_1.setObjectName("btnAC_1")
        self.btnDEL_1 = QtWidgets.QPushButton(self.tab1)
        self.btnDEL_1.setGeometry(QtCore.QRect(390, 90, 130, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnDEL_1.setFont(font)
        self.btnDEL_1.setStyleSheet("QPushButton{\n"
                                    "background: rgb(207, 0, 3);\n"
                                    "color:white;\n"
                                    "border-top-right-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:rgb(235, 6, 10);\n"
                                    "}")
        self.btnDEL_1.setObjectName("btnDEL_1")
        self.btnPercent_1 = QtWidgets.QPushButton(self.tab1)
        self.btnPercent_1.setGeometry(QtCore.QRect(260, 150, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnPercent_1.setFont(font)
        self.btnPercent_1.setStyleSheet("QPushButton{\n"
                                        "background: #256D85;\n"
                                        "color:white;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color:#47B5FF;\n"
                                        "}")
        self.btnPercent_1.setObjectName("btnPercent_1")
        self.btnMinPls_1 = QtWidgets.QPushButton(self.tab1)
        self.btnMinPls_1.setGeometry(QtCore.QRect(390, 150, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnMinPls_1.setFont(font)
        self.btnMinPls_1.setStyleSheet("QPushButton{\n"
                                       "background: #256D85;\n"
                                       "color:white;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color:#47B5FF;\n"
                                       "}")
        self.btnMinPls_1.setObjectName("btnMinPls_1")
        self.btnDEL_1.raise_()
        self.lineEditScreen.raise_()
        self.btnAC_1.raise_()
        self.btnPercent_1.raise_()
        self.btnMinPls_1.raise_()
        self.btndiv_1.raise_()
        self.btnMulti_1.raise_()
        self.btnAdd_1.raise_()
        self.btnSubtract_1.raise_()
        self.btnEqual_1.raise_()
        self.btnLeftBracket_1.raise_()
        self.btnRightBracket_1.raise_()
        self.btnANS_1.raise_()
        self.btn7_1.raise_()
        self.btn8_1.raise_()
        self.btn9_1.raise_()
        self.btn4_1.raise_()
        self.btn5_1.raise_()
        self.btn6_1.raise_()
        self.btn1_1.raise_()
        self.btn2_1.raise_()
        self.btn3_1.raise_()
        self.btn0_1.raise_()
        self.btn00_1.raise_()
        self.btnDot_1.raise_()
        icon = QtGui.QIcon.fromTheme("k")
        self.tab.addTab(self.tab1, icon, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setStyleSheet("background-color: #06283D;")
        self.tab2.setObjectName("tab2")
        self.lineEditScreen2 = QtWidgets.QLineEdit(self.tab2)
        self.lineEditScreen2.setGeometry(QtCore.QRect(20, 10, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEditScreen2.setFont(font)
        self.lineEditScreen2.setAutoFillBackground(False)
        self.lineEditScreen2.setStyleSheet("background: #DFF6FF ;\n"
                                           "border-radius : 5px;")
        self.lineEditScreen2.setReadOnly(True)
        self.lineEditScreen2.setObjectName("lineEditScreen2")
        self.btn8_2 = QtWidgets.QPushButton(self.tab2)
        self.btn8_2.setGeometry(QtCore.QRect(80, 150, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn8_2.setFont(font)
        self.btn8_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn8_2.setObjectName("btn8_2")
        self.btn6_2 = QtWidgets.QPushButton(self.tab2)
        self.btn6_2.setGeometry(QtCore.QRect(140, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn6_2.setFont(font)
        self.btn6_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn6_2.setObjectName("btn6_2")
        self.btnPi = QtWidgets.QPushButton(self.tab2)
        self.btnPi.setGeometry(QtCore.QRect(220, 90, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnPi.setFont(font)
        self.btnPi.setStyleSheet("QPushButton{\n"
                                 "background: #002E94;\n"
                                 "color:white;\n"
                                 "border-top-left-radius : 20px;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color:#1746A2;\n"
                                 "}R")
        self.btnPi.setObjectName("btnPi")
        self.btn7_2 = QtWidgets.QPushButton(self.tab2)
        self.btn7_2.setGeometry(QtCore.QRect(20, 150, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn7_2.setFont(font)
        self.btn7_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn7_2.setObjectName("btn7_2")
        self.btnLeftBracket_2 = QtWidgets.QPushButton(self.tab2)
        self.btnLeftBracket_2.setGeometry(QtCore.QRect(20, 90, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnLeftBracket_2.setFont(font)
        self.btnLeftBracket_2.setStyleSheet("QPushButton{\n"
                                            "background: #256D85;\n"
                                            "color:white;\n"
                                            "border-top-left-radius : 20px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color:#47B5FF;\n"
                                            "}")
        self.btnLeftBracket_2.setObjectName("btnLeftBracket_2")
        self.btnRightBracket_2 = QtWidgets.QPushButton(self.tab2)
        self.btnRightBracket_2.setGeometry(QtCore.QRect(80, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnRightBracket_2.setFont(font)
        self.btnRightBracket_2.setStyleSheet("QPushButton{\n"
                                             "background: #256D85;\n"
                                             "color:white;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color:#47B5FF;\n"
                                             "}")
        self.btnRightBracket_2.setObjectName("btnRightBracket_2")
        self.btn3_2 = QtWidgets.QPushButton(self.tab2)
        self.btn3_2.setGeometry(QtCore.QRect(140, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn3_2.setFont(font)
        self.btn3_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn3_2.setObjectName("btn3_2")
        self.btnDot_2 = QtWidgets.QPushButton(self.tab2)
        self.btnDot_2.setGeometry(QtCore.QRect(140, 330, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnDot_2.setFont(font)
        self.btnDot_2.setStyleSheet("QPushButton{\n"
                                    "background: #256D85;\n"
                                    "color:white;\n"
                                    "border-bottom-right-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:#47B5FF;\n"
                                    "}")
        self.btnDot_2.setObjectName("btnDot_2")
        self.btn9_2 = QtWidgets.QPushButton(self.tab2)
        self.btn9_2.setGeometry(QtCore.QRect(140, 150, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn9_2.setFont(font)
        self.btn9_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn9_2.setObjectName("btn9_2")
        self.btn5_2 = QtWidgets.QPushButton(self.tab2)
        self.btn5_2.setGeometry(QtCore.QRect(80, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn5_2.setFont(font)
        self.btn5_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn5_2.setObjectName("btn5_2")
        self.btn2_2 = QtWidgets.QPushButton(self.tab2)
        self.btn2_2.setGeometry(QtCore.QRect(80, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn2_2.setFont(font)
        self.btn2_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn2_2.setObjectName("btn2_2")
        self.btn00_2 = QtWidgets.QPushButton(self.tab2)
        self.btn00_2.setGeometry(QtCore.QRect(80, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn00_2.setFont(font)
        self.btn00_2.setStyleSheet("QPushButton{\n"
                                   "background: #256D85;\n"
                                   "color:white;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:#47B5FF;\n"
                                   "}")
        self.btn00_2.setObjectName("btn00_2")
        self.btn0_2 = QtWidgets.QPushButton(self.tab2)
        self.btn0_2.setGeometry(QtCore.QRect(20, 330, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn0_2.setFont(font)
        self.btn0_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "border-bottom-left-radius : 20px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn0_2.setObjectName("btn0_2")
        self.btn1_2 = QtWidgets.QPushButton(self.tab2)
        self.btn1_2.setGeometry(QtCore.QRect(20, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn1_2.setFont(font)
        self.btn1_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn1_2.setObjectName("btn1_2")
        self.btn4_2 = QtWidgets.QPushButton(self.tab2)
        self.btn4_2.setGeometry(QtCore.QRect(20, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn4_2.setFont(font)
        self.btn4_2.setStyleSheet("QPushButton{\n"
                                  "background: #256D85;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#47B5FF;\n"
                                  "}")
        self.btn4_2.setObjectName("btn4_2")
        self.btnSin = QtWidgets.QPushButton(self.tab2)
        self.btnSin.setGeometry(QtCore.QRect(280, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btnSin.setFont(font)
        self.btnSin.setStyleSheet("QPushButton{\n"
                                  "background: #002E94;\n"
                                  "color:white;\n"
                                  "\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#1746A2;\n"
                                  "}R")
        self.btnSin.setObjectName("btnSin")
        self.btnaRoot = QtWidgets.QPushButton(self.tab2)
        self.btnaRoot.setGeometry(QtCore.QRect(220, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnaRoot.setFont(font)
        self.btnaRoot.setStyleSheet("QPushButton{\n"
                                    "background: #002E94;\n"
                                    "color:white;\n"
                                    "\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:#1746A2;\n"
                                    "}R")
        self.btnaRoot.setObjectName("btnaRoot")
        self.btnLog = QtWidgets.QPushButton(self.tab2)
        self.btnLog.setGeometry(QtCore.QRect(340, 150, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.btnLog.setFont(font)
        self.btnLog.setStyleSheet("QPushButton{\n"
                                  "background: #002E94;\n"
                                  "color:white;\n"
                                  "\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#1746A2;\n"
                                  "}R")
        self.btnLog.setObjectName("btnLog")
        self.btnLn = QtWidgets.QPushButton(self.tab2)
        self.btnLn.setGeometry(QtCore.QRect(280, 150, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnLn.setFont(font)
        self.btnLn.setStyleSheet("QPushButton{\n"
                                 "background: #002E94;\n"
                                 "color:white;\n"
                                 "\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color:#1746A2;\n"
                                 "}R")
        self.btnLn.setObjectName("btnLn")
        self.btnCosh = QtWidgets.QPushButton(self.tab2)
        self.btnCosh.setGeometry(QtCore.QRect(340, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.btnCosh.setFont(font)
        self.btnCosh.setStyleSheet("QPushButton{\n"
                                   "background: #002E94;\n"
                                   "color:white;\n"
                                   "\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:#1746A2;\n"
                                   "}R")
        self.btnCosh.setObjectName("btnCosh")
        self.btnCos = QtWidgets.QPushButton(self.tab2)
        self.btnCos.setGeometry(QtCore.QRect(280, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.btnCos.setFont(font)
        self.btnCos.setStyleSheet("QPushButton{\n"
                                  "background: #002E94;\n"
                                  "color:white;\n"
                                  "\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#1746A2;\n"
                                  "}R")
        self.btnCos.setObjectName("btnCos")
        self.btn_e = QtWidgets.QPushButton(self.tab2)
        self.btn_e.setGeometry(QtCore.QRect(220, 150, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_e.setFont(font)
        self.btn_e.setStyleSheet("QPushButton{\n"
                                 "background: #002E94;\n"
                                 "color:white;\n"
                                 "\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "background-color:#1746A2;\n"
                                 "}R")
        self.btn_e.setObjectName("btn_e")
        self.btnTanh = QtWidgets.QPushButton(self.tab2)
        self.btnTanh.setGeometry(QtCore.QRect(340, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.btnTanh.setFont(font)
        self.btnTanh.setStyleSheet("QPushButton{\n"
                                   "background: #002E94;\n"
                                   "color:white;\n"
                                   "\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:#1746A2;\n"
                                   "}R")
        self.btnTanh.setObjectName("btnTanh")
        self.btnTan = QtWidgets.QPushButton(self.tab2)
        self.btnTan.setGeometry(QtCore.QRect(280, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btnTan.setFont(font)
        self.btnTan.setStyleSheet("QPushButton{\n"
                                  "background: #002E94;\n"
                                  "color:white;\n"
                                  "\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#1746A2;\n"
                                  "}R")
        self.btnTan.setObjectName("btnTan")
        self.btnEXP = QtWidgets.QPushButton(self.tab2)
        self.btnEXP.setGeometry(QtCore.QRect(280, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btnEXP.setFont(font)
        self.btnEXP.setStyleSheet("QPushButton{\n"
                                  "background: #002E94;\n"
                                  "color:white;\n"
                                  "\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "background-color:#1746A2;\n"
                                  "}R")
        self.btnEXP.setObjectName("btnEXP")
        self.btnSinh = QtWidgets.QPushButton(self.tab2)
        self.btnSinh.setGeometry(QtCore.QRect(340, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btnSinh.setFont(font)
        self.btnSinh.setStyleSheet("QPushButton{\n"
                                   "background: #002E94;\n"
                                   "color:white;\n"
                                   "\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:#1746A2;\n"
                                   "}R")
        self.btnSinh.setObjectName("btnSinh")
        self.btnANS_2 = QtWidgets.QPushButton(self.tab2)
        self.btnANS_2.setGeometry(QtCore.QRect(140, 90, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btnANS_2.setFont(font)
        self.btnANS_2.setStyleSheet("QPushButton{\n"
                                    "background: #256D85;\n"
                                    "color:white;\n"
                                    "border-top-right-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:#47B5FF;\n"
                                    "}")
        self.btnANS_2.setObjectName("btnANS_2")
        self.btnEqual_2 = QtWidgets.QPushButton(self.tab2)
        self.btnEqual_2.setGeometry(QtCore.QRect(400, 330, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnEqual_2.setFont(font)
        self.btnEqual_2.setStyleSheet("QPushButton{\n"
                                      "background:#7FBCD2;\n"
                                      "color:white;\n"
                                      "border-bottom-right-radius : 20px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:#3AB4F2;\n"
                                      "}")
        self.btnEqual_2.setObjectName("btnEqual_2")
        self.btnAdd_2 = QtWidgets.QPushButton(self.tab2)
        self.btnAdd_2.setGeometry(QtCore.QRect(400, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnAdd_2.setFont(font)
        self.btnAdd_2.setStyleSheet("QPushButton{\n"
                                    "background: #256D85;\n"
                                    "color:white;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:#47B5FF;\n"
                                    "}")
        self.btnAdd_2.setObjectName("btnAdd_2")
        self.btnSubtract_2 = QtWidgets.QPushButton(self.tab2)
        self.btnSubtract_2.setGeometry(QtCore.QRect(460, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnSubtract_2.setFont(font)
        self.btnSubtract_2.setStyleSheet("QPushButton{\n"
                                         "background: #256D85;\n"
                                         "color:white;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color:#47B5FF;\n"
                                         "}")
        self.btnSubtract_2.setObjectName("btnSubtract_2")
        self.btnMulti_2 = QtWidgets.QPushButton(self.tab2)
        self.btnMulti_2.setGeometry(QtCore.QRect(400, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnMulti_2.setFont(font)
        self.btnMulti_2.setStyleSheet("QPushButton{\n"
                                      "background: #256D85;\n"
                                      "color:white;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:#47B5FF;\n"
                                      "}")
        self.btnMulti_2.setObjectName("btnMulti_2")
        self.btndiv_2 = QtWidgets.QPushButton(self.tab2)
        self.btndiv_2.setGeometry(QtCore.QRect(460, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btndiv_2.setFont(font)
        self.btndiv_2.setStyleSheet("QPushButton{\n"
                                    "background: #256D85;\n"
                                    "color:white;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:#47B5FF;\n"
                                    "}")
        self.btndiv_2.setObjectName("btndiv_2")
        self.btnDEL_2 = QtWidgets.QPushButton(self.tab2)
        self.btnDEL_2.setGeometry(QtCore.QRect(400, 90, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnDEL_2.setFont(font)
        self.btnDEL_2.setStyleSheet("QPushButton{\n"
                                    "background: rgb(207, 0, 3);\n"
                                    "color:white;\n"
                                    "border-top-right-radius : 20px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:rgb(235, 6, 10);\n"
                                    "}")
        self.btnDEL_2.setObjectName("btnDEL_2")
        self.btnAC_2 = QtWidgets.QPushButton(self.tab2)
        self.btnAC_2.setGeometry(QtCore.QRect(400, 150, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnAC_2.setFont(font)
        self.btnAC_2.setStyleSheet("QPushButton{\n"
                                   "background: rgb(207, 0, 3);\n"
                                   "color:white;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:rgb(235, 6, 10);\n"
                                   "}")
        self.btnAC_2.setObjectName("btnAC_2")
        self.btnPercent_2 = QtWidgets.QPushButton(self.tab2)
        self.btnPercent_2.setGeometry(QtCore.QRect(220, 330, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnPercent_2.setFont(font)
        self.btnPercent_2.setStyleSheet("QPushButton{\n"
                                        "background: #002E94;\n"
                                        "color:white;\n"
                                        "border-bottom-left-radius : 20px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color:#1746A2;\n"
                                        "}R")
        self.btnPercent_2.setObjectName("btnPercent_2")
        self.btnFact = QtWidgets.QPushButton(self.tab2)
        self.btnFact.setGeometry(QtCore.QRect(220, 270, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btnFact.setFont(font)
        self.btnFact.setStyleSheet("QPushButton{\n"
                                   "background: #002E94;\n"
                                   "color:white;\n"
                                   "\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:#1746A2;\n"
                                   "}R")
        self.btnFact.setObjectName("btnFact")
        self.btnMinPls_2 = QtWidgets.QPushButton(self.tab2)
        self.btnMinPls_2.setGeometry(QtCore.QRect(340, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.btnMinPls_2.setFont(font)
        self.btnMinPls_2.setStyleSheet("QPushButton{\n"
                                       "background: #002E94;\n"
                                       "color:white;\n"
                                       "\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color:#1746A2;\n"
                                       "}R")
        self.btnMinPls_2.setObjectName("btnMinPls_2")
        self.lineEditScreen2.raise_()
        self.btnLeftBracket_2.raise_()
        self.btnRightBracket_2.raise_()
        self.btnANS_2.raise_()
        self.btn7_2.raise_()
        self.btn8_2.raise_()
        self.btn9_2.raise_()
        self.btn4_2.raise_()
        self.btn5_2.raise_()
        self.btn6_2.raise_()
        self.btn1_2.raise_()
        self.btn2_2.raise_()
        self.btn3_2.raise_()
        self.btn0_2.raise_()
        self.btn00_2.raise_()
        self.btnDot_2.raise_()
        self.btnPi.raise_()
        self.btnEXP.raise_()
        self.btnMinPls_2.raise_()
        self.btnDEL_2.raise_()
        self.btn_e.raise_()
        self.btnLn.raise_()
        self.btnLog.raise_()
        self.btnAC_2.raise_()
        self.btnaRoot.raise_()
        self.btnSin.raise_()
        self.btnSinh.raise_()
        self.btnMulti_2.raise_()
        self.btndiv_2.raise_()
        self.btnFact.raise_()
        self.btnCos.raise_()
        self.btnCosh.raise_()
        self.btnAdd_2.raise_()
        self.btnSubtract_2.raise_()
        self.btnPercent_2.raise_()
        self.btnTan.raise_()
        self.btnTanh.raise_()
        self.btnEqual_2.raise_()
        self.tab.addTab(self.tab2, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(mainWindow)
        self.actionHelp.setObjectName("actionHelp")

        self.retranslateUi(mainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btnAdd_1.setText(_translate("MainWindow", "+"))
        self.btnSubtract_1.setText(_translate("MainWindow", "-"))
        self.btnMulti_1.setText(_translate("MainWindow", "×"))
        self.btndiv_1.setText(_translate("MainWindow", "÷"))
        self.btnEqual_1.setText(_translate("MainWindow", "="))
        self.btn7_1.setText(_translate("MainWindow", "7"))
        self.btn8_1.setText(_translate("MainWindow", "8"))
        self.btn9_1.setText(_translate("MainWindow", "9"))
        self.btn4_1.setText(_translate("MainWindow", "4"))
        self.btn5_1.setText(_translate("MainWindow", "5"))
        self.btn6_1.setText(_translate("MainWindow", "6"))
        self.btn1_1.setText(_translate("MainWindow", "1"))
        self.btn2_1.setText(_translate("MainWindow", "2"))
        self.btn3_1.setText(_translate("MainWindow", "3"))
        self.btn00_1.setText(_translate("MainWindow", "00"))
        self.btnDot_1.setText(_translate("MainWindow", "."))
        self.btn0_1.setText(_translate("MainWindow", "0"))
        self.btnLeftBracket_1.setText(_translate("MainWindow", "("))
        self.btnANS_1.setText(_translate("MainWindow", "ANS"))
        self.btnRightBracket_1.setText(_translate("MainWindow", ")"))
        self.btnAC_1.setText(_translate("MainWindow", "AC"))
        self.btnDEL_1.setText(_translate("MainWindow", "DEL"))
        self.btnPercent_1.setText(_translate("MainWindow", "%"))
        self.btnMinPls_1.setText(_translate("MainWindow", "+/-"))
        self.tab.setTabText(self.tab.indexOf(self.tab1), _translate("MainWindow", "Basic Calculator"))
        self.btn8_2.setText(_translate("MainWindow", "8"))
        self.btn6_2.setText(_translate("MainWindow", "6"))
        self.btnPi.setText(_translate("MainWindow", "π"))
        self.btn7_2.setText(_translate("MainWindow", "7"))
        self.btnLeftBracket_2.setText(_translate("MainWindow", "("))
        self.btnRightBracket_2.setText(_translate("MainWindow", ")"))
        self.btn3_2.setText(_translate("MainWindow", "3"))
        self.btnDot_2.setText(_translate("MainWindow", "."))
        self.btn9_2.setText(_translate("MainWindow", "9"))
        self.btn5_2.setText(_translate("MainWindow", "5"))
        self.btn2_2.setText(_translate("MainWindow", "2"))
        self.btn00_2.setText(_translate("MainWindow", "00"))
        self.btn0_2.setText(_translate("MainWindow", "0"))
        self.btn1_2.setText(_translate("MainWindow", "1"))
        self.btn4_2.setText(_translate("MainWindow", "4"))
        self.btnSin.setText(_translate("MainWindow", "Sin"))
        self.btnaRoot.setText(_translate("MainWindow", "√"))
        self.btnLog.setText(_translate("MainWindow", "log"))
        self.btnLn.setText(_translate("MainWindow", "ln"))
        self.btnCosh.setText(_translate("MainWindow", "Cosh"))
        self.btnCos.setText(_translate("MainWindow", "Cos"))
        self.btn_e.setText(_translate("MainWindow", "e"))
        self.btnTanh.setText(_translate("MainWindow", "Tanh"))
        self.btnTan.setText(_translate("MainWindow", "Tan"))
        self.btnEXP.setText(_translate("MainWindow", "EXP"))
        self.btnSinh.setText(_translate("MainWindow", "Sinh"))
        self.btnANS_2.setText(_translate("MainWindow", "ANS"))
        self.btnEqual_2.setText(_translate("MainWindow", "="))
        self.btnAdd_2.setText(_translate("MainWindow", "+"))
        self.btnSubtract_2.setText(_translate("MainWindow", "-"))
        self.btnMulti_2.setText(_translate("MainWindow", "×"))
        self.btndiv_2.setText(_translate("MainWindow", "÷"))
        self.btnDEL_2.setText(_translate("MainWindow", "DEL"))
        self.btnAC_2.setText(_translate("MainWindow", "AC"))
        self.btnPercent_2.setText(_translate("MainWindow", "%"))
        self.btnFact.setText(_translate("MainWindow", "!"))
        self.btnMinPls_2.setText(_translate("MainWindow", "+/-"))
        self.tab.setTabText(self.tab.indexOf(self.tab2), _translate("MainWindow", "Scientific Calculator"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())