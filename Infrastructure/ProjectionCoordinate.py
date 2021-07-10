#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class ProjectionCoordinate(object):
	def setX(self, aX : decimal):
		self.___x = aX

	def getX(self) -> decimal:
		return self.___x

	def setY(self, aY : decimal):
		self.___y = aY

	def getY(self) -> decimal:
		return self.___y

	def setZ(self, aZ : decimal):
		self.___z = aZ

	def getZ(self) -> decimal:
		return self.___z

	def __init__(self):
		self.___x : decimal = None
		self.___y : decimal = None
		self.___z : decimal = None

