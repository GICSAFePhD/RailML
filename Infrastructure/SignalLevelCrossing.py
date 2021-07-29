#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tSignalLevelCrossingType, SignalX
from typing import List

class SignalLevelCrossing(SignalX.SignalX):
	@property
	def tSignalLevelCrossingType(self) -> tSignalLevelCrossingType:
		return self.___type
	@property
	def tElementWithIDref(self) -> tElementWithIDref:
		return self.___refersToLevelCrossing
	
	@tSignalLevelCrossingType.setter
	def tSignalLevelCrossingType(self, atSignalLevelCrossingType : tSignalLevelCrossingType):
		self.___type = atSignalLevelCrossingType
	@tElementWithIDref.setter
	def tElementWithIDref(self, *atElementWithIDref : tElementWithIDref):
		self.___refersToLevelCrossing = tElementWithIDref

	def __init__(self):
		self.___type : tSignalLevelCrossingType = tSignalLevelCrossingType.tSignalLevelCrossingType()
		# @AssociationType Infrastructure.tSignalLevelCrossingType
		# """type of the level crossing signal"""
		self.___refersToLevelCrossing : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 1..*
		# """reference to the level crossing element that is protected by the signal"""

