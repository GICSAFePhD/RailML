#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List, NewType
Decimal = NewType("Decimal", int)

class ProjectionCoordinate(object):
	@property
	def X(self) -> Decimal:
		return self.___x
	@property
	def Y(self) -> Decimal:
		return self.___y
	@property
	def Z(self) -> Decimal:
		return self.___z

	@X.setter
	def X(self, aX : Decimal):
		self.___x = aX
	@Y.setter
	def Y(self, aY : Decimal):
		self.___y = aY
	@Z.setter
	def Z(self, aZ : Decimal):
		self.___z = aZ

	def __init__(self):
		self.___x : Decimal = 0
		self.___y : Decimal = 0
		self.___z : Decimal = 0

