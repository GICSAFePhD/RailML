#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import PositioningSystemCoordinate
from typing import List

class GeometricCoordinate(PositioningSystemCoordinate.PositioningSystemCoordinate):
	@property
	def X(self) -> complex:
		return self.___x
	@property
	def Y(self) -> complex:
		return self.___y
	@property
	def Z(self) -> complex:
		return self.___z

	@X.setter
	def X(self, aX : complex):
		self.___x = aX
	@Y.setter
	def Y(self, aY : complex):
		self.___y = aY
	@Z.setter
	def Z(self, aZ : complex):
		self.___z = aZ
    
	def __init__(self):
		super().__init__()
		self.___x : complex = None
		self.___y : complex = None
		self.___z : complex = None