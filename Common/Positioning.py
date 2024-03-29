#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import GeometricPositioningSystems, LinearPositioningSystems, ScreenPositioningSystems
from typing import List

class Positioning(object):
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

	def create_GeometricPositioningSystems(self):
		self.GeometricPositioningSystems = GeometricPositioningSystems.GeometricPositioningSystems()
	def create_LinearPositioningSystems(self):
		self.LinearPositioningSystems = LinearPositioningSystems.LinearPositioningSystems()
	def create_ScreenPositioningSystems(self):
		self.ScreenPositioningSystems = ScreenPositioningSystems.ScreenPositioningSystems()

	def __init__(self):
		self.___geometricPositioningSystems : GeometricPositioningSystems = None
		# @AssociationType Common.GeometricPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all geometric positioning systems"""
		self.___linearPositioningSystems : LinearPositioningSystems = None
		# @AssociationType Common.LinearPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all linear positioning systems"""
		self.___screenPositioningSystems : ScreenPositioningSystems = None
		# @AssociationType Common.ScreenPositioningSystems
		# @AssociationMultiplicity 0..1
		# """container element for all screen coordinate systems"""

