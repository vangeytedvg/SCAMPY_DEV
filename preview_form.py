# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/frm_preview.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frm_ScanPreview(object):
    def setupUi(self, frm_ScanPreview):
        frm_ScanPreview.setObjectName("frm_ScanPreview")
        frm_ScanPreview.resize(519, 693)
        self.verticalLayout = QtWidgets.QVBoxLayout(frm_ScanPreview)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(frm_ScanPreview)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 503, 637))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblPreview = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblPreview.setScaledContents(False)
        self.lblPreview.setObjectName("lblPreview")
        self.verticalLayout_2.addWidget(self.lblPreview)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(frm_ScanPreview)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(frm_ScanPreview)
        self.buttonBox.accepted.connect(frm_ScanPreview.accept)
        self.buttonBox.rejected.connect(frm_ScanPreview.reject)
        QtCore.QMetaObject.connectSlotsByName(frm_ScanPreview)

    def retranslateUi(self, frm_ScanPreview):
        _translate = QtCore.QCoreApplication.translate
        frm_ScanPreview.setWindowTitle(_translate("frm_ScanPreview", "Scan Preview"))
        self.lblPreview.setText(_translate("frm_ScanPreview", "Geen afbeelding..."))
