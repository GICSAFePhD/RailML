#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import TrainProtectionElement
from typing import List

class TrainProtectionElements(object):
	def setTrainProtectionElement(self, *aTrainProtectionElement : TrainProtectionElement*):
		self._trainProtectionElement = aTrainProtectionElement

	def getTrainProtectionElement(self) -> TrainProtectionElement*:
		return self._trainProtectionElement

	def __init__(self):
		self._trainProtectionElement : TrainProtectionElement = None
		# @AssociationType Infrastructure.TrainProtectionElement*
		# @AssociationMultiplicity 0..*

