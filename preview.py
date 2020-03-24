"""
    preview.py
    Dialog showing a preview of the scanned image
    Author : Danny Van Geyte
    Created : 18/12/2019
    Last Mod : 19/12/2019
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from preview_form import Ui_frm_ScanPreview


class PreviewForm(QDialog, Ui_frm_ScanPreview):

    _previewFile = ""

    def __init__(self, previewfile):
        self._previewFile = previewfile
        super(PreviewForm, self).__init__()
        self.setupUi(self)
        pixmap = QPixmap(previewfile)

        # Load the image pixmap
        self.lblPreview.setPixmap(pixmap)



