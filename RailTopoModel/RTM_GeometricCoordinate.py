#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_PositioningSystemCoordinate
from typing import List

#class RTM_GeometricCoordinate(RTM_PositioningSystemCoordinate): # NO SE XQ CON ESTA HERENCIA SE ROMPE
class RTM_GeometricCoordinate():    
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
		self.___x : complex = None
		self.___y : complex = None
		self.___z : complex = None

