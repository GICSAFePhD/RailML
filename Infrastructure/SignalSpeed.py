#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tSignalSpeedType, tTrainRelation, SignalX
from typing import List

class SignalSpeed(SignalX.SignalX):
	@property
	def tSignalSpeedType(self) -> tSignalSpeedType:
		return self.___type
	@property
	def tTrainRelation(self) -> tTrainRelation:
		return self.___trainRelation
	@property
	def RefersToBeginOfSpeedSection(self) -> tElementWithIDref:
		return self.___refersToBeginOfSpeedSection
	@property
	def RefersToEndOfSpeedSection(self) -> tElementWithIDref:
		return self.___refersToEndOfSpeedSection

	@tSignalSpeedType.setter
	def tSignalSpeedType(self, atSignalSpeedType : tSignalSpeedType):
		self.___type = atSignalSpeedType
	@tTrainRelation.setter
	def tTrainRelation(self, atTrainRelation : tTrainRelation):
		self.___trainRelation = atTrainRelation
	@RefersToBeginOfSpeedSection.setter
	def RefersToBeginOfSpeedSection(self, *aRefersToBeginOfSpeedSection : tElementWithIDref):
		self.___refersToBeginOfSpeedSection = aRefersToBeginOfSpeedSection
	@RefersToEndOfSpeedSection.setter
	def RefersToEndOfSpeedSection(self, *aRefersToEndOfSpeedSection : tElementWithIDref):
		self.___refersToEndOfSpeedSection = aRefersToEndOfSpeedSection

	def __init__(self):
		self.___type : tSignalSpeedType = tSignalSpeedType.tSignalSpeedType()
		# @AssociationType Infrastructure.tSignalSpeedType
		# """speed signal/panel type (announcement, execution)"""
		self.___trainRelation : tTrainRelation = tTrainRelation.tTrainRelation()
		# @AssociationType Infrastructure.tTrainRelation
		# """Reference to the part of the train from where on the shown speed signal aspect is valid. Normally, a limiting speed signal aspect relates to the head of the train while a speed release refers to the end of the train."""
		self.___refersToBeginOfSpeedSection : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		"""reference to the begin of a speedSection"""
		self.___refersToEndOfSpeedSection : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to the end of a speedSection"""

