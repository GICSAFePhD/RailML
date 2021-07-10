#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tRef
from Infrastructure import tInfrastructureStateExt
from Common import Period
from Infrastructure import StatesBaseElement
from typing import List

class ElementState(StatesBaseElement):
	def setRefersToElement(self, aRefersToElement : tRef):
		self.___refersToElement = aRefersToElement

	def getRefersToElement(self) -> tRef:
		return self.___refersToElement

	def setValue(self, aValue : tInfrastructureStateExt):
		self.___value = aValue

	def getValue(self) -> tInfrastructureStateExt:
		return self.___value

	def setValidityTime(self, *aValidityTime : Period*):
		self._validityTime = aValidityTime

	def getValidityTime(self) -> Period*:
		return self._validityTime

	def __init__(self):
		self.___refersToElement : tRef = None
		# @AssociationType Common.tRef
		# """reference to any element of infrastructure model"""
		self.___value : tInfrastructureStateExt = None
		# @AssociationType Infrastructure.tInfrastructureStateExt
		# """railway infrastructure element functional state, e.g. "operational""""
		self._validityTime : Period = None
		# @AssociationType Common.Period*
		# @AssociationMultiplicity 0..*
		# """list of time periods when the infrastructure element state is valid; there should be at least some overlap with the infrastructure state validity time"""

