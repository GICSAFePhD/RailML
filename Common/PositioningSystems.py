#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.GeometricPositioningSystems import GeometricPositioningSystems
from RailML.Common.LinearPositioningSystems import LinearPositioningSystems
from RailML.Common.ScreenPositioningSystems import ScreenPositioningSystems
from typing import List

class PositioningSystems(object):
	"""This is the top level element for railML3 positioning and coordinate systems model."""
	def setGeometricPositioningSystems(self, aGeometricPositioningSystems : GeometricPositioningSystems):
		self._geometricPositioningSystems = aGeometricPositioningSystems

	def getGeometricPositioningSystems(self) -> GeometricPositioningSystems:
		return self._geometricPositioningSystems

	def setLinearPositioningSystems(self, aLinearPositioningSystems : LinearPositioningSystems):
		self._linearPositioningSystems = aLinearPositioningSystems

	def getLinearPositioningSystems(self) -> LinearPositioningSystems:
		return self._linearPositioningSystems

	def setScreenPositioningSystems(self, aScreenPositioningSystems : ScreenPositioningSystems):
		self._screenPositioningSystems = aScreenPositioningSystems

	def getScreenPositioningSystems(self) -> ScreenPositioningSystems:
		return self._screenPositioningSystems

	def __init__(self):
		self._geometricPositioningSystems : GeometricPositioningSystems = None
		# @AssociationType Common.GeometricPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all geometric positioning systems"""
		self._linearPositioningSystems : LinearPositioningSystems = None
		# @AssociationType Common.LinearPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all linear positioning systems"""
		self._screenPositioningSystems : ScreenPositioningSystems = None
		# @AssociationType Common.ScreenPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all screen coordinate systems"""

