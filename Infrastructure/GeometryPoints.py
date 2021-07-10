#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import GeometryPoint
from typing import List

class GeometryPoints(object):
	def setGeometryPoint(self, *aGeometryPoint : GeometryPoint*):
		self._geometryPoint = aGeometryPoint

	def getGeometryPoint(self) -> GeometryPoint*:
		return self._geometryPoint

	def __init__(self):
		self._geometryPoint : GeometryPoint = None
		# @AssociationType Infrastructure.GeometryPoint*
		# @AssociationMultiplicity 1..*

