#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Infrastructure.aTrainProtection import aTrainProtection
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class TrainProtectionElement(FunctionalInfrastructureEntity):
	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def __init__(self):
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# """reference to a template train protection element/system"""
		self._unnamed_aTrainProtection_ : aTrainProtection = None

