"""
    gmailmanager.py
    Send an email using yagmail (Gmail)
"""
import yagmail
import logging
from dvgtools.DanExceptions import MailSendError


class GmailClient:

    _receiver = ""
    _body = ""
    _filename = []
    _subject = ""

    def __init__(self, receiver=None, body=None, files=None, subject=None, gmail_key=None):
        """
            Ctor
        :param receiver: email address of the receiver
        :param body: body text
        :param filename: name of the zipfile
        :param subject: subject of email
        :param gmail_key: gmail app key
        """
        self._receiver = receiver
        self._body = body
        self._filename = files
        self._subject = subject
        # Create keyring on instantiation
        print(self._filename)

    def sendGMail(self):
        """
            Send email
        :return: True or False
        """
        yagmail.register('vangeytedvg@gmail.com', 'freqqwjyfttqaggg')
        yag = yagmail.SMTP("vangeytedvg@gmail.com")

        content = [self._body, 'File attached']
        # EAFP
        try:
            yag.send(self._receiver, self._subject, contents=content, attachments=self._filename)
        except Exception:
            raise MailSendError("Mail can't be sent (to is):", self._receiver)

