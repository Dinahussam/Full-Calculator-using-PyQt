# imports
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calculator import Ui_MainWindow
import numpy as np
import math
from numpy import log as ln

# initialization
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# ---------------------------------------Basic Calculator ---------------------------------------

# Logic of Basic Calculator
answer = 0
check = True
percent_var = False


def zero():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×0")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "0")
    if not check:
        ui.lineEditScreen.setText("0")
    check = True


def one():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×1")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "1")
    if not check:
        ui.lineEditScreen.setText("1")
    check = True


def two():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×2")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "2")
    if not check:
        ui.lineEditScreen.setText("2")
    check = True


def three():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×3")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "3")
    if not check:
        ui.lineEditScreen.setText("3")
    check = True


def four():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×4")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "4")
    if not check:
        ui.lineEditScreen.setText("4")
    check = True


def five():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×5")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "5")
    if not check:
        ui.lineEditScreen.setText("5")
    check = True


def six():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×6")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "6")
    if not check:
        ui.lineEditScreen.setText("6")
    check = True


def seven():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×7")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "7")
    if not check:
        ui.lineEditScreen.setText("7")
    check = True


def eight():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×8")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "8")
    if not check:
        ui.lineEditScreen.setText("8")
    check = True


def nine():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×9")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "9")
    if not check:
        ui.lineEditScreen.setText("9")
    check = True


def dot():  # here we should modify this function don't forget please dino ok dino.....................................
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if percent_var == True and screen_items[-1] == "%":
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×.")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + ".")
    if not check:
        ui.lineEditScreen.setText(".")
    check = True


def double_zero():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×00")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "00")
    if not check:
        ui.lineEditScreen.setText("00")
    check = True


def left_bracket():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×(")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "(")
    if not check:
        ui.lineEditScreen.setText("6")
    check = True


def right_bracket():
    global check
    global percent_var
    if check:
        screen = ui.lineEditScreen.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×)")
        else:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + ")")
    if not check:
        ui.lineEditScreen.setText("6")
    check = True


def add():
    global check
    ui.lineEditScreen.setText(ui.lineEditScreen.text() + "+")
    check = True


def subtract():
    global check
    ui.lineEditScreen.setText(ui.lineEditScreen.text() + "-")
    check = True


def multiply():
    global check
    ui.lineEditScreen.setText(ui.lineEditScreen.text() + "×")
    check = True


def div():
    global check
    ui.lineEditScreen.setText(ui.lineEditScreen.text() + "÷")
    check = True


def min_pls():
    try:
        screen = ui.lineEditScreen.text()
        screen_list = []
        for i in screen:
            screen_list.append(i)
        if screen_list[0] != "-":
            ui.lineEditScreen.setText("-" + ui.lineEditScreen.text())
        else:
            num = ""
            screen_list.remove(screen_list[0])
            for j in screen_list:
                num += j
            ui.lineEditScreen.setText(num)
    except:
        ui.lineEditScreen.setText("")


def percent():
    global check
    global percent_var
    ui.lineEditScreen.setText(ui.lineEditScreen.text() + "%")
    check = True
    percent_var = True


def clear_ac():
    global percent_var
    percent_var = False
    ui.lineEditScreen.setText("")


def delete():
    ui.lineEditScreen.setText(ui.lineEditScreen.text()[0:-1])


def ans():
    global check
    if check:
        try:
            ui.lineEditScreen.setText(ui.lineEditScreen.text() + answer)
        except:
            ui.lineEditScreen.setText("")

    if not check:
        ui.lineEditScreen.setText(answer)
    check = True


