# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(649, 396)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 90, 336, 204))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelUsername = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelUsername.setObjectName(_fromUtf8("labelUsername"))
        self.horizontalLayout_2.addWidget(self.labelUsername)
        self.textEditUsername = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEditUsername.setObjectName(_fromUtf8("textEditUsername"))
        self.horizontalLayout_2.addWidget(self.textEditUsername)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelPassword = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
        self.horizontalLayout.addWidget(self.labelPassword)
        self.textEditPassword = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEditPassword.setObjectName(_fromUtf8("textEditPassword"))
        self.horizontalLayout.addWidget(self.textEditPassword)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonLogin = QtGui.QPushButton(Dialog)
        self.pushButtonLogin.setGeometry(QtCore.QRect(290, 300, 99, 27))
        self.pushButtonLogin.setObjectName(_fromUtf8("pushButtonLogin"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelUsername.setText(_translate("Dialog", "Username", None))
        self.labelPassword.setText(_translate("Dialog", "Password", None))
        self.pushButtonLogin.setText(_translate("Dialog", "Login", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

