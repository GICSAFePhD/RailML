#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tElementWithIDref
from Infrastructure import SignalX
from typing import List

class SignalStopPost(SignalX):
	def setRefersToStoppingPlace(self, aRefersToStoppingPlace : tElementWithIDref):
		self._refersToStoppingPlace = aRefersToStoppingPlace

	def getRefersToStoppingPlace(self) -> tElementWithIDref:
		return self._refersToStoppingPlace

	def __init__(self):
		self._refersToStoppingPlace : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 0..1
		# """reference to the stoppingPlace"""

