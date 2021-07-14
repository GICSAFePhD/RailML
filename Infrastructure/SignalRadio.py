#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.SignalX import SignalX
from typing import List

class SignalRadio(SignalX):
	def setRefersToTrainRadioSection(self, *aRefersToTrainRadioSection : tElementWithIDref):
		self._refersToTrainRadioSection = aRefersToTrainRadioSection

	def getRefersToTrainRadioSection(self) -> tElementWithIDref:
		return self._refersToTrainRadioSection

	def __init__(self):
		self._refersToTrainRadioSection : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*

