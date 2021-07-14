#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.aTrainDetectionElement import aTrainDetectionElement
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class TrainDetectionElement(FunctionalInfrastructureEntity):
	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def setLimitsTrainDetectionElement(self, *aLimitsTrainDetectionElement : tElementWithIDref):
		self._limitsTrainDetectionElement = aLimitsTrainDetectionElement

	def getLimitsTrainDetectionElement(self) -> tElementWithIDref:
		return self._limitsTrainDetectionElement

	def __init__(self):
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# """reference to a template train detection element/system"""
		self._limitsTrainDetectionElement : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..2
		# """If the current <trainDetectionElement> is an insulated rail joint or an axle counter and thus a border between two <trainDetectionElement> objects, these two <trainDetectionElement> objects can be referenced."""
		self._unnamed_aTrainDetectionElement_ : aTrainDetectionElement = None

