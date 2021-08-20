#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import InfrastructureState
from typing import List

class InfrastructureStates(object):
	@property
	def InfrastructureState(self) -> InfrastructureState:
		return self.___infrastructureState
	
	@InfrastructureState.setter
	def InfrastructureState(self, *aInfrastructureState : InfrastructureState):
		self.___infrastructureState = aInfrastructureState

	def __init__(self):
		self.___infrastructureState : InfrastructureState = None
		# @AssociationType Infrastructure.InfrastructureState*
		# @AssociationMultiplicity 1..*
		# """state of (a part of) the functional infrastructure regarding its availability and usability"""

