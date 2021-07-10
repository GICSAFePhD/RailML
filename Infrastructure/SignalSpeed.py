#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tSignalSpeedType
from Infrastructure import tTrainRelation
from Common import tElementWithIDref
from Infrastructure import SignalX
from typing import List

class SignalSpeed(SignalX):
	def setType(self, aType : tSignalSpeedType):
		self.___type = aType

	def getType(self) -> tSignalSpeedType:
		return self.___type

	def setTrainRelation(self, aTrainRelation : tTrainRelation):
		self.___trainRelation = aTrainRelation

	def getTrainRelation(self) -> tTrainRelation:
		return self.___trainRelation

	def setRefersToBeginOfSpeedSection(self, *aRefersToBeginOfSpeedSection : tElementWithIDref*):
		self._refersToBeginOfSpeedSection = aRefersToBeginOfSpeedSection

	def getRefersToBeginOfSpeedSection(self) -> tElementWithIDref*:
		return self._refersToBeginOfSpeedSection

	def setRefersToEndOfSpeedSection(self, *aRefersToEndOfSpeedSection : tElementWithIDref*):
		self._refersToEndOfSpeedSection = aRefersToEndOfSpeedSection

	def getRefersToEndOfSpeedSection(self) -> tElementWithIDref*:
		return self._refersToEndOfSpeedSection

	def __init__(self):
		self.___type : tSignalSpeedType = None
		# @AssociationType Infrastructure.tSignalSpeedType
		# """speed signal/panel type (announcement, execution)"""
		self.___trainRelation : tTrainRelation = None
		# @AssociationType Infrastructure.tTrainRelation
		# """Reference to the part of the train from where on the shown speed signal aspect is valid. Normally, a limiting speed signal aspect relates to the head of the train while a speed release refers to the end of the train."""
		self._refersToBeginOfSpeedSection : tElementWithIDref = None
		"""reference to the begin of a speedSection"""
		self._refersToEndOfSpeedSection : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to the end of a speedSection"""

