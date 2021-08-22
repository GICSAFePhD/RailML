#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import GeometricPositioningSystem
from typing import List

class GeometricPositioningSystems(object):
	@property
	def GeometricPositioningSystem(self) -> GeometricPositioningSystem:
		return self.___geometricPositioningSystem
	
	@GeometricPositioningSystem.setter
	def GeometricPositioningSystem(self, aGeometricPositioningSystem : GeometricPositioningSystem):
		self.___geometricPositioningSystem = aGeometricPositioningSystem

	def create_GeometricPositioningSystem(self):
		self.GeometricPositioningSystem.append(GeometricPositioningSystem.GeometricPositioningSystem())

	def __init__(self):
		self.___geometricPositioningSystem : GeometricPositioningSystem = [GeometricPositioningSystem.GeometricPositioningSystem()]
		# @AssociationType Infrastructure.RTM.RTM_GeometricPositioningSystem*
		# @AssociationMultiplicity 1..*

