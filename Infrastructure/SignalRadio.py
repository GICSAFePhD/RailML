#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tElementWithIDref
from Infrastructure import SignalX
from typing import List

class SignalRadio(SignalX):
	def setRefersToTrainRadioSection(self, *aRefersToTrainRadioSection : tElementWithIDref*):
		self._refersToTrainRadioSection = aRefersToTrainRadioSection

	def getRefersToTrainRadioSection(self) -> tElementWithIDref*:
		return self._refersToTrainRadioSection

	def __init__(self):
		self._refersToTrainRadioSection : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*

