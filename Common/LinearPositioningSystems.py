#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.RTM_LinearPositioningSystem import RTM_LinearPositioningSystem
from typing import List

class LinearPositioningSystems(object):
	def setLinearPositioningSystem(self, aLinearPositioningSystem : RTM_LinearPositioningSystem):
		self._linearPositioningSystem = aLinearPositioningSystem

	def getLinearPositioningSystem(self) -> RTM_LinearPositioningSystem:
		return self._linearPositioningSystem

	def __init__(self):
		self._linearPositioningSystem : RTM_LinearPositioningSystem = None
		# @AssociationType Infrastructure.RTM.RTM_LinearPositioningSystem*
		# @AssociationMultiplicity 1..*

