"""
    scampy.py
    SCan and Mail with PYthon
    Main application entry module
    Author : Danny Van Geyte
    Created : 17/12/2019 - 12:58
    History:  26/01/2020 - 11:47
              20/02/2020 - 13:25 Finishing touch on context menu for listview
              24/03/2020 - 15:22 Integrating with GIT, GIT OK
"""
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_form import Ui_MainWindow
from scannermanager import ScannerManager
from dvgtools.dvgFileUtills import isMailOk, nextImageFileName, extractFileNameOnly, makezip, Get_png_images, nukeFile
from dvgtools.DanExceptions import MailSendError
from MsgBox import MsgBox
from Settings import SettingsManager
from database.db import Session
from database.linkdb import *
import datetime
from preview import PreviewForm
import time
import glob
from sqlalchemy import desc
from gmailmanager import GmailClient
import logging
# Global vars
ERR_STYLE = "background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);"
COLUMN_COUNT = 7
MAILBOX = 0
PROJECTS = 1
SCAN_TARGET = "*.pdf"
SCAN_SOURCE = "*.png"

logging.Logger("dannyslog")
logging.basicConfig(filename="scampy.log.txt", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class SCaMPy(QMainWindow, Ui_MainWindow):
    # Private values for last inserted record id's
    _lastIndexOfMail = 0
    _lastIndexOfProject = 0
    _lastIndexOfScans = 0

    # Name of scan target base folder
    _scan_base_folder = ""
    _full_doc_path = ""
    _file_prefix = ""
    _defaultZipFileName = ""
    _ownEmailAddress = ""
    _gmailappkey = ""
    _iconSize = QSize(64, 64)

    def __init__(self):
        super(SCaMPy, self).__init__()
        self.setupUi(self)
        self.loadsettings()
        # Setup the logging mechanic
        # makedb()
        logging.info("Application startup")
        """ Some initial 'make-up' """
        # self.setWindowState(Qt.WindowMaximized)
        # Be sure to be on the main tab
        self.sliderPreviewSize.setValue(32)
        self.sliderPreviewSize.setMinimum(32)
        self.sliderPreviewSize.setMaximum(241)
        self.sliderPreviewSize.setSingleStep(25)
        self.sliderPreviewSize.setTickInterval(25)
        self.sliderPreviewSize.setTickPosition(QSlider.TicksAbove)
        self.sliderPreviewSize.valueChanged.connect(self.changeSizeOfIcons2)

        self.horizontalSlider.setMinimum(32)
        self.horizontalSlider.setMaximum(241)
        self.horizontalSlider.setSingleStep(25)
        self.horizontalSlider.setTickInterval(25)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)
        self.horizontalSlider.valueChanged.connect(self.changeSizeOfIcons)
        self.horizontalSlider.setValue(32)
        self.tabWidget.setCurrentIndex(0)
        self.listWidget.setIconSize(self._iconSize)
        self.listWidget.setEditTriggers(QAbstractItemView.CurrentChanged |
                                        QAbstractItemView.DoubleClicked |
                                        QAbstractItemView.EditKeyPressed)
        # Toolbar buttons and menu
        self.tlbRefresh.pressed.connect(self.selectNothing)
        self.action_NewMail.triggered.connect(self.new_scampy)
        self.actionTest_Scanner.triggered.connect(self.show_settings_panel)
        self.action_Overview.triggered.connect(self.showMailOverview)
        self.action_Afsluiten.triggered.connect(self.close)
        # Tab 2
        self.btn_TestScanner.pressed.connect(self.is_scanner_online)
        self.btnSaveEmail.pressed.connect(self.save_email)
        self.btnScanDoc.pressed.connect(self.scan_doc)
        self.btnSendEmail.pressed.connect(self.sendMail)
        self.btnRestrictOverride.pressed.connect(self.overrideRestriction)
        # option part actions
        self.btnSelectFolder.pressed.connect(self.select_scan_target_folder)
        self.btn_SaveOptions.pressed.connect(self.save_app_settings)
        self.toggleScanControls(False)
        # Overview table definition and events
        self._loadSentItemsTable("all")
        # When a row is clicked in the overview table
        self.table_SentItems.selectionModel().selectionChanged.connect(self.table_row_changed)
        self.listPreview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listPreview.customContextMenuRequested.connect(self.showcontextmenu)
        self.listWidget.customContextMenuRequested.connect(self.showcontextmenu)
        self.listPreview.itemClicked.connect(self.getCurrentScan)
        self.listWidget.itemClicked.connect(self.getCurrentScan)
        self.msgFrameBox.setVisible(False)

    def overrideRestriction(self):
        if MsgBox.show(title="Hela!", icontype=QMessageBox.Warning, 
                       text="Override Restrictions", subtext="Are you sure?", 
                       buttons=QMessageBox.Yes | QMessageBox.Cancel) == QMessageBox.Yes:
            self.msgFrameBox.setStyleSheet("background-color: rgb(85, 170, 0);")
            self.lblWarningNewMail.setText("You can change details now! Notice that SCaMPy has logged this event...")
            logging.warning(f"User selected override on a sent email mail id = {self._lastIndexOfMail}")

    def selectNothing(self):
        self.showMailOverview()
        self.listPreview.clear()

    def getCurrentScan(self):
        print("Kwak")

    def showcontextmenu(self, point):
        """
            Show the context menu for the selected item
            point is the location of the mouse when click occurred
        """
        index=self.table_SentItems.indexAt(point)
        if not index.isValid():
            return
        # if we get here, we are at a valid list item
        item=self.listPreview.itemAt(point)
        if not item:
            return
        # Construct the menu
        self.my_menu=QMenu(self.listPreview)
        # Add options
        delete_option=self.my_menu.addAction(f"Delete scan")
        copy_option=self.my_menu.addAction(f"Kopieer pad naar bestand")
        # Execute and wait for menu item selection
        user_action=self.my_menu.exec_(self.listPreview.mapToGlobal(point))
        # See what user clicked on
        if user_action == delete_option:
            self.delete_scanned_document(item.text())
        elif user_action == copy_option:
            print("Copy path")

    def delete_scanned_document(self, itemname):
        """
        Remove a scanned document from the listview
        """
        if MsgBox.show(title = "Vraag", text = "Deze scan verwijderen?", icontype = QMessageBox.Question, subtext = "Dit kan niet ongedaan gemaakt worden", buttons = QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return

        file_to_delete=self._scan_base_folder + os.sep + str(self._lastIndexOfMail) + os.sep + itemname
        try:
            os.remove(file_to_delete)
            self._populate2(self.listPreview, self._lastIndexOfMail)
            self._populate2(self.listWidget, self._lastIndexOfMail)
            logging.warning(f"File {file_to_delete} was deleted by the user!")
        except Exception as e:
            logging.warning(f"File {file_to_delete} could not be deleted by the user!")
            MsgBox.show("Probleem!", QMessageBox.Critical, "Fout", "Bestand kan niet worden gewist", QMessageBox.Ok)

    def table_row_changed(self, *args):
        """ Get info from the cell with the id """
        id=self.table_SentItems.item(self.table_SentItems.currentIndex().row(), 0).text()
        # Now get the scans if any and show them
        self._populate2(self.listPreview, id)
        self._populate2(self.listWidget, id)
        # make the selected email the active one
        self.activate_mail_instance(id)

    def activate_mail_instance(self, messageid):
        """
            Get the contents of the selected mail
        :param messageid: id of selected message
        :return: Nothing
        """
        self._lastIndexOfMail=messageid
        session=Session()
        mails=session.query(MailBox).filter(MailBox.id == messageid).first()
        proj=session.query(Projects).filter(Projects.parent_mail_id == messageid).first()
        # fill the textfields with the contents of the mail,
        # also activate the 'scan' and 'send' buttons in this case
        self.txtTo.setText(mails.mail_to)
        self.txtSubject.setText(mails.subject)
        self.txtProjectName.setText(proj.scan_path)
        self.txtBody.setPlainText(mails.mail_body)
        if not mails.date_sent:
            # user can still modify this email
            self.lblWarningNewMail.setVisible(True)
            # buttons
            self.msgFrameBox.setStyleSheet("background-color: rgb(148, 0, 0);")
            self.msgFrameBox.setVisible(False)
            self.btnSendEmail.setEnabled(True)
            self.btnSaveEmail.setEnabled(True)
            self.btnScanDoc.setEnabled(True)
            # input boxes
            self.txtTo.setEnabled(True)
            self.txtSubject.setEnabled(True)
            self.txtBody.setEnabled(True)
            self.txtProjectName.setEnabled(True)
        else:
            # mail was already sent, changes not allowed anymore
            self.msgFrameBox.setVisible(True)
            self.btnSendEmail.setEnabled(False)
            self.btnSaveEmail.setEnabled(False)
            self.btnScanDoc.setEnabled(False)
            self.txtTo.setEnabled(False)
            self.txtSubject.setEnabled(False)
            self.txtBody.setEnabled(False)
            self.txtProjectName.setEnabled(False)

    def showMailOverview(self):
        self.tabWidget.setCurrentIndex(0)
        self._loadSentItemsTable("all")

    def _loadSentItemsTable(self, status):
        """
            Fill sent items table
        :param status: sent or unset
        :return:
        """
        # Number of columns
        session=Session()
        self.table_SentItems.setColumnCount(COLUMN_COUNT)
        self.table_SentItems.clear()

        """
            The next part was tricky, when creating a join, the results are returns with indexes
            for each table.  Hence in this case MailBox in table 0, and Projects is index 1.
            The SqlAlchemy code is equivalent to this SQL
                SELECT mailbox.id AS mailbox_id, mailbox.date_created AS mailbox_date_created,
                   mailbox.date_sent AS mailbox_date_sent, mailbox.mail_to AS mailbox_mail_to,
                   mailbox.subject AS mailbox_subject, mailbox.mail_body AS mailbox_mail_body,
                   projects.id AS projects_id, projects.parent_mail_id AS projects_parent_mail_id,
                   projects.scan_path AS projects_scan_path
                FROM mailbox JOIN projects ON mailbox.id = projects.parent_mail_id
                ORDER BY mailbox_id desc
        """
        mails=session.query(MailBox, Projects).join(Projects,
                                                      MailBox.id == Projects.parent_mail_id).order_by(desc(MailBox.id))

        # Set the headers
        self.table_SentItems.setHorizontalHeaderLabels(("ID", "Datum aanmaak",
                                                        "Datum Verzonden", "Naar",
                                                        "Onderwerp", "Project id", "Project naam"))
        # Create rows, use double ( for tuple
        rows=[]
        for mail in mails:
            # Notice the indexes of the table
            rows.append((str(mail[MAILBOX].id),
                         str(mail[MAILBOX].date_created),
                         str(mail[MAILBOX].date_sent),
                         mail[MAILBOX].mail_to,
                         mail[MAILBOX].subject,
                         str(mail[PROJECTS].id),
                         mail[PROJECTS].scan_path
                         ))

        self.table_SentItems.setRowCount(len(rows))
        for row, cols in enumerate(rows):
            for col, text in enumerate(cols):
                table_item=QTableWidgetItem(text)
                # Optional, but very useful.
                table_item.setData(Qt.UserRole + 1, "user")
                self.table_SentItems.setItem(row, col, table_item)
        # Make the table look good
        self.table_SentItems.resizeColumnsToContents()
        # Don't need to see id field
        self.table_SentItems.hideColumn(5)

    def sendMail(self):
        """
            Send the mail via the Gmail server.
            Note, due to an unknown reason, the yagmail library can't send
            zipfiles.  Therefore the code has been changed to send each png file.
            Code adapted on 11/01/2020
        """
        # Zip the files
        # result = makezip(self._scan_base_folder, self._defaultZipFileName, self._lastIndexOfMail)
        result=Get_png_images(self._scan_base_folder + os.sep + str(self._lastIndexOfMail))
        print(result)
        mg=GmailClient(receiver = self.txtTo.text(), body = self.txtBody.toPlainText(),
                         subject=self.txtSubject.text(), files=result, gmail_key=self._gmailappkey)
        
        try:
            mg.sendGMail()
            session = Session()
            x = session.query(MailBox).get(self._lastIndexOfMail)
            # Set sent date and time
            x.date_sent = datetime.datetime.now()
            session.commit()
            logging.info(f"Mail sent and updated record {self._lastIndexOfMail}")       
        except MailSendError as err:
            MsgBox.show("Probleem!", QMessageBox.Critical, "Fout", "Email niet verzonden!", QMessageBox.Ok)
            logging.error(f"Unable to send mail {err.msg} {err.destination}")

    """ The following two methods work on different list widgets """

    def changeSizeOfIcons(self):
        z = self.horizontalSlider.value()
        ps = QSize(z, z)
        self.listWidget.setIconSize(ps)

    def changeSizeOfIcons2(self):
        z = self.sliderPreviewSize.value()
        ps = QSize(z, z)
        self.listPreview.setIconSize(ps)

    def toggleScanControls(self, state):
        """
            Toggle enabled state of the scan controls
        :param state: false or true (enabled/disabled)
        :return:
        """
        self.btnScanDoc.setEnabled(state)
        self.btnSendEmail.setEnabled(state)

    def new_scampy(self):
        """
            Select the New Mail tab
        """
        self.tabWidget.setCurrentIndex(1)
        path = self._scan_base_folder + os.sep + str(self._lastIndexOfMail)
        self._populate()

    def is_scanner_online(self):
        """
            Check if the scanner can be reached
        """
        logging.info("Test scanner started")
        self.lblScannerTest.setText(
            "Test wordt uitgevoerd, dit kan enkele ogenblikken duren!....")
        QApplication.processEvents()
        scanresult = ScannerManager.check_scanner_alive()
        if scanresult == "No device":
            logging.error("Scanner not online, or wrong WIFI hotspot")
            self.lblScampy.setPixmap(QPixmap(":/imgs/smallangryscampy.png"))
            self.lblScannerTest.setText("De scanner is blijkbaar niet online. Kijk of hij aanstaat "
                                        "en dat de juiste WIFI hotspot is gekozen op deze computer!")
            return False
        else:
            logging.info("Scanner ready")
            self.lblScampy.setPixmap(QPixmap(":/imgs/smallhappyscampy.png"))
            self.lblScannerTest.setText(
                "De scanner is gevonden!\nDit zijn de details van de driver:\n" + scanresult)
            return True

    def checkInputFields(self):
        """
            Validates the input fields for a new email.
            If fields are not filled in, their label will become red
        """
        # This array will hold any invalid field message wich are shown afterwards to the user
        incorrectFields = []
        if len(self.txtProjectName.text()) == 0:
            self.lblProjectName.setStyleSheet(ERR_STYLE)
            incorrectFields.append("Project naam")
        else:
            self.lblProjectName.setStyleSheet("")
        if isMailOk(self.txtTo.text()):
            self.lblTo.setStyleSheet("")
        else:
            self.lblTo.setStyleSheet(ERR_STYLE)
            incorrectFields.append("Bestemmeling, kijk of email adres correct is!")

        if len(self.txtSubject.text()) == 0:
            self.lblSubject.setStyleSheet(ERR_STYLE)
            incorrectFields.append("Onderwerp")
        else:
            self.lblSubject.setStyleSheet("")
        if len(self.txtBody.toPlainText()) == 0:
            self.lblBody.setStyleSheet(ERR_STYLE)
            incorrectFields.append("Boodschap")
        else:
            self.lblBody.setStyleSheet("")

        return incorrectFields

    def save_email(self):
        """
            Adds or update a new record to the scampy mailbox.
        """
        mail_action = "CREATE"
        if self._lastIndexOfMail:
            """ We already have a record """
            mail_action = "UPDATE"
            path = self._scan_base_folder + os.sep + str(self._lastIndexOfMail)
            self._full_doc_path = path

        if len(self.checkInputFields()) == 0:
            session = Session()
            date_created = datetime.datetime.now()
            date_sent = None
            mailbox_item = MailBox(date_created,
                                   date_sent,
                                   self.txtTo.text(),
                                   self.txtSubject.text(),
                                   self.txtBody.toPlainText())
            # Add new record
            if mail_action == "CREATE":
                session.add(mailbox_item)
                print("Message created")
                session.commit()
                self._lastIndexOfMail = mailbox_item.id
                project_item = Projects(mailbox_item.id, self.txtProjectName.text())
                session.add(project_item)
                session.commit()
                # Remember last project item id
                self._lastIndexOfProject = project_item.id
                logging.info(f"Created record {mailbox_item.id}")
                # Now create the target folder for the scans related to this email
                # Note, the folders will reside under the selected target folder in the settings.
                path = self._scan_base_folder + os.sep + str(self._lastIndexOfMail)
                self.lblScanTarget.setText(path)
                logging.warning(f"Creating folder {path}")
                try:
                    os.mkdir(path)
                except Exception as ex:
                    logging.error(f"Could not create path {path} {ex}")
            else:
                print("Message updated")
                # Get the item with the last mail id and update this record
                x = session.query(MailBox).get(self._lastIndexOfMail)
                # Now we can update the information
                x.subject = self.txtSubject.text()
                x.mail_to = self.txtTo.text()
                x.mail_body = self.txtBody.toPlainText()
                session.commit()
                logging.info(f"Updated record {self._lastIndexOfMail}")
                self.showMailOverview()

            session.close()
            # Now enable the scanning controls
            self.toggleScanControls(True)
        else:
            errfields = ""
            for field in self.checkInputFields():
                errfields += field + "\n"
            MsgBox.show("Probleem!", QMessageBox.Critical,
                        "De volgende velden zijn niet ingevuld!", errfields, QMessageBox.Ok)
            logging.error(f"Problem with input")
            self.txtProjectName.setFocus()

            return False

    def deleteScannedImage(self):
        # TODO : Continue here
        # Need to get the row nr of the icon, then we are
        # able to delete it
        p = QModelIndex(self.listWidget.currentIndex())
        argm = int(p.row())
        # For some reason, takeItem gives an Type Error,
        # even when passing the requested int value.  This is
        # a workaround for now:
        try:
            self.listWidget.takeItem(self.listWidget.takeItem(argm))
        except:
            pass

    def _images(self, location):
        """ Return a list of filenames  """
        # Start with an empty list
        images = []
        pattern = os.path.join(location, '*.png')
        images.extend(glob.glob(pattern))
        return images

    def _populate2(self, widget, idx):
        ''' Fill the list with images from the
            current directory in self._dirpath. '''

        # In case we're repopulating, clear the list
        widget.clear()
        # Create a list item for each image file,
        # setting the text and icon appropriately
        for image in self._images(self._scan_base_folder + os.sep + str(idx)):
            ic = QIcon()
            it = QListWidgetItem()
            ic.addPixmap(QPixmap(image))
            it.setText(extractFileNameOnly(image))
            it.setIcon(ic)
            widget.addItem(it)

    def _populate(self):
        ''' Fill the list with images from the
            current directory in self._dirpath. '''

        # In case we're repopulating, clear the list
        self.listWidget.clear()
        # Create a list item for each image file,
        # setting the text and icon appropriately
        for image in self._images(self._scan_base_folder + os.sep + str(self._lastIndexOfMail)):
            ic = QIcon()
            it = QListWidgetItem()
            ic.addPixmap(QPixmap(image))
            it.setText(extractFileNameOnly(image))
            it.setIcon(ic)
            self.listWidget.addItem(it)

    def scan_doc(self):
        """
            Scan a document
        :return:
        """
        logging.info("Starting scan of document")
        self.btnScanDoc.setText("Eventjes geduld")

        # Get a new unique filename
        new_filename = nextImageFileName(self._scan_base_folder +
                                         os.sep +
                                         str(self._lastIndexOfMail),
                                         self._file_prefix)
        logging.info(f"Next new document : {new_filename}")
        try:
            zen = ScannerManager(72, 0)
            zen.scan_document(new_filename)
            p_screen = PreviewForm(new_filename)
            t = p_screen.exec()
            logging.info(t)
            self._populate()
        except Exception as zer:
            MsgBox.show("Probleem!", QMessageBox.Critical,
                        "Scanner probleem", "", QMessageBox.Ok)
            logging.error("Scanner not connecting")

        QApplication.processEvents()
        self.btnScanDoc.setText("Scan")

    # ### SETTINGS SECTION ###
    def select_scan_target_folder(self):
        """
            Show folder selection dialog
        """
        initial_path = QDir.currentPath()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog + QFileDialog.DirectoryOnly
        self.txt_Destination.setText(
            str(QFileDialog.getExistingDirectory(self,
                                                 "Select default playlist folder",
                                                 initial_path,
                                                 options=options)))

    def save_app_settings(self):
        self.saveSettings()

    def show_settings_panel(self):
        self.tabWidget.setCurrentIndex(2)

    """ SETTINGS """

    def closeEvent(self, event):
        """
            Overrides the base close event
        :param event: event to override
        :return:
        """
        logging.info("Application shutting down")
        self.saveSettings()

    def saveSettings(self):
        """ Write all available options to the system """
        logging.info("Saving settings")
        this_settings = {
            "position": self.pos(),
            "size": self.size(),
            "scanfilepath": self.txt_Destination.text(),
            "scanfileprefix": self.txt_ScanFilePrefix.text(),
            "defaultzip": self.txtDefaultZipName.text(),
            "sendermailaddress": self.txtOwnEmailAddress.text(),
            "gmailappkey": self.txtGmailAppKey.text(),
        }
        mysettings = SettingsManager()
        mysettings.saveSettings(this_settings, 'denkatech', 'scanner')
        self._scan_base_folder = self.txt_Destination.text()
        self.lblScanTarget.setText(self._scan_base_folder)
        self._file_prefix = self.txt_ScanFilePrefix.text()
        self._defaultZipFileName = self.txtDefaultZipName.text()
        self._ownEmailAddress = self.txtOwnEmailAddress.text()
        self._gmailappkey = self.txtGmailAppKey.text()

    def loadsettings(self):
        # Get stored settings
        this_settings = {
            "position": 0,
            "size": 0,
            "scanfilepath": None,
            "scanfileprefix": None,
            "defaultzip": None,
            "sendermailaddress": None,
            "gmailappkey": None,
        }
        setting = SettingsManager()
        this_settings_getter = setting.load_settings(
            this_settings, 'denkatech', 'scanner')
        # Restore the size of our form
        try:
            self.move(this_settings_getter["position"])
            self.resize(this_settings_getter["size"])
            self.txt_Destination.setText(this_settings_getter["scanfilepath"])
            self.txt_ScanFilePrefix.setText(this_settings_getter["scanfileprefix"])
            self._scan_base_folder = this_settings_getter["scanfilepath"]
            self.lblScanTarget.setText(self._scan_base_folder)
            self._file_prefix = this_settings_getter["scanfileprefix"]
            self.txtDefaultZipName.setText(this_settings_getter["defaultzip"])
            self._defaultZipFileName = this_settings_getter["defaultzip"]
            self.txtOwnEmailAddress.setText(this_settings_getter["sendermailaddress"])
            self._ownEmailAddress = this_settings_getter["sendermailaddress"]
            self._gmailappkey = this_settings_getter["gmailappkey"]
            self.txtGmailAppKey.setText(self._gmailappkey)
        except Exception as e:
            print(e)
        if self._scan_base_folder == "":
            MsgBox.show("Probleem!", QMessageBox.Critical,
                        "Gelieve target voor scans in te stellen", "", QMessageBox.Ok)


# ## MAIN APPLICATION ENTRY POINT ## #
if __name__ == '__main__':
    import sys
    import os

    app = QApplication(sys.argv)
    pixmap = QPixmap("splash.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    splash.showMessage("Opstarten ...")
    # # time.sleep(1)
    if os.path.isfile("newdark1.css"):
        styleSheetFile = "newdark.css"
        with open(styleSheetFile, "r") as fh:
            app.setStyleSheet(fh.read())
    else:
        print("Stylesheet newdark.css not found, running in standard GUI settings!")
    main_form = SCaMPy()
    splash.showMessage("Laden hoofdscherm")
    # # time.sleep(5)
    main_form.show()
    splash.finish(main_form)
    sys.exit(app.exec_())

