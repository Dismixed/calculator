from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
import sys
from PyQt5.QtWidgets import QTextEdit
import re
import math
from decimal import Decimal


def addprint(printed):
    if printed == "√":
        # square root parentheses
        text.setText(text.toPlainText() + str(printed) + "(")
    else:
        text.setText(text.toPlainText() + str(printed))


def backspace():
    newtext = text.toPlainText()
    finaltext = ""
    for i in range(len(newtext)):
        if i == len(newtext) - 1:
            break
        finaltext = finaltext + newtext[i]
    text.setText(finaltext)


def clear():
    text.clear()


def printans(ans):
    if ans == "Undefined":
        text.append(ans)
    else:
        text.append(str(ans[0]))
    text.append("")


def pieval(func):
    while "π" in func:
        for i in range(len(func)):
            if func[i] == "π":
                func[i] = math.pi
    return func


# reverse to find first occurance of \n to seperate the calculation
def reverselist(newsplits):
    newsplits.reverse()
    indx2 = 0
    for i in newsplits:
        indx2 = indx2 + 1
        if i == "\n":
            del newsplits[indx2 - 1:]
            newsplits.reverse()
            return newsplits


# removing blank strings
def blankremove(newsplits):
    while "" in newsplits:
        newsplits.remove("")
    while " " in newsplits:
        newsplits.remove(" ")
    return newsplits


#secondary eval(For parentheses)
def evaluate(eval, secondary):
    # splitting equation, splits at all non alphanumeric, keeps ".", keeps the delimiter
    splits = re.split('([^a-zA-Z0-9.])', eval)


    tempsplits = []

    splits = blankremove(splits)
    splits = pieval(splits)
    if "\n" in splits:
        splits = reverselist(splits)

    # solving loop
    while len(splits) > 1:
        # floats instead of ints
        if "(" in splits:
            for i in range(len(splits)):
                if splits[i] == "(":
                    if splits[i - 1] == "√":
                        pass
                    else:
                        indexed1 = i
                        indexed2 = 0
                        for y in range(len(splits[i:])):
                            indexed2 = indexed2 + 1
                            if splits[y] == ")":
                                break
                        mainstr = ""
                        for x in range(len(splits[indexed1:indexed2])):
                            mainstr = mainstr + str(splits[x])
                        mainstr = mainstr.replace("(", "")
                        mainstr = mainstr.replace(")", "")

                        del splits[indexed1:indexed2]
                        splits.insert(indexed1, evaluate(mainstr, False))
                        print(splits)
                        break
                    
        if "²" in splits:
            indx = 0
            for i in splits:
                indx = indx + 1
                if i == "²":
                    # -2 because it's 1 behind the squared symbol and an extra for accounting for starting indx at 1
                    temp = float(splits[indx - 2]) * float(splits[indx - 2])
                    del splits[indx - 1]
                    del splits[indx - 2]
                    splits.insert(indx - 2, str(temp))


        if "√" in splits:
            for i in range(len(splits)):
                if splits[i] == "(":
                    indx1 = i
                    indx2 = 0
                    for y in range(len(splits)):
                        if splits[y] == ")":
                            indx2 = y
                            temp = evaluate()

        if "*" in splits:
            indx = 0
            for y in splits:
                indx = indx + 1
                if y == "*":
                    temp = float(splits[indx - 2]) * float(splits[indx])
                    del splits[indx]
                    del splits[indx - 1]
                    del splits[indx - 2]
                    splits.insert(indx - 2, str(temp))

        if "÷" in splits:
            indx = 0
            for y in splits:
                indx = indx + 1
                if y == "÷":
                    # Divide by zero error
                    if splits[indx] == "0":
                        splits.clear()
                        splits.append("Undefined")
                        break
                    temp = float(splits[indx - 2]) / float(splits[indx])
                    del splits[indx]
                    del splits[indx - 1]
                    del splits[indx - 2]
                    splits.insert(indx - 2, str(temp))

        if "+" in splits:
            indx = 0
            for y in splits:
                indx = indx + 1
                if y == "+":
                    temp = float(splits[indx - 2]) + float(splits[indx])
                    del splits[indx]
                    del splits[indx - 1]
                    del splits[indx - 2]
                    splits.insert(indx - 2, str(temp))

        if "-" in splits:
            indx = 0
            for y in splits:
                indx = indx + 1
                if y == "-":
                    temp = float(splits[indx - 2]) - float(splits[indx])
                    del splits[indx]
                    del splits[indx - 1]
                    del splits[indx - 2]
                    splits.insert(indx - 2, str(temp))

        print(splits)


    #secondary eval (for paretheses)
    if secondary:
        printans(splits)
        splits.clear()
    else:
        return float(splits[0])



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Calculator")
layout = QGridLayout()
text = QTextEdit()