def equal():
    count1 = 0
    count2 = 0
    global answer
    global check
    global percent_var
    percent_var = False
    try:
        equation = ui.lineEditScreen.text()
        x1 = equation.split("×")  # First process to transform from × to *
        k1 = ""
        for i in range(0, len(x1) - 1, 1):
            k1 = k1 + x1[i] + "*"
        k1 = k1 + x1[-1]

        x2 = k1.split("÷")  # Second process to transform from ÷ to /
        k2 = ""
        for j in range(0, len(x2) - 1, 1):
            k2 = k2 + x2[j] + "/"
        k2 = k2 + x2[-1]

        x3 = k2.split("%")  # Third process to transform from % to /100
        k3 = ""
        for z in range(0, len(x3) - 1, 1):
            k3 = k3 + x3[z] + "/100"
        k3 = k3 + x3[-1]

        result = str(eval(k3))
        for i in result:
            if i == ".":
                d = result.split(".")
                v = d[1]
                for j in v:
                    count2 += 1
                    if j == "0":
                        if count2 == (len(result) - count1 - 1):
                            s = result.split(".")
                            collect = s[0]
                            answer = collect
                            ui.lineEditScreen.setText(collect)
                        else:
                            continue
                    else:
                        answer = result
                        ui.lineEditScreen.setText(result)
                        break
            else:
                d = result.split(".")
                if len(d[0]) == len(result):
                    answer = result
                    ui.lineEditScreen.setText(result)
                else:
                    count1 += 1
        check = False
    except ZeroDivisionError:
        ui.lineEditScreen.setText(" Cannot divide by zero")
        check = False
    except SyntaxError:
        ui.lineEditScreen.setText(" Invalid operation")
        check = False
    except:
        ui.lineEditScreen.setText(" Error")


# Connection Of Basic Calculator
ui.btn0_1.clicked.connect(zero)
ui.btn1_1.clicked.connect(one)
ui.btn2_1.clicked.connect(two)
ui.btn3_1.clicked.connect(three)
ui.btn4_1.clicked.connect(four)
ui.btn5_1.clicked.connect(five)
ui.btn6_1.clicked.connect(six)
ui.btn7_1.clicked.connect(seven)
ui.btn8_1.clicked.connect(eight)
ui.btn9_1.clicked.connect(nine)
ui.btnDot_1.clicked.connect(dot)
ui.btn00_1.clicked.connect(double_zero)
ui.btnLeftBracket_1.clicked.connect(left_bracket)
ui.btnRightBracket_1.clicked.connect(right_bracket)
ui.btnAdd_1.clicked.connect(add)
ui.btnSubtract_1.clicked.connect(subtract)
ui.btnMulti_1.clicked.connect(multiply)
ui.btndiv_1.clicked.connect(div)
ui.btnMinPls_1.clicked.connect(min_pls)
ui.btnPercent_1.clicked.connect(percent)
ui.btnAC_1.clicked.connect(clear_ac)
ui.btnDEL_1.clicked.connect(delete)
ui.btnEqual_1.clicked.connect(equal)
ui.btnANS_1.clicked.connect(ans)

# ---------------------------------------- Scientific Calculator ----------------------------------------------

# Logic of Basic Calculator
answer2 = 0
check2 = True
percent_var2 = False
right_bracket = False  # This variable for log function.


def zero2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×0")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "0")
    if not check2:
        ui.lineEditScreen2.setText("0")
    check2 = True


def one2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×1")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "1")
    if not check2:
        ui.lineEditScreen2.setText("1")
    check2 = True


def two2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×2")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "2")
    if not check2:
        ui.lineEditScreen2.setText("2")
    check2 = True


def three2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×3")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "3")
    if not check2:
        ui.lineEditScreen2.setText("3")
    check2 = True


def four2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×4")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "4")
    if not check2:
        ui.lineEditScreen2.setText("4")
    check2 = True


def five2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×5")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "5")
    if not check2:
        ui.lineEditScreen2.setText("5")
    check2 = True


def six2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×6")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "6")
    if not check2:
        ui.lineEditScreen2.setText("6")
    check2 = True


def seven2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×7")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "7")
    if not check2:
        ui.lineEditScreen2.setText("7")
    check2 = True


def eight2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×8")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "8")
    if not check2:
        ui.lineEditScreen2.setText("8")
    check2 = True


