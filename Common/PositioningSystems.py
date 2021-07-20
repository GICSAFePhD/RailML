#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.GeometricPositioningSystems import GeometricPositioningSystems
from RailML.Common.LinearPositioningSystems import LinearPositioningSystems
from RailML.Common.ScreenPositioningSystems import ScreenPositioningSystems
from typing import List

class PositioningSystems(object):
	"""This is the top level element for railML3 positioning and coordinate systems model."""
	@property
	def GeometricPositioningSystems(self) -> GeometricPositioningSystems:
		return self.___geometricPositioningSystems
	@property
	def LinearPositioningSystems(self) -> LinearPositioningSystems:
		return self.___linearPositioningSystems
	@property
	def ScreenPositioningSystems(self) -> ScreenPositioningSystems:
		return self.___screenPositioningSystems

	@GeometricPositioningSystems.setter
	def GeometricPositioningSystems(self, aGeometricPositioningSystems : GeometricPositioningSystems):
		self.___geometricPositioningSystems = aGeometricPositioningSystems
	@LinearPositioningSystems.setter
	def LinearPositioningSystems(self, aLinearPositioningSystems : LinearPositioningSystems):
		self.___linearPositioningSystems = aLinearPositioningSystems
	@ScreenPositioningSystems.setter
	def ScreenPositioningSystems(self, aScreenPositioningSystems : ScreenPositioningSystems):
		self.___screenPositioningSystems = aScreenPositioningSystems

	def __init__(self):
		self.___geometricPositioningSystems : GeometricPositioningSystems = GeometricPositioningSystems()
		# @AssociationType Common.GeometricPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all geometric positioning systems"""
		self.___linearPositioningSystems : LinearPositioningSystems = LinearPositioningSystems()
		# @AssociationType Common.LinearPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all linear positioning systems"""
		self.___screenPositioningSystems : ScreenPositioningSystems = ScreenPositioningSystems()
		# @AssociationType Common.ScreenPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all screen coordinate systems"""

