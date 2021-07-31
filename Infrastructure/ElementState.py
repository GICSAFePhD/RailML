#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, Period
from RailML.Infrastructure import tInfrastructureStateExt, StatesBaseElement
from typing import List

class ElementState(StatesBaseElement.StatesBaseElement):
	@property
	def RefersToElement(self) -> tRef:
		return self.___refersToElement
	@property
	def Value(self) -> tInfrastructureStateExt:
		return self.___value
	@property
	def ValidityTime(self) -> Period:
		return self.___validityTime

	@RefersToElement.setter
	def RefersToElement(self, aRefersToElement : tRef):
		self.___refersToElement = aRefersToElement
	@Value.setter
	def Value(self, aValue : tInfrastructureStateExt):
		self.___value = aValue
	@ValidityTime.setter
	def ValidityTime(self, *aValidityTime : Period):
		self.___validityTime = aValidityTime

	def __init__(self):
		self.___refersToElement : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# """reference to any element of infrastructure model"""
		self.___value : tInfrastructureStateExt = tInfrastructureStateExt.tInfrastructureStateExt()
		# @AssociationType Infrastructure.tInfrastructureStateExt
		# """railway infrastructure element functional state, e.g. "operational""""
		self.___validityTime : Period = Period.Period()
		# @AssociationType Common.Period*
		# @AssociationMultiplicity 0..*
		# """list of time periods when the infrastructure element state is valid; there should be at least some overlap with the infrastructure state validity time"""

