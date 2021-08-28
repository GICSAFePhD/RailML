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

	def create_GeometryPoint(self):
		if self.GeometryPoint == None:
			self.GeometryPoint = []
		self.GeometryPoint.append(GeometryPoint.GeometryPoint())

	def __init__(self):
		self.___geometryPoint : GeometryPoint = None
		# @AssociationType Infrastructure.GeometryPoint*
		# @AssociationMultiplicity 1..*

