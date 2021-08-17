#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import elementContainer
from typing import List

class Metadata(elementContainer.elementContainer):
	"""This is the top level element for file metadata information."""

	def __init__(self):	
		self.___title : str = None
		self.___date : str = None
		self.___creator : str = None
		self.___source : str = None
		self.___identifier : str = None
		self.___subject : str = None
		self.___format : str = None
		self.___description : str = None
		self.___publisher : str = None
	
	@property
	def Title(self):
		return self.___title
	@property
	def Date(self):
		return self.___date
	@property
	def Creator(self):
		return self.___creator
	@property
	def Source(self):
		return self.___source
	@property
	def Identifier(self):
		return self.___identifier
	@property
	def Subject(self):
		return self.___subject
	@property
	def Format(self):
		return self.___format
	@property
	def Description(self):
		return self.___description
	@property
	def Publisher(self):
		return self.___publisher

	@Title.setter
	def Title(self, aTitle : str):
		self.___title = aTitle
	@Date.setter
	def Date(self, aDate : str):
		self.___date = aDate
	@Creator.setter
	def Creator(self, aCreator : str):
		self.___creator = aCreator
	@Source.setter
	def Source(self, aSource : str):
		self.___source = aSource
	@Identifier.setter
	def Identifier(self, aIdentifier : str):
		self.___identifier = aIdentifier
	@Subject.setter
	def Subject(self, aSubject : str):
		self.___subject = aSubject
	@Format.setter
	def Format(self, aFormat : str):
		self.___format = aFormat
	@Description.setter
	def Description(self, aDescription : str):
		self.___description = aDescription
	@Publisher.setter
	def Publisher(self, aPublisher : str):
		self.___publisher = aPublisher

	# def __str__(self):  
	# 	print(f'Title:{self.Title}')
	# 	print(f'Date:{self.Date}')
	# 	print(f'Creator:{self.Creator}')
	# 	print(f'Source:{self.Source}')
	# 	print(f'Identifier:{self.Identifier}')
	# 	print(f'Subject:{self.Subject}')
	# 	print(f'Format:{self.Format}')
	# 	print(f'Description:{self.Description}')
	# 	print(f'Publisher:{self.Publisher}')
	# 	return ''