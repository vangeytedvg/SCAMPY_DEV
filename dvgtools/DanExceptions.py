"""
DanExceptions.py
Own defined exceptions
Author : Van Geyte Danny
24/02/2020
"""

# Base class for own exceptions
class Error(Exception):
    pass

# In case of problems with email
class MailSendError(Error):
    def __init__(self, msg, destination):
        self.__msg = msg
        self.__destination = destination


