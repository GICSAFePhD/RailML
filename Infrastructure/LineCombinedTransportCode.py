#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class LineCombinedTransportCode(object):
	def setWagonCompatibilityCode(self, aWagonCompatibilityCode : str):
		self.___wagonCompatibilityCode = aWagonCompatibilityCode

	def getWagonCompatibilityCode(self) -> str:
		return self.___wagonCompatibilityCode

	def setProfileNumber(self, aProfileNumber : int):	#TODO DEFINED AS INTEGER
		self.___profileNumber = aProfileNumber

	def getProfileNumber(self) -> int:	#TODO DEFINED AS INTEGER
		return self.___profileNumber

	def __init__(self):
		self.___wagonCompatibilityCode : str = None
		"""1 letter code: C, P"""
		self.___profileNumber : int = None	#TODO DEFINED AS INTEGER
		"""standard combined transport profile number (2 or 3 digits)"""

