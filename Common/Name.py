#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Name(object):
	def setName(self, aName : str):
		self.___name = aName

	def getName(self) -> str:
		return self.___name

	def setDescription(self, aDescription : str):
		self.___description = aDescription

	def getDescription(self) -> str:
		return self.___description

	def setLanguage(self, aLanguage : language):
		self.___language = aLanguage

	def getLanguage(self) -> language:
		return self.___language

	def __init__(self):
		self.___name : str = None
		"""should be interpreted in its elements' context (e.g. signal/name, vehicle/name)"""
		self.___description : str = None
		"""should be interpreted in its elements' context, substantiates the name"""
		self.___language : language = None
		"""natural language identification according to http://www.w3.org/TR/xml/#sec-lang-tag; should always be given"""

