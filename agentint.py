# Form implementation generated from reading ui file 'agentint.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 684)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(590, 30, 251, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sizeLadel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.sizeLadel.setObjectName("sizeLadel")
        self.verticalLayout.addWidget(self.sizeLadel)
        self.sizeSpinBox = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.sizeSpinBox.setMinimum(10)
        self.sizeSpinBox.setMaximum(25)
        self.sizeSpinBox.setObjectName("sizeSpinBox")
        self.verticalLayout.addWidget(self.sizeSpinBox)
        self.boxesLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.boxesLabel.setObjectName("boxesLabel")
        self.verticalLayout.addWidget(self.boxesLabel)
        self.goalLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.goalLabel.setObjectName("goalLabel")
        self.verticalLayout.addWidget(self.goalLabel)
        self.scoreLabel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.scoreLabel.setObjectName("scoreLabel")
        self.verticalLayout.addWidget(self.scoreLabel)
        self.restartButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.restartButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.restartButton.setObjectName("restartButton")
        self.verticalLayout.addWidget(self.restartButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agent 007"))
        self.sizeLadel.setText(_translate("MainWindow", "Size:"))
        self.boxesLabel.setText(_translate("MainWindow", "Boxes:"))
        self.goalLabel.setText(_translate("MainWindow", "Goal:"))
        self.scoreLabel.setText(_translate("MainWindow", "Score:"))
        self.restartButton.setText(_translate("MainWindow", "Restart"))
