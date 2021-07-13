#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.RTM_GeometricPositioningSystem import RTM_GeometricPositioningSystem
from typing import List

class GeometricPositioningSystems(object):
	def setGeometricPositioningSystem(self, aGeometricPositioningSystem : RTM_GeometricPositioningSystem):
		self._geometricPositioningSystem = aGeometricPositioningSystem

	def getGeometricPositioningSystem(self) -> RTM_GeometricPositioningSystem:
		return self._geometricPositioningSystem

	def __init__(self):
		self._geometricPositioningSystem : RTM_GeometricPositioningSystem = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricPositioningSystem*
		# @AssociationMultiplicity 1..*

