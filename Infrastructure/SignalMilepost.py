#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import SignalX
from typing import List

class SignalMilepost(SignalX.SignalX):
	@property
	def ShownValue(self) -> str:
		return self.___shownValue
	@property
	def tElementWithIDref(self) -> tElementWithIDref:
		return self.___refersToLine
	
	@ShownValue.setter
	def ShownValue(self, aShownValue : str):
		self.___shownValue = aShownValue
	@tElementWithIDref.setter
	def tElementWithIDref(self, atElementWithIDref : tElementWithIDref):
		self.___refersToLine = atElementWithIDref

	def __init__(self):
		self.___shownValue : str = ""
		"""kilometer value plus any further remark that is printed on the milepost, e.g. for documenting a kilometer gap"""
		self.___refersToLine : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to the railway line to which the mileage value belongs"""

