#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import InfrastructureState
from typing import List

class InfrastructureStates(object):
	def setInfrastructureState(self, *aInfrastructureState : InfrastructureState*):
		self._infrastructureState = aInfrastructureState

	def getInfrastructureState(self) -> InfrastructureState*:
		return self._infrastructureState

	def __init__(self):
		self._infrastructureState : InfrastructureState = None
		# @AssociationType Infrastructure.InfrastructureState*
		# @AssociationMultiplicity 1..*
		# """state of (a part of) the functional infrastructure regarding its availability and usability"""

