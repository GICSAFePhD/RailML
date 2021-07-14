#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tSignalCatenaryType import tSignalCatenaryType
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.SignalX import SignalX
from typing import List

class SignalCatenary(SignalX):
	def setType(self, aType : tSignalCatenaryType):
		self.___type = aType

	def getType(self) -> tSignalCatenaryType:
		return self.___type

	def setRefersToElectrificationSection(self, aRefersToElectrificationSection : tElementWithIDref):
		self._refersToElectrificationSection = aRefersToElectrificationSection

	def getRefersToElectrificationSection(self) -> tElementWithIDref:
		return self._refersToElectrificationSection

	def __init__(self):
		self.___type : tSignalCatenaryType = None
		# @AssociationType Infrastructure.tSignalCatenaryType
		self._refersToElectrificationSection : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to an electrification section"""

