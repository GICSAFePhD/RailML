#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import RTM_GeometricPositioningSystem
from typing import List

class GeometricPositioningSystems(object):
	@property
	def RTM_GeometricPositioningSystem(self) -> RTM_GeometricPositioningSystem:
		return self.___geometricPositioningSystem
	
	@RTM_GeometricPositioningSystem.setter
	def RTM_GeometricPositioningSystem(self, aRTM_GeometricPositioningSystem : RTM_GeometricPositioningSystem):
		self.___geometricPositioningSystem = aRTM_GeometricPositioningSystem

	def __init__(self):
		self.___geometricPositioningSystem : RTM_GeometricPositioningSystem = RTM_GeometricPositioningSystem.RTM_GeometricPositioningSystem()
		# @AssociationType Infrastructure.RTM.RTM_GeometricPositioningSystem*
		# @AssociationMultiplicity 1..*

