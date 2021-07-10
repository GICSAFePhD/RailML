#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tInfrastructureStateExt
from Infrastructure import ElementState
from Common import Period
from Infrastructure import StatesBaseElement
from typing import List

class InfrastructureState(StatesBaseElement):
	def setValue(self, aValue : tInfrastructureStateExt):
		self.___value = aValue

	def getValue(self) -> tInfrastructureStateExt:
		return self.___value

	def setElementState(self, *aElementState : ElementState*):
		self._elementState = aElementState

	def getElementState(self) -> ElementState*:
		return self._elementState

	def setValidityTime(self, *aValidityTime : Period*):
		self._validityTime = aValidityTime

	def getValidityTime(self) -> Period*:
		return self._validityTime

	def __init__(self):
		self.___value : tInfrastructureStateExt = None
		# @AssociationType Infrastructure.tInfrastructureStateExt
		# """railway infrastructure functional state, e.g. "operational""""
		self._elementState : ElementState = None
		# @AssociationType Infrastructure.ElementState*
		# @AssociationMultiplicity 0..*
		# """list of infrastructure elements in a certain state that belong to this infrastructure state"""
		self._validityTime : Period = None
		# @AssociationType Common.Period*
		# @AssociationMultiplicity 0..*
		# """list of time periods when the infrastructure state is valid"""

