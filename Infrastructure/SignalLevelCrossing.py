#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tSignalLevelCrossingType
from Common import tElementWithIDref
from Infrastructure import SignalX
from typing import List

class SignalLevelCrossing(SignalX):
	def setType(self, aType : tSignalLevelCrossingType):
		self.___type = aType

	def getType(self) -> tSignalLevelCrossingType:
		return self.___type

	def setRefersToLevelCrossing(self, *aRefersToLevelCrossing : tElementWithIDref*):
		self._refersToLevelCrossing = aRefersToLevelCrossing

	def getRefersToLevelCrossing(self) -> tElementWithIDref*:
		return self._refersToLevelCrossing

	def __init__(self):
		self.___type : tSignalLevelCrossingType = None
		# @AssociationType Infrastructure.tSignalLevelCrossingType
		# """type of the level crossing signal"""
		self._refersToLevelCrossing : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 1..*
		# """reference to the level crossing element that is protected by the signal"""

