# This GUI was created using QT Creator/Designer and was converted to .py using pyuic6
# This form acts as a user interface for Robinhood stock trading code previously developed in python

import robinhood_function as rf
import testing_function as tf
import support_function as sf
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import date


# Builds the form and connects buttons to slots and signals
# ================================================================================================================
# Approached/organized by frame (three total) broken out by buttons, user fields, and labels/lines
# Then connected all buttons to slots/signals
# Then set all initial text values as applicable
# Then defined button functionality
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(34, 40, 49);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # TEXT AT TOP OF FORM
        # =========================================================================
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 721, 21))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(16)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(8, 217, 214);")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 30, 761, 41))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")

        # LOG IN FRAME
        # =========================================================================
        self.frame_login = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_login.setGeometry(QtCore.QRect(20, 90, 351, 141))
        self.frame_login.setStyleSheet("background-color: rgb(82, 89, 100);\n"
                                       "border-color: rgb(0, 173, 181);")
        self.frame_login.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_login.setLineWidth(1)
        self.frame_login.setObjectName("frame_login")

        # LOG IN BUTTONS
        # =========================================================================
        # primary login button
        self.button_login = QtWidgets.QPushButton(parent=self.frame_login)
        self.button_login.setGeometry(QtCore.QRect(250, 70, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.button_login.setFont(font)
        self.button_login.setStyleSheet("color: rgb(8, 217, 214);\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.497475, y1:0.534591, x2:0.497376, y2:0, stop:0 rgba(117, 128, 144, 255), stop:1 rgba(144, 147, 177, 255));")
        self.button_login.setObjectName("button_login")

        # mfa button
        self.button_mfa = QtWidgets.QPushButton(parent=self.frame_login)
        self.button_mfa.setGeometry(QtCore.QRect(250, 100, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.button_mfa.setFont(font)
        self.button_mfa.setStyleSheet("color: rgb(34, 40, 49);")
        self.button_mfa.setObjectName("button_mfa")
        self.button_mfa.setEnabled(False)

        # USER INPUT FIELDS
        # =========================================================================
        # username/email
        self.login_email = QtWidgets.QLineEdit(parent=self.frame_login)
        self.login_email.setGeometry(QtCore.QRect(130, 40, 201, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.login_email.setFont(font)
        self.login_email.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                       "color: rgb(34, 40, 49);")
        self.login_email.setInputMask("")
        self.login_email.setObjectName("login_email")

        # password
        self.login_password = QtWidgets.QLineEdit(parent=self.frame_login)
        self.login_password.setGeometry(QtCore.QRect(130, 70, 113, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.login_password.setFont(font)
        self.login_password.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                          "color: rgb(34, 40, 49);")
        self.login_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.login_password.setObjectName("login_password")

        # mfa
        self.login_mfa = QtWidgets.QLineEdit(parent=self.frame_login)
        self.login_mfa.setEnabled(False)
        self.login_mfa.setGeometry(QtCore.QRect(130, 100, 113, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.login_mfa.setFont(font)
        self.login_mfa.setStyleSheet("background-color: rgb(144, 157, 177);\n"
                                     "color: rgb(34, 40, 49);")
        self.login_mfa.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.login_mfa.setObjectName("login_mfa")

        # LABELS/TEXT
        # =========================================================================
        self.line = QtWidgets.QFrame(parent=self.frame_login)
        self.line.setGeometry(QtCore.QRect(10, 20, 331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.label = QtWidgets.QLabel(parent=self.frame_login)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.frame_login)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.frame_login)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(parent=self.frame_login)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(parent=self.frame_login)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(8, 217, 214);")
        self.label_5.setObjectName("label_5")

        # RAISE - orders items front/back
        # =========================================================================
        self.button_login.raise_()
        self.button_mfa.raise_()
        self.login_email.raise_()
        self.login_password.raise_()
        self.login_mfa.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        # STOCK FRAME
        # =========================================================================
        self.frame_stock = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_stock.setGeometry(QtCore.QRect(20, 250, 351, 171))
        self.frame_stock.setStyleSheet("background-color: rgb(82, 89, 100);\n"
                                       "border-color: rgb(0, 173, 181);")
        self.frame_stock.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_stock.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_stock.setLineWidth(1)
        self.frame_stock.setObjectName("frame_stock")

        # BUTTONS
        # =========================================================================
        # recommend button
        self.button_recommend = QtWidgets.QPushButton(parent=self.frame_stock)
        self.button_recommend.setGeometry(QtCore.QRect(250, 100, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.button_recommend.setFont(font)
        self.button_recommend.setStyleSheet("color: rgb(34, 40, 49);")
        self.button_recommend.setEnabled(False)
        self.button_recommend.setObjectName("button_recommend")

        # test button
        self.button_test = QtWidgets.QPushButton(parent=self.frame_stock)
        self.button_test.setGeometry(QtCore.QRect(250, 40, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.button_test.setFont(font)
        self.button_test.setStyleSheet("color: rgb(34, 40, 49);")
        self.button_test.setEnabled(False)
        self.button_test.setObjectName("button_test")

        # submit button
        self.button_submit = QtWidgets.QPushButton(parent=self.frame_stock)
        self.button_submit.setGeometry(QtCore.QRect(250, 130, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.button_submit.setFont(font)
        self.button_submit.setStyleSheet("color: rgb(34, 40, 49);")
        self.button_submit.setEnabled(False)
        self.button_submit.setObjectName("button_submit")

        # USER INPUTS
        # =========================================================================
        # target stock
        self.stock_target = QtWidgets.QLineEdit(parent=self.frame_stock)
        self.stock_target.setGeometry(QtCore.QRect(130, 40, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.stock_target.setFont(font)
        self.stock_target.setStyleSheet("background-color: rgb(144, 157, 177);\n"
                                        "color: rgb(34, 40, 49);")
        self.stock_target.setObjectName("stock_target")
        self.stock_target.setEnabled(False)

        # spend amount
        self.stock_spend = QtWidgets.QLineEdit(parent=self.frame_stock)
        self.stock_spend.setGeometry(QtCore.QRect(130, 70, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.stock_spend.setFont(font)
        self.stock_spend.setStyleSheet("background-color: rgb(144, 157, 177);\n"
                                       "color: rgb(34, 40, 49);")
        self.stock_spend.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.stock_spend.setObjectName("stock_spend")
        self.stock_target.setEnabled(False)

        # purchase price
        self.stock_buy = QtWidgets.QLineEdit(parent=self.frame_stock)
        self.stock_buy.setEnabled(True)
        self.stock_buy.setGeometry(QtCore.QRect(130, 100, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.stock_buy.setFont(font)
        self.stock_buy.setStyleSheet("background-color: rgb(144, 157, 177);\n"
                                     "color: rgb(34, 40, 49);")
        self.stock_buy.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.stock_buy.setObjectName("stock_buy")
        self.stock_buy.setEnabled(False)

        # sell price
        self.stock_sell = QtWidgets.QLineEdit(parent=self.frame_stock)
        self.stock_sell.setEnabled(True)
        self.stock_sell.setGeometry(QtCore.QRect(130, 130, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.stock_sell.setFont(font)
        self.stock_sell.setStyleSheet("background-color: rgb(144, 157, 177);\n"
                                      "color: rgb(34, 40, 49);")
        self.stock_sell.setText("")
        self.stock_sell.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.stock_sell.setObjectName("stock_sell")
        self.stock_sell.setEnabled(False)

        # LABELS/TEXT/LINES
        # =========================================================================
        self.line_2 = QtWidgets.QFrame(parent=self.frame_stock)
        self.line_2.setGeometry(QtCore.QRect(10, 20, 331, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_6 = QtWidgets.QLabel(parent=self.frame_stock)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(parent=self.frame_stock)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(parent=self.frame_stock)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(parent=self.frame_stock)
        self.label_9.setGeometry(QtCore.QRect(80, 10, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(parent=self.frame_stock)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(8, 217, 214);")
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(parent=self.frame_stock)
        self.label_11.setGeometry(QtCore.QRect(10, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")

        # RAISE - order front/back
        # =========================================================================
        self.button_recommend.raise_()
        self.button_test.raise_()
        self.button_submit.raise_()
        self.stock_target.raise_()
        self.stock_spend.raise_()
        self.stock_buy.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.line_2.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.stock_sell.raise_()
        self.label_11.raise_()

        # OUTPUT FRAME
        # =========================================================================
        self.frame_output = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_output.setGeometry(QtCore.QRect(390, 90, 391, 331))
        self.frame_output.setStyleSheet("background-color: rgb(144, 157, 177);")
        self.frame_output.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_output.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_output.setObjectName("frame_output")

        # SYSTEM OUTPUT TEXT
        # =========================================================================
        self.output_text = QtWidgets.QTextBrowser(parent=self.frame_output)
        self.output_text.setGeometry(QtCore.QRect(15, 40, 361, 281))
        self.output_text.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                       "color: rgb(82, 89, 100);")
        self.output_text.setObjectName("output_text")

        # LABELS/TEXT/LINES
        # =========================================================================
        self.line_3 = QtWidgets.QFrame(parent=self.frame_output)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 371, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")

        self.label_14 = QtWidgets.QLabel(parent=self.frame_output)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(34, 40, 49);")
        self.label_14.setObjectName("label_14")

        # RAISE - order front/back
        # =========================================================================
        self.line_3.raise_()
        self.label_14.raise_()
        self.output_text.raise_()

        # Set general form information
        # =========================================================================
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # BUTTON SLOTS AND SIGNALS
        # =========================================================================
        self.button_login.clicked.connect(self.login)
        self.button_mfa.clicked.connect(self.mfa)
        self.button_submit.clicked.connect(self.submit)
        self.button_test.clicked.connect(self.test)
        self.button_recommend.clicked.connect(self.recommend)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Set initial text values
    # =========================================================================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_login.setText(_translate("MainWindow", "Log in"))
        self.button_mfa.setText(_translate("MainWindow", "Send MFA"))
        self.label.setText(_translate("MainWindow", "Username (email):"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.label_3.setText(_translate("MainWindow", "MFA (if applicable):"))
        self.label_4.setText(_translate("MainWindow", "Log in to Robinhood"))
        self.label_5.setText(_translate("MainWindow", "Step One:"))
        self.button_recommend.setText(_translate("MainWindow", "Recommend"))
        self.button_test.setText(_translate("MainWindow", "Test Stock"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))
        self.label_6.setText(_translate("MainWindow", "Target Stock:"))
        self.label_7.setText(_translate("MainWindow", "Max spend amount:"))
        self.label_8.setText(_translate("MainWindow", "Target Buy Price:"))
        self.label_9.setText(_translate("MainWindow", "Enter Target Stock Information"))
        self.label_10.setText(_translate("MainWindow", "Step Two:"))
        self.label_11.setText(_translate("MainWindow", "Target Sell Price:"))
        self.label_12.setText(_translate("MainWindow", "Robinhood Stock Auto-Trading App"))
        self.label_13.setText(_translate("MainWindow",
                                         "This app allows users to automate trades during the day (9am - 5pm).  The app will buy your target stock (in fractional shares) when it drops below a target purchase price and then sell that stock when it climbs above a target sell price."))
        self.label_14.setText(_translate("MainWindow", "System Message:"))
        self.output_text.setText(
            f'Before you are able to input any stock information, you will need to log in (Step One).  Enter your username and password, and click the Log In button.  If you have multi-factor authentication enabled, you will then be able to enter your MFA code and click the Send MFA button to proceed.')

    # BUTTON CODES
    # ===================================================================================================
    # The log in button will attempt to log in without an MFA.  If an MFA is required, the user will be prompted for
    # it and the MFA box will unlock for entry.
    def login(self):
        email = self.login_email.text()
        pw = self.login_password.text()
        msg = rf.robinhood_login(email, pw)
        self.output_text.setText(msg)
        if msg[:4] == "You ":
            # enable the stock info panel
            self.button_test.setEnabled(True)
            self.button_submit.setEnabled(True)
            self.button_recommend.setEnabled(True)
            self.button_test.setStyleSheet("color: rgb(8, 217, 214);\n"
                                           "background-color: qlineargradient(spread:pad, x1:0.497475, y1:0.534591, x2:0.497376, y2:0, stop:0 rgba(117, 128, 144, 255), stop:1 rgba(144, 147, 177, 255));")
            self.button_submit.setStyleSheet("color: rgb(8, 217, 214);\n"
                                             "background-color: qlineargradient(spread:pad, x1:0.497475, y1:0.534591, x2:0.497376, y2:0, stop:0 rgba(117, 128, 144, 255), stop:1 rgba(144, 147, 177, 255));")
            self.button_recommend.setStyleSheet("color: rgb(8, 217, 214);\n"
                                                "background-color: qlineargradient(spread:pad, x1:0.497475, y1:0.534591, x2:0.497376, y2:0, stop:0 rgba(117, 128, 144, 255), stop:1 rgba(144, 147, 177, 255));")
            self.stock_sell.setEnabled(True)
            self.stock_sell.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                          "color: rgb(34, 40, 49);")
            self.stock_buy.setEnabled(True)
            self.stock_buy.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                         "color: rgb(34, 40, 49);")
            self.stock_spend.setEnabled(True)
            self.stock_spend.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                           "color: rgb(34, 40, 49);")
            self.stock_target.setEnabled(True)
            self.stock_target.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                            "color: rgb(34, 40, 49);")
        if msg[:4] == "Your":
            self.login_mfa.setEnabled(True)
            self.login_mfa.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                         "color: rgb(34, 40, 49);")
            self.button_mfa.setEnabled(True)
            self.button_mfa.setStyleSheet("color: rgb(8, 217, 214);\n"
                                          "background-color: qlineargradient(spread:pad, x1:0.497475, y1:0.534591, x2:0.497376, y2:0, stop:0 rgba(117, 128, 144, 255), stop:1 rgba(144, 147, 177, 255));")

    # The mfa button will log in with the provided MFA.
    def mfa(self):
        email = self.login_email.text()
        pw = self.login_password.text()
        mfa = self.login_mfa.text()
        msg = rf.robinhood_login_mfa(email, pw, mfa)
        self.output_text.setText(msg)
        if msg[:4] == "You ":
            # disable the login info panel
            self.login_mfa.setEnabled(False)
            self.login_email.setEnabled(False)
            self.login_password.setEnabled(False)
            self.login_mfa.setStyleSheet("background-color: rgb(144, 157, 177);\n"
                                         "color: rgb(34, 40, 49);")
            self.login_email.setStyleSheet("background-color: rgb(144, 157, 177);\n"
                                           "color: rgb(34, 40, 49);")
            self.login_password.setStyleSheet("background-color: rgb(144, 157, 177);\n"
                                              "color: rgb(34, 40, 49);")

            # enable the stock info panel
            self.button_test.setEnabled(True)
            self.button_submit.setEnabled(True)
            self.button_recommend.setEnabled(True)
            self.button_test.setStyleSheet("color: rgb(8, 217, 214);\n"
                                           "background-color: qlineargradient(spread:pad, x1:0.497475, y1:0.534591, x2:0.497376, y2:0, stop:0 rgba(117, 128, 144, 255), stop:1 rgba(144, 147, 177, 255));")
            self.button_submit.setStyleSheet("color: rgb(8, 217, 214);\n"
                                             "background-color: qlineargradient(spread:pad, x1:0.497475, y1:0.534591, x2:0.497376, y2:0, stop:0 rgba(117, 128, 144, 255), stop:1 rgba(144, 147, 177, 255));")
            self.button_recommend.setStyleSheet("color: rgb(8, 217, 214);\n"
                                                "background-color: qlineargradient(spread:pad, x1:0.497475, y1:0.534591, x2:0.497376, y2:0, stop:0 rgba(117, 128, 144, 255), stop:1 rgba(144, 147, 177, 255));")
            self.stock_sell.setEnabled(True)
            self.stock_sell.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                          "color: rgb(34, 40, 49);")
            self.stock_buy.setEnabled(True)
            self.stock_buy.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                         "color: rgb(34, 40, 49);")
            self.stock_spend.setEnabled(True)
            self.stock_spend.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                           "color: rgb(34, 40, 49);")
            self.stock_target.setEnabled(True)
            self.stock_target.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                            "color: rgb(34, 40, 49);")

    # Submits a stock and its price information to be bought/sold over the course of the day
    def submit(self):
        target = self.stock_target.text()
        check = tf.check_stock(target)
        self.output_text.setText(check)
        if check[:7] == 'WARNING':
            return
        spend = float(self.stock_spend.text())
        if spend < 1:
            self.output_text.setText('You must trade in at least $1 increments.  Update spend amount and try again.')
            return
        buy = float(self.stock_buy.text())
        sell = float(self.stock_sell.text())
        # TODO - add in live data output
        # TODO - add cancel option
        msg = rf.purchase_by_price(target, spend, buy, sell)
        self.output_text.setText(msg)

    # Tests a stock over the last thirty days to see how well it would have peformed
    def test(self):
        target = self.stock_target.text()
        check = tf.check_stock(target)
        self.output_text.setText(check)
        if check[:7] == 'WARNING':
            return
        spend = float(self.stock_spend.text())
        if spend < 1:
            self.output_text.setText('You must trade in at least $1 increments.  Update spend amount and try again.')
            return
        else:
            self.output_text.setText('This may take a minute to run.  Running now...')
        msg_one = tf.test_x_days(target, 1, spend, 30)
        msg_half = tf.test_x_days(target, .5, spend, 30)
        msg = f'''Analyzed at a standard deviation of 1 for the last 30 days:
{msg_one} 

Analyzed at a standard deviation of .5 for the last 30 days:
{msg_half}

What does this mean? 
At a standard deviation of one, the buy and sell price will be 
further from average.  That means you will trade at target 
prices further from average (trade less often).  When standard 
deviation is .5, you will trade closer to average (trading more 
frequently).  This test code runs over the last 30 days of data
using the standard deviation to determine sell/buy prices for 
the given stock.  It then shows you how much of that stock you
would have bought and sold over that time frame, as well as 
how much stock you will be holding (stock that went unsold) 
so you can determine if the stock is compatible with this 
trading logic.'''
        self.output_text.setText(msg)

    # Recommends stock prices based on a five day historical input and a one day historical input
    def recommend(self):
        target = self.stock_target.text()
        check = tf.check_stock(target)
        self.output_text.setText(check)
        if check[:7] == 'WARNING':
            return
        start = date.today()
        prices_five = sf.recommend_points(target, start, 1, 5)
        prices_five_half = sf.recommend_points(target, start, .5, 5)
        prices_one = sf.recommend_points(target, start, 1, 1)
        prices_one_half = sf.recommend_points(target, start, .5, 1)
        msg = f'''For {target} stock and a five-day historical data pull:
At a standard deviation of 1, buy at {prices_five[0]}, sell at {prices_five[1]}
At a standard deviation of .5, buy at {prices_five_half[0]}, sell at {prices_five_half[1]}

For {target} stock and a one-day historical data pull:
At a standard deviation of 1, buy at {prices_one[0]}, sell at {prices_one[1]}
At a standard deviaiton of .5, buy at {prices_one_half[0]}, sell at {prices_one_half[1]}.

What does this mean? 
The code pulls five days of historical data for stock prices 
at five minute intervals.  It pulls an average price based on 
that data, then determines standard deviation.  At a standard 
deviation of 1, your buy and sell prices will be further away 
from average (focusing on bigger price changes).  When your 
standard deviation is .5, your prices will be closer to your 
average (more trades at lower prices).  The code then repeats 
using only the most recent day's worth of data to give you 
more options and a chance to see how consistent the stock 
has been. '''
        self.output_text.setText(msg)


# Initializes and launches form
# =================================================================================================================
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
