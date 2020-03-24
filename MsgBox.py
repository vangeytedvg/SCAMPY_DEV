from PyQt5.QtWidgets import QMessageBox


class MsgBox:

    @staticmethod
    def show(title, icontype, text, subtext, buttons):
        msg = QMessageBox()
        msg.setIcon(icontype)
        msg.setText(text)
        msg.setInformativeText(subtext)
        msg.setWindowTitle(title)
        msg.setStandardButtons(buttons)
        retval = msg.exec_()
        return retval
