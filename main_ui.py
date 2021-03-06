# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 918)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 867))
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(36, 11, 805, 542))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.RBCustomMode = QtWidgets.QRadioButton(self.layoutWidget)
        self.RBCustomMode.setText("")
        self.RBCustomMode.setChecked(True)
        self.RBCustomMode.setObjectName("RBCustomMode")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.RBCustomMode)
        self.horizontalLayout_8.addWidget(self.RBCustomMode)
        self.VLXInfo = QtWidgets.QVBoxLayout()
        self.VLXInfo.setObjectName("VLXInfo")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.VLXInfo.addWidget(self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.TEBefore = QtWidgets.QLineEdit(self.layoutWidget)
        self.TEBefore.setObjectName("TEBefore")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TEBefore)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.TEAfter = QtWidgets.QLineEdit(self.layoutWidget)
        self.TEAfter.setObjectName("TEAfter")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TEAfter)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.TEHeight = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TEHeight.sizePolicy().hasHeightForWidth())
        self.TEHeight.setSizePolicy(sizePolicy)
        self.TEHeight.setObjectName("TEHeight")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.TEHeight)
        self.VLXInfo.addLayout(self.formLayout)
        self.horizontalLayout_8.addLayout(self.VLXInfo)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.VLFunctions = QtWidgets.QVBoxLayout()
        self.VLFunctions.setObjectName("VLFunctions")
        self.RBSin = QtWidgets.QRadioButton(self.layoutWidget)
        self.RBSin.setChecked(True)
        self.RBSin.setObjectName("RBSin")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.RBSin)
        self.VLFunctions.addWidget(self.RBSin)
        self.RBCos = QtWidgets.QRadioButton(self.layoutWidget)
        self.RBCos.setObjectName("RBCos")
        self.buttonGroup.addButton(self.RBCos)
        self.VLFunctions.addWidget(self.RBCos)
        self.RBExp = QtWidgets.QRadioButton(self.layoutWidget)
        self.RBExp.setObjectName("RBExp")
        self.buttonGroup.addButton(self.RBExp)
        self.VLFunctions.addWidget(self.RBExp)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.VLFunctions.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.RBCustom = QtWidgets.QRadioButton(self.layoutWidget)
        self.RBCustom.setText("")
        self.RBCustom.setObjectName("RBCustom")
        self.buttonGroup.addButton(self.RBCustom)
        self.horizontalLayout_5.addWidget(self.RBCustom)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.TEFunc = QtWidgets.QLineEdit(self.layoutWidget)
        self.TEFunc.setEnabled(False)
        self.TEFunc.setClearButtonEnabled(False)
        self.TEFunc.setObjectName("TEFunc")
        self.horizontalLayout_5.addWidget(self.TEFunc)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.VLFunctions.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9.addLayout(self.VLFunctions)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.RBChoseFileMode = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RBChoseFileMode.sizePolicy().hasHeightForWidth())
        self.RBChoseFileMode.setSizePolicy(sizePolicy)
        self.RBChoseFileMode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RBChoseFileMode.setAutoFillBackground(False)
        self.RBChoseFileMode.setText("")
        self.RBChoseFileMode.setObjectName("RBChoseFileMode")
        self.buttonGroup_2.addButton(self.RBChoseFileMode)
        self.horizontalLayout_6.addWidget(self.RBChoseFileMode)
        self.TEFileName = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TEFileName.sizePolicy().hasHeightForWidth())
        self.TEFileName.setSizePolicy(sizePolicy)
        self.TEFileName.setObjectName("TEFileName")
        self.horizontalLayout_6.addWidget(self.TEFileName)
        self.BtnChooseFile = QtWidgets.QPushButton(self.layoutWidget)
        self.BtnChooseFile.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnChooseFile.sizePolicy().hasHeightForWidth())
        self.BtnChooseFile.setSizePolicy(sizePolicy)
        self.BtnChooseFile.setObjectName("BtnChooseFile")
        self.horizontalLayout_6.addWidget(self.BtnChooseFile)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BtnCreate = QtWidgets.QPushButton(self.layoutWidget)
        self.BtnCreate.setObjectName("BtnCreate")
        self.verticalLayout_2.addWidget(self.BtnCreate)
        self.BtnSpline = QtWidgets.QPushButton(self.layoutWidget)
        self.BtnSpline.setObjectName("BtnSpline")
        self.verticalLayout_2.addWidget(self.BtnSpline)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????????????? ????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????? ??"))
        self.label_3.setText(_translate("MainWindow", "????:"))
        self.label_4.setText(_translate("MainWindow", "????:"))
        self.label_5.setText(_translate("MainWindow", "???????????????????? \n"
" ??????????:"))
        self.RBSin.setText(_translate("MainWindow", "f(x) = sin(x)"))
        self.RBCos.setText(_translate("MainWindow", "f(x) = cos(x)"))
        self.RBExp.setText(_translate("MainWindow", "f(x) = e^(x^2)"))
        self.label.setText(_translate("MainWindow", "y = f(x)"))
        self.label_6.setText(_translate("MainWindow", "y = "))
        self.TEFileName.setText(_translate("MainWindow", "?????? ??????????"))
        self.BtnChooseFile.setText(_translate("MainWindow", "??????????????"))
        self.BtnCreate.setText(_translate("MainWindow", "???????????????????????? ?????????? ??????????????????"))
        self.BtnSpline.setText(_translate("MainWindow", "???????????????????????? ????????????????"))
        self.label_7.setText(_translate("MainWindow", "???????????????????? ?????? ?????????????????????????? ?????????? ??????????????:"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline;\">?????????????????????? ????????????????:</span></p><p>????????????????: <span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">+</span></p><p>??????????????????: <span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">-</span></p><p>??????????????????: <span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">*</span></p><p>??????????????: <span style=\" color:#ff0000;\">/</span></p><p>?????????????? ???? ??????????????: <span style=\" color:#ff0000;\">%</span></p><p>???????????????????? ?? ??????????????:<span style=\" color:#ff0000;\"> **</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "??????????????: \n"
"sin(x),cos(x),tan(x) - ???????????????????????????????????? ??????????, ?????????????? ?????? ??????????????.\n"
"arcsin(x),arccos(x),arctan(x) - ???????????????????????????????????? ???????????????? ??????????, ?????????????? ?????? ??????????????.\n"
"arctan2(x1, x2) - ???????????????????????????????????? ???????????????? ??????????????.\n"
"sinh(x),cosh(x),tanh(x) - ?????????????????????????????? ??????????, ?????????????? ?????? ??????????????.\n"
"arcsinh(x),arccosh(x),arctanh(x) - ?????????????????????????????? ???????????????? ??????????, ?????????????? ?????? ??????????????.\n"
"log(x),log10(x),log1p(x) - ??????????????????????, ??????????????-10 ?? ??????????????????????????????(1+x) ??????????????????.\n"
"exp(x),expm1(x) - ???????????????????????????????? ?? ???????????????????????????????? ?????????? ????????.\n"
"sqrt(x) - ???????????????????? ????????????.\n"
"abs(x) - ???????????????????? ????????????????."))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline;\">?????????????? ?????? ???????????? ???????????? ?? ??????????:</span></p><p>???????????? ???????????? ???????? ???????????????? ?? ?????? ????????????:</p><p>    1 ???????????? ???????????????????? ?? ?????????????? ?????????????? x/X, ?????????? ???????????????? ??????????????</p><p>    2 ???????????? ???????????????????? ?? ?????????????? ?????????????? y/Y, ?????????? ???????????????? ??????????????</p></body></html>"))