def nine2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×9")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "9")
    if not check2:
        ui.lineEditScreen2.setText("9")
    check2 = True


def pi():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×π")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "π")
        if not check2:
            ui.lineEditScreen2.setText("π")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def e():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×e")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "e")
        if not check2:
            ui.lineEditScreen2.setText("e")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def dot2():  # here we should modify this function don't forget please dino ok dino.....................................
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×.")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + ".")
    if not check2:
        ui.lineEditScreen2.setText(".")
    check2 = True


def double_zero2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×00")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "00")
    if not check2:
        ui.lineEditScreen2.setText("00")
    check2 = True


def left_bracket2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×(")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "(")
    if not check2:
        ui.lineEditScreen2.setText("6")
    check2 = True


def right_bracket2():
    global check2
    global percent_var2
    if check2:
        screen = ui.lineEditScreen2.text()
        screen_items = []
        for i in screen:
            screen_items.append(i)
        if (percent_var2 == True) and (screen_items[-1] == "%"):
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×)")
        else:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + ")")
    if not check2:
        ui.lineEditScreen2.setText(")")
    check2 = True


def add2():
    global check2
    ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "+")
    check2 = True


def subtract2():
    global check2
    ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "-")
    check2 = True


def multiply2():
    global check2
    ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×")
    check2 = True


def div2():
    global check2
    ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "÷")
    check2 = True


def min_pls2():
    try:
        screen = ui.lineEditScreen2.text()
        screen_list = []
        for i in screen:
            screen_list.append(i)
        if screen_list[0] != "-":
            ui.lineEditScreen2.setText("-" + ui.lineEditScreen2.text())
        else:
            num = ""
            screen_list.remove(screen_list[0])
            for j in screen_list:
                num += j
            ui.lineEditScreen2.setText(num)
    except:
        ui.lineEditScreen2.setText("")


def percent2():
    global check2
    global percent_var2
    ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "%")
    check2 = True
    percent_var2 = True


