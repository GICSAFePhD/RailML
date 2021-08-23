#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import LinearPositioningSystem
from typing import List

class LinearPositioningSystems(object):
	@property
	def LinearPositioningSystem(self) -> LinearPositioningSystem:
		return self.___linearPositioningSystem
	
	@LinearPositioningSystem.setter
	def LinearPositioningSystem(self, aLinearPositioningSystem : LinearPositioningSystem):
		self.___linearPositioningSystem = aLinearPositioningSystem

	def create_LinearPositioningSystem(self):
		if self.LinearPositioningSystem == None:
			self.LinearPositioningSystem = []
		self.LinearPositioningSystem.append(LinearPositioningSystem.LinearPositioningSystem())

	def __init__(self):
		self.___linearPositioningSystem : LinearPositioningSystem = None # It should be [LinearPositioningSystem.LinearPositioningSystem()] but it is better to behave as it was a 0..*
		# @AssociationType Infrastructure.RTM.RTM_LinearPositioningSystem*
		# @AssociationMultiplicity 1..*
		# Everytime <linearPositioningSystems> appears then a <linearPositioningSystem> exists, the 1..* is achieved even without the CORRECT definition

