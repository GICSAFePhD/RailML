#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tElementWithIDref
from Infrastructure import SignalX
from typing import List

class SignalMilepost(SignalX):
	def setShownValue(self, aShownValue : str):
		self.___shownValue = aShownValue

	def getShownValue(self) -> str:
		return self.___shownValue

	def setRefersToLine(self, aRefersToLine : tElementWithIDref):
		self._refersToLine = aRefersToLine

	def getRefersToLine(self) -> tElementWithIDref:
		return self._refersToLine

	def __init__(self):
		self.___shownValue : str = None
		"""kilometer value plus any further remark that is printed on the milepost, e.g. for documenting a kilometer gap"""
		self._refersToLine : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to the railway line to which the mileage value belongs"""