# buttons
num1 = QPushButton("1")
num2 = QPushButton("2")
num3 = QPushButton("3")
num4 = QPushButton("4")
num5 = QPushButton("5")
num6 = QPushButton("6")
num7 = QPushButton("7")
num8 = QPushButton("8")
num9 = QPushButton("9")
num0 = QPushButton("0")
dot = QPushButton(".")
equals = QPushButton("=")
plus = QPushButton("+")
minus = QPushButton("-")
times = QPushButton("x")
divided = QPushButton("÷")
plusnegative = QPushButton("+/-")
percent = QPushButton("%")
bkspce = QPushButton("⌫")
clr = QPushButton("CLR")
sqrt = QPushButton("√")
squared = QPushButton("x²")
pi = QPushButton("π")
lparentheses = QPushButton("(")
rparentheses = QPushButton(")")

# stylesheets
equals.setStyleSheet("color: white; background-color: blue")

num1.setStyleSheet("background-color: #F8F8FF")
num2.setStyleSheet("background-color: #F8F8FF")
num3.setStyleSheet("background-color: #F8F8FF")
num4.setStyleSheet("background-color: #F8F8FF")
num5.setStyleSheet("background-color: #F8F8FF")
num6.setStyleSheet("background-color: #F8F8FF")
num7.setStyleSheet("background-color: #F8F8FF")
num8.setStyleSheet("background-color: #F8F8FF")
num9.setStyleSheet("background-color: #F8F8FF")
num0.setStyleSheet("background-color: #F8F8FF")

# widgets
layout.addWidget(text, 0, 0, 1, 5)

layout.addWidget(dot, 5, 2)
layout.addWidget(equals, 5, 3)
layout.addWidget(plus, 5, 4)
layout.addWidget(minus, 4, 4)
layout.addWidget(times, 3, 4)
layout.addWidget(divided, 2, 4)
layout.addWidget(plusnegative, 1, 1)
layout.addWidget(percent, 1, 2)
layout.addWidget(clr, 1, 3)
layout.addWidget(bkspce, 1, 4)
layout.addWidget(pi, 5, 0)
layout.addWidget(sqrt, 1, 0)
layout.addWidget(squared, 2, 0)
layout.addWidget(lparentheses, 3, 0)
layout.addWidget(rparentheses, 4, 0)

layout.addWidget(num0, 5, 1)
layout.addWidget(num1, 4, 1)
layout.addWidget(num2, 4, 2)
layout.addWidget(num3, 4, 3)
layout.addWidget(num4, 3, 1)
layout.addWidget(num5, 3, 2)
layout.addWidget(num6, 3, 3)
layout.addWidget(num7, 2, 1)
layout.addWidget(num8, 2, 2)
layout.addWidget(num9, 2, 3)

# clicked function
num1.clicked.connect(lambda: addprint(1))
num2.clicked.connect(lambda: addprint(2))
num3.clicked.connect(lambda: addprint(3))
num4.clicked.connect(lambda: addprint(4))
num5.clicked.connect(lambda: addprint(5))
num6.clicked.connect(lambda: addprint(6))
num7.clicked.connect(lambda: addprint(7))
num8.clicked.connect(lambda: addprint(8))
num9.clicked.connect(lambda: addprint(9))
num0.clicked.connect(lambda: addprint(0))

plus.clicked.connect(lambda: addprint("+"))
minus.clicked.connect(lambda: addprint("-"))
divided.clicked.connect(lambda: addprint("÷"))
times.clicked.connect(lambda: addprint("*"))
bkspce.clicked.connect(lambda: backspace())
clr.clicked.connect(lambda: clear())
equals.clicked.connect(lambda: evaluate(text.toPlainText(), True))
squared.clicked.connect(lambda: addprint("²"))
pi.clicked.connect(lambda: addprint("π"))
rparentheses.clicked.connect(lambda: addprint(")"))
lparentheses.clicked.connect(lambda: addprint("("))
sqrt.clicked.connect(lambda: addprint("√"))
dot.clicked.connect(lambda: addprint("."))

window.setLayout(layout)
window.show()
sys.exit(app.exec())
