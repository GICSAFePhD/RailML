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
			self.LinearPositioningSystem.append(LinearPositioningSystem.LinearPositioningSystem())

	def __init__(self):
		self.___linearPositioningSystem : LinearPositioningSystem = [LinearPositioningSystem.LinearPositioningSystem()]
		# @AssociationType Infrastructure.RTM.RTM_LinearPositioningSystem*
		# @AssociationMultiplicity 1..*

