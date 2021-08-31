#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef,  tElementWithIDref
from RailML.Infrastructure import aTrainDetectionElement, FunctionalInfrastructureEntity
from typing import List

class TrainDetectionElement(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def LimitsTrainDetectionElement(self) -> tElementWithIDref:
		return self.___limitsTrainDetectionElement
	@property
	def Unnamed_aTrainDetectionElement(self) -> aTrainDetectionElement:
		return self.___unnamed_aTrainDetectionElement
	
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@LimitsTrainDetectionElement.setter
	def LimitsTrainDetectionElement(self, *aLimitsTrainDetectionElement : tElementWithIDref):
		self.___limitsTrainDetectionElement = aLimitsTrainDetectionElement
	@Unnamed_aTrainDetectionElement.setter
	def Unnamed_aTrainDetectionElement(self, aUnnamed_aTrainDetectionElement : aTrainDetectionElement):
		self.___unnamed_aTrainDetectionElement = aUnnamed_aTrainDetectionElement

	def __init__(self):
		super().__init__()
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# """reference to a template train detection element/system"""
		self.___limitsTrainDetectionElement : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..2
		# """If the current <trainDetectionElement> is an insulated rail joint or an axle counter and thus a border between two <trainDetectionElement> objects, these two <trainDetectionElement> objects can be referenced."""
		self.___unnamed_aTrainDetectionElement : aTrainDetectionElement = None