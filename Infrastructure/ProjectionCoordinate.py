#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class ProjectionCoordinate(object):
	def setX(self, aX : int):	#TODO DEFINED AS DECIMAL
		self.___x = aX

	def getX(self) -> int:	#TODO DEFINED AS DECIMAL
		return self.___x

	def setY(self, aY : int):	#TODO DEFINED AS DECIMAL
		self.___y = aY

	def getY(self) -> int:	#TODO DEFINED AS DECIMAL
		return self.___y

	def setZ(self, aZ : int):	#TODO DEFINED AS DECIMAL
		self.___z = aZ

	def getZ(self) -> int:	#TODO DEFINED AS DECIMAL
		return self.___z

	def __init__(self):
		self.___x : int = None	#TODO DEFINED AS DECIMAL
		self.___y : int = None	#TODO DEFINED AS DECIMAL
		self.___z : int = None	#TODO DEFINED AS DECIMAL

