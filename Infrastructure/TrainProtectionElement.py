#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.Infrastructure import aTrainProtection, FunctionalInfrastructureEntity
from typing import List

class TrainProtectionElement(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def Unnamed_aTrainProtection(self) -> aTrainProtection:
		return self.___unnamed_aTrainProtection

	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@Unnamed_aTrainProtection.setter
	def Unnamed_aTrainProtection(self, aUnnamed_aTrainProtection : aTrainProtection):
		self.___unnamed_aTrainProtection = aUnnamed_aTrainProtection

	def __init__(self):
		self.___basedOnTemplate : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# """reference to a template train protection element/system"""
		self.___unnamed_aTrainProtection : aTrainProtection = aTrainProtection.aTrainProtection()

