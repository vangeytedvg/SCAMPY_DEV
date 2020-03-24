"""
	linkdb.py
	Datamodel for the Scampy application (sqlAlchemy style)
"""

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base


class MailBox(Base):
	__tablename__ = 'mailbox'

	id = Column(Integer, primary_key=True)
	date_created = Column(DateTime())
	date_sent = Column(DateTime())
	mail_to = Column(String(255), nullable=False)
	subject = Column(String(255), nullable=False)
	mail_body = Column(String(1000), nullable=True)
	# Define a relation between MailBox and Projects
	project = relationship("Projects")

	def __init__(self, date_created, date_sent, mail_to, subject, mail_body):
		self.date_created = date_created
		self.date_sent = date_sent
		self.mail_to = mail_to
		self.subject = subject
		self.mail_body = mail_body


class Projects(Base):

	__tablename__ = "projects"

	id = Column(Integer, primary_key=True)
	# The mailbox.id primary key field is our key in this relation
	parent_mail_id = Column(Integer, ForeignKey('mailbox.id'))
	scan_path = Column(String(500), nullable=True)
	parent = relationship("MailBox")

	def __init__(self, parent, filepath):
		self.parent_mail_id = parent
		self.scan_path = filepath

	def __repr__(self):
		return "id='%s'" % (self.id)