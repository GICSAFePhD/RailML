#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import SignalX
from typing import List

class SignalRadio(SignalX.SignalX):
	@property
	def RefersToTrainRadioSection(self) -> tElementWithIDref:
		return self.___refersToTrainRadioSection
	
	@RefersToTrainRadioSection.setter
	def RefersToTrainRadioSection(self, aRefersToTrainRadioSection : tElementWithIDref):
		self.___refersToTrainRadioSection = aRefersToTrainRadioSection

	def __init__(self):
		self.___refersToTrainRadioSection : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*

