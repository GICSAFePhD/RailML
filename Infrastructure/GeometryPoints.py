#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import GeometryPoint
from typing import List

class GeometryPoints(object):
	@property
	def GeometryPoint(self) -> GeometryPoint:
		return self.___geometryPoint
	
	@GeometryPoint.setter
	def GeometryPoint(self, aGeometryPoint : GeometryPoint):
		self.___geometryPoint = aGeometryPoint

	def __init__(self):
		self.___geometryPoint : GeometryPoint = GeometryPoint.GeometryPoint()
		# @AssociationType Infrastructure.GeometryPoint*
		# @AssociationMultiplicity 1..*

