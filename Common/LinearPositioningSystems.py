#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import RTM_LinearPositioningSystem
from typing import List

class LinearPositioningSystems(object):
	@property
	def RTM_LinearPositioningSystem(self) -> RTM_LinearPositioningSystem:
		return self.___linearPositioningSystem
	
	@RTM_LinearPositioningSystem.setter
	def RTM_LinearPositioningSystem(self, aRTM_LinearPositioningSystem : RTM_LinearPositioningSystem):
		self.___linearPositioningSystem = aRTM_LinearPositioningSystem

	def __init__(self):
		self.___linearPositioningSystem : RTM_LinearPositioningSystem = RTM_LinearPositioningSystem.RTM_LinearPositioningSystem()
		# @AssociationType Infrastructure.RTM.RTM_LinearPositioningSystem*
		# @AssociationMultiplicity 1..*

