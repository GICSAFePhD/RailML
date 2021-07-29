#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tSignalCatenaryType, SignalX
from typing import List

class SignalCatenary(SignalX.SignalX):
	@property
	def Type(self) -> tSignalCatenaryType:
		return self.___type
	@property
	def RefersToElectrificationSection(self) -> tElementWithIDref:
		return self.___refersToElectrificationSection
	
	@Type.setter
	def Type(self, aType : tSignalCatenaryType):
		self.___type = aType
	@RefersToElectrificationSection.setter
	def RefersToElectrificationSection(self, aRefersToElectrificationSection : tElementWithIDref):
		self.___refersToElectrificationSection = aRefersToElectrificationSection

	def __init__(self):
		self.___type : tSignalCatenaryType = tSignalCatenaryType.tSignalCatenaryType()
		# @AssociationType Infrastructure.tSignalCatenaryType
		self.___refersToElectrificationSection : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to an electrification section"""

