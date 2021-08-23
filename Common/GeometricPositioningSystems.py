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
		if self.GeometricPositioningSystem == None:
			self.GeometricPositioningSystem = []
		self.GeometricPositioningSystem.append(GeometricPositioningSystem.GeometricPositioningSystem())

	def __init__(self):
		self.___geometricPositioningSystem : GeometricPositioningSystem = None # It should be [GeometricPositioningSystem.GeometricPositioningSystem()] but it is better to behave as it was a 0..*
		# @AssociationType Infrastructure.RTM.RTM_GeometricPositioningSystem*
		# @AssociationMultiplicity 1..* ---> 
		# Everytime <geometricPositioningSystems> appears then a <geometricPositioningSystem> exists, the 1..* is achieved even without the CORRECT definition

