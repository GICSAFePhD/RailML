#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class LineCombinedTransportCode(object):
	@property
	def WagonCompatibilityCode(self) -> str:
		return self.___wagonCompatibilityCode
	@property
	def ProfileNumber(self) -> int:
		return self.___profileNumber

	@WagonCompatibilityCode.setter
	def WagonCompatibilityCode(self, aWagonCompatibilityCode : str):
		self.___wagonCompatibilityCode = aWagonCompatibilityCode
	@ProfileNumber.setter
	def ProfileNumber(self, aProfileNumber : int):
		self.___profileNumber = aProfileNumber

	def __init__(self):
		self.___wagonCompatibilityCode : str = ""
		"""1 letter code: C, P"""
		self.___profileNumber : int = 0
		"""standard combined transport profile number (2 or 3 digits)"""