def root():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×√(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "√(")
        if not check2:
            ui.lineEditScreen2.setText("√(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def fact():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×!(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "!(")
        if not check2:
            ui.lineEditScreen2.setText("!(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def exp():
    global check2
    global percent_var2
    try:
        if check2:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "EXP(")
        if not check2:
            ui.lineEditScreen2.setText("EXP(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def ln():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×ln(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "ln(")
        if not check2:
            ui.lineEditScreen2.setText("ln(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def log():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×log(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "log(")
        if not check2:
            ui.lineEditScreen2.setText("log(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def sin():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×sin(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "sin(")
        if not check2:
            ui.lineEditScreen2.setText("sin(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def cos():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×cos(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "cos(")
        if not check2:
            ui.lineEditScreen2.setText("cos(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def tan():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×tan(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "tan(")
        if not check2:
            ui.lineEditScreen2.setText("tan(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def sinh():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×sinh(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "sinh(")
        if not check2:
            ui.lineEditScreen2.setText("sinh(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def cosh():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×cosh(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "cosh(")
        if not check2:
            ui.lineEditScreen2.setText("cosh(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def tanh():
    global check2
    global percent_var2
    try:
        if check2:
            screen = ui.lineEditScreen2.text()
            items = []  # Items of screen
            for i in screen:
                items.append(i)
            if len(items) >= 1 and items[-1] != "×" and items[-1] != "+" and items[-1] != "-" and items[-1] != "÷":
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "×tanh(")
            else:
                ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + "tanh(")
        if not check2:
            ui.lineEditScreen2.setText("tanh(")
        check2 = True
        percent_var2 = True
    except:
        ui.lineEditScreen2.setText("")


def clear_ac2():
    global percent_var2
    percent_var2 = False
    ui.lineEditScreen2.setText("")


def delete2():
    ui.lineEditScreen2.setText(ui.lineEditScreen2.text()[0:-1])


def ans2():
    global check2
    if check2:
        try:
            ui.lineEditScreen2.setText(ui.lineEditScreen2.text() + answer2)
        except:
            ui.lineEditScreen2.setText("")

    if not check2:
        ui.lineEditScreen2.setText(answer2)
    check2 = True


def equal2():
    count1 = 0
    count2 = 0
    global answer2
    global check2
    global percent_var2
    percent_var2 = False
    try:
        equation = ui.lineEditScreen2.text()
        x1 = equation.split("×")  # First process to transform from × to *
        k1 = ""
        for i in range(0, len(x1) - 1, 1):
            k1 = k1 + x1[i] + "*"
        k1 = k1 + x1[-1]

        x2 = k1.split("÷")  # Second process to transform from ÷ to /
        k2 = ""
        for j in range(0, len(x2) - 1, 1):
            k2 = k2 + x2[j] + "/"
        k2 = k2 + x2[-1]

        x3 = k2.split("%")  # Third process to transform from % to /100
        k3 = ""
        for z in range(0, len(x3) - 1, 1):
            k3 = k3 + x3[z] + "/100"
        k3 = k3 + x3[-1]

        x4 = k3.split("π")  # Fourth process to transform from π to 3.141592653589793
        k4 = ""
        for h in range(0, len(x4) - 1, 1):
            k4 = k4 + x4[h] + "3.141592653589793"
        k4 = k4 + x4[-1]

        x5 = k4.split("e")  # Fifth process to transform from e to 2.718281828459045
        k5 = ""
        for v in range(0, len(x5) - 1, 1):
            k5 = k5 + x5[v] + "2.718281828459045"
        k5 = k5 + x5[-1]

        x6 = k5.split("√")  # sixth process to transform from √ to math.sqrt
        k6 = ""
        for c in range(0, len(x6) - 1, 1):
            k6 = k6 + x6[c] + "np.sqrt"
        k6 = k6 + x6[-1]

        x7 = k6.split("sin(")  # seventh process to transform from sin( to np.sin(np.pi/180*
        k7 = ""
        for c in range(0, len(x7) - 1, 1):
            k7 = k7 + x7[c] + "np.sin(np.pi/180*"
        k7 = k7 + x7[-1]

        x8 = k7.split("cos")  # eighth process to transform from cos to np.cos
        k8 = ""
        for c in range(0, len(x8) - 1, 1):
            k8 = k8 + x8[c] + "np.cos"
        k8 = k8 + x8[-1]

        x9 = k8.split("tan")  # ninth process to transform from tan to np.tan
        k9 = ""
        for c in range(0, len(x9) - 1, 1):
            k9 = k9 + x9[c] + "np.tan"
        k9 = k9 + x9[-1]

        x10 = k9.split("sinh")  # 10th process to transform from sinh to np.sinh
        k10 = ""
        for c in range(0, len(x10) - 1, 1):
            k10 = k10 + x10[c] + "np.sinh"
        k10 = k10 + x10[-1]

        x11 = k10.split("cosh")  # 11th process to transform from cosh to np.cosh
        k11 = ""
        for c in range(0, len(x11) - 1, 1):
            k11 = k11 + x11[c] + "np.cosh"
        k11 = k11 + x11[-1]

        x12 = k11.split("EXP")  # 12th process to transform from EXP to **
        k12 = ""
        for c in range(0, len(x12) - 1, 1):
            k12 = k12 + x12[c] + "**"
        k12 = k12 + x12[-1]

        x13 = k12.split("log")  # 13th process to transform from log to np.log(number, 10)
        k13 = ""
        for c in range(0, len(x13) - 1, 1):
            k13 = k13 + x13[c] + "math.log"
        k13 = k13 + x13[-1]

        screen_items = []
        count = 0
        for i in k13:
            screen_items.append(i)
        for j in screen_items:  # log(5, 10) --> log(5)
            if j == "m":
                count += 1
                for x in range(count, len(screen_items) + 1, 1):
                    if screen_items[x - 1] == ")":
                        count += 1
                        screen_items[x - 1] = ", 10)"
                    else:
                        count += 1
            else:
                count += 1

        k14 = ""
        for h in screen_items:
            k14 = k14 + h

        x15 = k14.split("ln")  # 14th process to transform from ln to np.log --> ln in math
        k15 = ""
        for c in range(0, len(x15) - 1, 1):
            k15 = k15 + x15[c] + "np.log"
        k15 = k15 + x15[-1]

        x16 = k15.split("!")  # 15th process to transform from ! to math.factorial
        k16 = ""
        for c in range(0, len(x16) - 1, 1):
            k16 = k16 + x16[c] + "math.factorial"
        k16 = k16 + x16[-1]

        x17 = k16.split("tanh")  # 16 process to transform from tanh to np.tanh
        k17 = ""
        for c in range(0, len(x17) - 1, 1):
            k17 = k17 + x17[c] + "np.tanh"
        k17 = k17 + x17[-1]

        result = str(eval(k17))
        for i in result:
            if i == ".":
                d = result.split(".")
                v = d[1]
                for j in v:
                    count2 += 1
                    if j == "0":
                        if count2 == (len(result) - count1 - 1):
                            s = result.split(".")
                            collect = s[0]
                            answer2 = collect
                            ui.lineEditScreen2.setText(collect)
                        else:
                            continue
                    else:
                        answer2 = result
                        ui.lineEditScreen2.setText(result)
                        break
            else:
                d = result.split(".")
                if len(d[0]) == len(result):
                    answer2 = result
                    ui.lineEditScreen2.setText(result)
                else:
                    count1 += 1
        check2 = False
    except ZeroDivisionError:
        ui.lineEditScreen2.setText(" Cannot divide by zero")
        check2 = False
    except SyntaxError:
        ui.lineEditScreen2.setText(" Invalid operation")
        check2 = False
    except:
        ui.lineEditScreen2.setText(" Error")


# Connection Of Scientific Calculator
ui.btn0_2.clicked.connect(zero2)
ui.btn1_2.clicked.connect(one2)
ui.btn2_2.clicked.connect(two2)
ui.btn3_2.clicked.connect(three2)
ui.btn4_2.clicked.connect(four2)
ui.btn5_2.clicked.connect(five2)
ui.btn6_2.clicked.connect(six2)
ui.btn7_2.clicked.connect(seven2)
ui.btn8_2.clicked.connect(eight2)
ui.btn9_2.clicked.connect(nine2)
ui.btnPi.clicked.connect(pi)
ui.btn_e.clicked.connect(e)
ui.btnDot_2.clicked.connect(dot2)
ui.btn00_2.clicked.connect(double_zero2)
ui.btnLeftBracket_2.clicked.connect(left_bracket2)
ui.btnRightBracket_2.clicked.connect(right_bracket2)
ui.btnAdd_2.clicked.connect(add2)
ui.btnSubtract_2.clicked.connect(subtract2)
ui.btnMulti_2.clicked.connect(multiply2)
ui.btndiv_2.clicked.connect(div2)
ui.btnMinPls_2.clicked.connect(min_pls2)
ui.btnPercent_2.clicked.connect(percent2)
ui.btnaRoot.clicked.connect(root)
ui.btnFact.clicked.connect(fact)
ui.btnEXP.clicked.connect(exp)
ui.btnLn.clicked.connect(ln)
ui.btnLog.clicked.connect(log)
ui.btnSin.clicked.connect(sin)
ui.btnCos.clicked.connect(cos)
ui.btnTan.clicked.connect(tan)
ui.btnSinh.clicked.connect(sinh)
ui.btnCosh.clicked.connect(cosh)
ui.btnTanh.clicked.connect(tanh)
ui.btnAC_2.clicked.connect(clear_ac2)
ui.btnDEL_2.clicked.connect(delete2)
ui.btnEqual_2.clicked.connect(equal2)
ui.btnANS_2.clicked.connect(ans2)

sys.exit(app.exec_())