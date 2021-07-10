#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tBitPatternAny
from typing import List

class InitStatus(object):
	"""This is the description of the interface status in command and message direction which is assumed in start-up cases, i.e. when both sides of the system are just powered up."""
	def setComString(self, aComString : tBitPatternAny):
		self.___comString = aComString

	def getComString(self) -> tBitPatternAny:
		return self.___comString

	def setMessString(self, aMessString : tBitPatternAny):
		self.___messString = aMessString

	def getMessString(self) -> tBitPatternAny:
		return self.___messString

	def __init__(self):
		self.___comString : tBitPatternAny = None
		"""The status of all outputs as bit string starting with lowest bit. "0"-inactive, "1"-active, "x"-does not matter"""
		self.___messString : tBitPatternAny = None
		# @AssociationType Interlocking.tBitPatternAny
		# @AssociationType Interlocking.tBitPatternAny
		# """The status of all inputs as bit string starting with lowest bit. "0"-inactive, "1"-active, "x"-does not matter"""

