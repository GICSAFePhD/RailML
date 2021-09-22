#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Name(object):
	@property
	def Name(self) -> str:
		return self.___name
	@property
	def Description(self) -> str:
		return self.___description
	@property
	def Language(self) -> str:
		return self.___language

	@Name.setter
	def Name(self, aName : str):
		self.___name = aName
	@Description.setter
	def Description(self, aDescription : str):
		self.___description = aDescription
	@Language.setter
	def Language(self, aLanguage : str):
		self.___language = aLanguage

	def __init__(self):
		self.___name : str = None
		"""should be interpreted in its elements' context (e.g. signal/name, vehicle/name)"""
		self.___description : str = None
		"""should be interpreted in its elements' context, substantiates the name"""
		#self.___language : language = None
		self.___language : str = None
		"""natural language identification according to http://www.w3.org/TR/xml/#sec-lang-tag; should always be given"""