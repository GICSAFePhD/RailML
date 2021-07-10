#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import HorizontalCurves
from Infrastructure import GradientCurves
from Infrastructure import GeometryPoints
from typing import List

class Geometry(object):
	"""This is the top level element for railML3 geometry model."""
	def setHorizontalCurves(self, aHorizontalCurves : HorizontalCurves):
		self._horizontalCurves = aHorizontalCurves

	def getHorizontalCurves(self) -> HorizontalCurves:
		return self._horizontalCurves

	def setGradientCurves(self, aGradientCurves : GradientCurves):
		self._gradientCurves = aGradientCurves

	def getGradientCurves(self) -> GradientCurves:
		return self._gradientCurves

	def setGeometryPoints(self, aGeometryPoints : GeometryPoints):
		self._geometryPoints = aGeometryPoints

	def getGeometryPoints(self) -> GeometryPoints:
		return self._geometryPoints

	def __init__(self):
		self._horizontalCurves : HorizontalCurves = None
		# @AssociationType Infrastructure.HorizontalCurves
		# @AssociationMultiplicity 0..1
		# """container element for all horizontalCurve elements"""
		self._gradientCurves : GradientCurves = None
		# @AssociationType Infrastructure.GradientCurves
		# @AssociationMultiplicity 0..1
		# """container element for all gradientCurve elements"""
		self._geometryPoints : GeometryPoints = None
		# @AssociationType Infrastructure.GeometryPoints
		# @AssociationMultiplicity 0..1
		# """container element for all geometryPoint elements"""
		self._unnamed_any_ = []
		"""# @AssociationMultiplicity 0..*"""

