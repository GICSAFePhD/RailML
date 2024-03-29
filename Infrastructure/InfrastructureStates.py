#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import InfrastructureState
from typing import List

class InfrastructureStates(object):
	@property
	def InfrastructureState(self) -> InfrastructureState:
		return self.___infrastructureState
	
	@InfrastructureState.setter
	def InfrastructureState(self, aInfrastructureState : InfrastructureState):	# *aInfrastructureState
		self.___infrastructureState = aInfrastructureState

	def create_InfrastructureState(self):
		if self.InfrastructureState == None:
			self.InfrastructureState = []
		self.InfrastructureState.append(InfrastructureState.InfrastructureState())
    
	def __init__(self):
		self.___infrastructureState : InfrastructureState = None
		# @AssociationType Infrastructure.InfrastructureState*
		# @AssociationMultiplicity 1..*
		# """state of (a part of) the functional infrastructure regarding its availability and usability"""