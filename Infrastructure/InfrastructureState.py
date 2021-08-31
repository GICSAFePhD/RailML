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
	def ElementState(self, aElementState : ElementState): # TODO *aElementState
		self.___elementState = aElementState
	@ValidityTime.setter
	def ValidityTime(self, aValidityTime : Period): # TODO *aValidityTime
		self.___validityTime = aValidityTime

	def create_ElementState(self):
		if self.ElementState == None:
			self.ElementState = []
		self.ElementState.append(ElementState.ElementState())
	def create_ValidityTime(self):
		if self.ValidityTime == None:
			self.ValidityTime = []
		self.ValidityTime.append(Period.Period())

	def __init__(self):
		super().__init__()
		self.___value : tInfrastructureStateExt = None
		# @AssociationType Infrastructure.tInfrastructureStateExt
		# """railway infrastructure functional state, e.g. "operational""""
		self.___elementState : ElementState = None
		# @AssociationType Infrastructure.ElementState*
		# @AssociationMultiplicity 0..*
		# """list of infrastructure elements in a certain state that belong to this infrastructure state"""
		self.___validityTime : Period = None
		# @AssociationType Common.Period*
		# @AssociationMultiplicity 0..*
		# """list of time periods when the infrastructure state is valid"""