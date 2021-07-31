#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import Period
from RailML.Infrastructure import tInfrastructureStateExt, ElementState, StatesBaseElement
from typing import List

class InfrastructureState(StatesBaseElement.StatesBaseElement):
	@property
	def Value(self) -> tInfrastructureStateExt:
		return self.___value
	@property
	def ElementState(self) -> ElementState:
		return self.___elementState
	@property
	def ValidityTime(self) -> Period:
		return self.___validityTime

	@Value.setter
	def Value(self, aValue : tInfrastructureStateExt):
		self.___value = aValue
	@ElementState.setter
	def ElementState(self, *aElementState : ElementState):
		self.___elementState = aElementState
	@ValidityTime.setter
	def ValidityTime(self, *aValidityTime : Period):
		self.___validityTime = aValidityTime

	def __init__(self):
		self.___value : tInfrastructureStateExt = tInfrastructureStateExt.tInfrastructureStateExt()
		# @AssociationType Infrastructure.tInfrastructureStateExt
		# """railway infrastructure functional state, e.g. "operational""""
		self.___elementState : ElementState = ElementState.ElementState()
		# @AssociationType Infrastructure.ElementState*
		# @AssociationMultiplicity 0..*
		# """list of infrastructure elements in a certain state that belong to this infrastructure state"""
		self.___validityTime : Period = Period.Period()
		# @AssociationType Common.Period*
		# @AssociationMultiplicity 0..*
		# """list of time periods when the infrastructure state is valid"""

