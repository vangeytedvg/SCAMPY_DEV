# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Overview = QtWidgets.QWidget()
        self.tab_Overview.setObjectName("tab_Overview")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_Overview)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tlbRefresh = QtWidgets.QToolButton(self.tab_Overview)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/repeat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tlbRefresh.setIcon(icon)
        self.tlbRefresh.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tlbRefresh.setObjectName("tlbRefresh")
        self.verticalLayout_4.addWidget(self.tlbRefresh)
        self.splitter = QtWidgets.QSplitter(self.tab_Overview)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.table_SentItems = QtWidgets.QTableWidget(self.splitter)
        self.table_SentItems.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_SentItems.setTabKeyNavigation(True)
        self.table_SentItems.setAlternatingRowColors(True)
        self.table_SentItems.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_SentItems.setObjectName("table_SentItems")
        self.table_SentItems.setColumnCount(0)
        self.table_SentItems.setRowCount(0)
        self.table_SentItems.horizontalHeader().setStretchLastSection(True)
        self.listPreview = QtWidgets.QListWidget(self.splitter)
        self.listPreview.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listPreview.setFlow(QtWidgets.QListView.LeftToRight)
        self.listPreview.setProperty("isWrapping", True)
        self.listPreview.setResizeMode(QtWidgets.QListView.Adjust)
        self.listPreview.setViewMode(QtWidgets.QListView.IconMode)
        self.listPreview.setObjectName("listPreview")
        self.sliderPreviewSize = QtWidgets.QSlider(self.splitter)
        self.sliderPreviewSize.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPreviewSize.setObjectName("sliderPreviewSize")
        self.verticalLayout_4.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab_Overview, "")
        self.tab_Create = QtWidgets.QWidget()
        self.tab_Create.setObjectName("tab_Create")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_Create)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.msgFrameBox = QtWidgets.QFrame(self.tab_Create)
        self.msgFrameBox.setStyleSheet("background-color: rgb(148, 0, 0);")
        self.msgFrameBox.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.msgFrameBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.msgFrameBox.setObjectName("msgFrameBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.msgFrameBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblWarningNewMail = QtWidgets.QLabel(self.msgFrameBox)
        self.lblWarningNewMail.setMinimumSize(QtCore.QSize(0, 40))
        self.lblWarningNewMail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblWarningNewMail.setIndent(4)
        self.lblWarningNewMail.setObjectName("lblWarningNewMail")
        self.horizontalLayout_2.addWidget(self.lblWarningNewMail)
        self.btnRestrictOverride = QtWidgets.QToolButton(self.msgFrameBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/folder-8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRestrictOverride.setIcon(icon1)
        self.btnRestrictOverride.setIconSize(QtCore.QSize(24, 24))
        self.btnRestrictOverride.setObjectName("btnRestrictOverride")
        self.horizontalLayout_2.addWidget(self.btnRestrictOverride)
        self.verticalLayout_2.addWidget(self.msgFrameBox)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblScanTarget = QtWidgets.QLabel(self.tab_Create)
        self.lblScanTarget.setObjectName("lblScanTarget")
        self.gridLayout_2.addWidget(self.lblScanTarget, 5, 1, 1, 1)
        self.txtProjectName = QtWidgets.QLineEdit(self.tab_Create)
        self.txtProjectName.setObjectName("txtProjectName")
        self.gridLayout_2.addWidget(self.txtProjectName, 0, 3, 1, 2)
        self.lblTo = QtWidgets.QLabel(self.tab_Create)
        self.lblTo.setObjectName("lblTo")
        self.gridLayout_2.addWidget(self.lblTo, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(618, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 2, 1, 3)
        self.btnScanDoc = QtWidgets.QPushButton(self.tab_Create)
        self.btnScanDoc.setObjectName("btnScanDoc")
        self.gridLayout_2.addWidget(self.btnScanDoc, 5, 0, 1, 1)
        self.lblBody = QtWidgets.QLabel(self.tab_Create)
        self.lblBody.setObjectName("lblBody")
        self.gridLayout_2.addWidget(self.lblBody, 3, 0, 1, 3)
        self.txtSubject = QtWidgets.QLineEdit(self.tab_Create)
        self.txtSubject.setObjectName("txtSubject")
        self.gridLayout_2.addWidget(self.txtSubject, 2, 3, 1, 2)
        self.txtBody = QtWidgets.QPlainTextEdit(self.tab_Create)
        self.txtBody.setObjectName("txtBody")
        self.gridLayout_2.addWidget(self.txtBody, 3, 3, 1, 2)
        self.lblSubject = QtWidgets.QLabel(self.tab_Create)
        self.lblSubject.setObjectName("lblSubject")
        self.gridLayout_2.addWidget(self.lblSubject, 2, 0, 1, 3)
        self.lblProjectName = QtWidgets.QLabel(self.tab_Create)
        self.lblProjectName.setStyleSheet("")
        self.lblProjectName.setObjectName("lblProjectName")
        self.gridLayout_2.addWidget(self.lblProjectName, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(518, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 4, 1, 1)
        self.txtTo = QtWidgets.QLineEdit(self.tab_Create)
        self.txtTo.setObjectName("txtTo")
        self.gridLayout_2.addWidget(self.txtTo, 1, 3, 1, 2)
        self.btnSaveEmail = QtWidgets.QPushButton(self.tab_Create)
        self.btnSaveEmail.setObjectName("btnSaveEmail")
        self.gridLayout_2.addWidget(self.btnSaveEmail, 4, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.tab_Create)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_Create)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.btnSendEmail = QtWidgets.QPushButton(self.tab_Create)
        self.btnSendEmail.setObjectName("btnSendEmail")
        self.verticalLayout_2.addWidget(self.btnSendEmail)
        spacerItem2 = QtWidgets.QSpacerItem(754, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_Create, "")
        self.tab_Test = QtWidgets.QWidget()
        self.tab_Test.setObjectName("tab_Test")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_Test)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_TestScanner = QtWidgets.QPushButton(self.tab_Test)
        self.btn_TestScanner.setObjectName("btn_TestScanner")
        self.verticalLayout.addWidget(self.btn_TestScanner)
        self.lblScampy = QtWidgets.QLabel(self.tab_Test)
        self.lblScampy.setText("")
        self.lblScampy.setObjectName("lblScampy")
        self.verticalLayout.addWidget(self.lblScampy)
        self.lblScannerTest = QtWidgets.QLabel(self.tab_Test)
        self.lblScannerTest.setObjectName("lblScannerTest")
        self.verticalLayout.addWidget(self.lblScannerTest)
        self.tabWidget.addTab(self.tab_Test, "")
        self.tab_Options = QtWidgets.QWidget()
        self.tab_Options.setObjectName("tab_Options")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_Options)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.tab_Options)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.btn_SaveOptions = QtWidgets.QPushButton(self.tab_Options)
        self.btn_SaveOptions.setObjectName("btn_SaveOptions")
        self.gridLayout.addWidget(self.btn_SaveOptions, 5, 1, 1, 1)
        self.txt_ScanFilePrefix = QtWidgets.QLineEdit(self.tab_Options)
        self.txt_ScanFilePrefix.setObjectName("txt_ScanFilePrefix")
        self.gridLayout.addWidget(self.txt_ScanFilePrefix, 1, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_Options)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_Options)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.txt_Destination = QtWidgets.QLineEdit(self.tab_Options)
        self.txt_Destination.setObjectName("txt_Destination")
        self.gridLayout.addWidget(self.txt_Destination, 0, 1, 1, 2)
        self.txtOwnEmailAddress = QtWidgets.QLineEdit(self.tab_Options)
        self.txtOwnEmailAddress.setObjectName("txtOwnEmailAddress")
        self.gridLayout.addWidget(self.txtOwnEmailAddress, 3, 1, 1, 2)
        self.btnSelectFolder = QtWidgets.QToolButton(self.tab_Options)
        self.btnSelectFolder.setObjectName("btnSelectFolder")
        self.gridLayout.addWidget(self.btnSelectFolder, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_Options)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.txtDefaultZipName = QtWidgets.QLineEdit(self.tab_Options)
        self.txtDefaultZipName.setObjectName("txtDefaultZipName")
        self.gridLayout.addWidget(self.txtDefaultZipName, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.tab_Options)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.txtGmailAppKey = QtWidgets.QLineEdit(self.tab_Options)
        self.txtGmailAppKey.setObjectName("txtGmailAppKey")
        self.gridLayout.addWidget(self.txtGmailAppKey, 4, 1, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 366, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab_Options, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 30))
        self.menubar.setObjectName("menubar")
        self.menu_Bestand = QtWidgets.QMenu(self.menubar)
        self.menu_Bestand.setObjectName("menu_Bestand")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(50, 50))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Afsluiten = QtWidgets.QAction(MainWindow)
        self.action_Afsluiten.setObjectName("action_Afsluiten")
        self.action_Over = QtWidgets.QAction(MainWindow)
        self.action_Over.setObjectName("action_Over")
        self.action_NewMail = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgs/scannermail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_NewMail.setIcon(icon2)
        self.action_NewMail.setObjectName("action_NewMail")
        self.action_Overview = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgs/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Overview.setIcon(icon3)
        self.action_Overview.setObjectName("action_Overview")
        self.actionTest_Scanner = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgs/startup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTest_Scanner.setIcon(icon4)
        self.actionTest_Scanner.setObjectName("actionTest_Scanner")
        self.menu_Bestand.addAction(self.action_Afsluiten)
        self.menu_Help.addAction(self.action_Over)
        self.menubar.addAction(self.menu_Bestand.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Overview)
        self.toolBar.addAction(self.action_NewMail)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTest_Scanner)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtProjectName, self.txtTo)
        MainWindow.setTabOrder(self.txtTo, self.txtSubject)
        MainWindow.setTabOrder(self.txtSubject, self.txtBody)
        MainWindow.setTabOrder(self.txtBody, self.btnSaveEmail)
        MainWindow.setTabOrder(self.btnSaveEmail, self.btnScanDoc)
        MainWindow.setTabOrder(self.btnScanDoc, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.btnSendEmail)
        MainWindow.setTabOrder(self.btnSendEmail, self.table_SentItems)
        MainWindow.setTabOrder(self.table_SentItems, self.btn_TestScanner)
        MainWindow.setTabOrder(self.btn_TestScanner, self.btnSelectFolder)
        MainWindow.setTabOrder(self.btnSelectFolder, self.btn_SaveOptions)
        MainWindow.setTabOrder(self.btn_SaveOptions, self.txt_Destination)
        MainWindow.setTabOrder(self.txt_Destination, self.txt_ScanFilePrefix)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SCaMPy Scan And Mail with Python"))
        self.tlbRefresh.setText(_translate("MainWindow", "Vernieuwen"))
        self.table_SentItems.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Overview), _translate("MainWindow", "Gemaakte berichten"))
        self.lblWarningNewMail.setText(_translate("MainWindow", "Opgepast, deze mail is reeds verzonden en kan niet meer worden aangepast. Maak een nieuwe email aan! "))
        self.btnRestrictOverride.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/imgs/warning.png\"/> Wijzigingen aanbrengen aan deze reeds verzonden email.</p><p>Opgepast, dit wordt in de logs opgeslagen.</p></body></html>"))
        self.btnRestrictOverride.setText(_translate("MainWindow", "..."))
        self.lblScanTarget.setText(_translate("MainWindow", "..."))
        self.lblTo.setText(_translate("MainWindow", "Bestemmeling(en):"))
        self.btnScanDoc.setText(_translate("MainWindow", "Scan"))
        self.lblBody.setText(_translate("MainWindow", "Boodschap:"))
        self.lblSubject.setText(_translate("MainWindow", "Onderwerp:"))
        self.lblProjectName.setText(_translate("MainWindow", "Projectnaam:"))
        self.btnSaveEmail.setText(_translate("MainWindow", "Bewaar"))
        self.btnSendEmail.setText(_translate("MainWindow", "Verzend email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Create), _translate("MainWindow", "Nieuwe Email"))
        self.btn_TestScanner.setText(_translate("MainWindow", "Test Scanner"))
        self.lblScannerTest.setText(_translate("MainWindow", "Nog geen test uitgevoerd, druk op Test Scanner..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Test), _translate("MainWindow", "Scanner Details"))
        self.label_2.setText(_translate("MainWindow", "Uw email adres:"))
        self.btn_SaveOptions.setText(_translate("MainWindow", "Opslaan"))
        self.label.setText(_translate("MainWindow", "Naam zipfile:"))
        self.label_5.setText(_translate("MainWindow", "Sla scans op in deze folder:"))
        self.btnSelectFolder.setText(_translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "Prefix voor gescande bestanden:"))
        self.label_3.setText(_translate("MainWindow", "GMail App-key:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Options), _translate("MainWindow", "Opties"))
        self.menu_Bestand.setTitle(_translate("MainWindow", "&Bestand"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Afsluiten.setText(_translate("MainWindow", "&Afsluiten"))
        self.action_Over.setText(_translate("MainWindow", "&Over"))
        self.action_NewMail.setText(_translate("MainWindow", "Nieuwe Scan en Mail"))
        self.action_NewMail.setToolTip(_translate("MainWindow", "Aanmaken nieuwe email"))
        self.action_Overview.setText(_translate("MainWindow", "Overzicht gemaakte mails"))
        self.action_Overview.setToolTip(_translate("MainWindow", "Overzicht verzonden items"))
        self.actionTest_Scanner.setText(_translate("MainWindow", "Test Scanner"))
        self.actionTest_Scanner.setToolTip(_translate("MainWindow", "Test of the scanner klaar is"))
import images_rc
