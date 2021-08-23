#!/usr/bin/python
# -*- coding: UTF-8 -*-

#TODO THIS IS HOW TO SOLVE THE CIRCULAR IMPORT!
from RailML.Infrastructure import HorizontalCurves
from RailML.Infrastructure import GradientCurves
from RailML.Infrastructure import GeometryPoints

from typing import List

class Geometry(object):
	"""This is the top level element for railML3 geometry model."""

	@property
	def HorizontalCurves(self) -> HorizontalCurves:
		return self.___horizontalCurves
	@property
	def GradientCurves(self) -> GradientCurves:
		return self.___gradientCurves
	@property
	def GeometryPoints(self) -> GeometryPoints:
		return self.___geometryPoints

	@HorizontalCurves.setter
	def HorizontalCurves(self, aHorizontalCurves : HorizontalCurves):
		self.___horizontalCurves = aHorizontalCurves
	@GradientCurves.setter
	def GradientCurves(self, aGradientCurves : GradientCurves):
		self.___gradientCurves = aGradientCurves
	@GeometryPoints.setter
	def GeometryPoints(self, aGeometryPoints : GeometryPoints):
		self.___geometryPoints = aGeometryPoints

	def __init__(self):
		self.___horizontalCurves : HorizontalCurves = None#HorizontalCurves.HorizontalCurves()
		# @AssociationType Infrastructure.HorizontalCurves
		# @AssociationMultiplicity 0..1
		# """container element for all horizontalCurve elements"""
		self.___gradientCurves : GradientCurves = None#GradientCurves.GradientCurves()
		# @AssociationType Infrastructure.GradientCurves
		# @AssociationMultiplicity 0..1
		# """container element for all gradientCurve elements"""
		self.___geometryPoints : GeometryPoints = None#GeometryPoints.GeometryPoints()
		# @AssociationType Infrastructure.GeometryPoints
		# @AssociationMultiplicity 0..1
		# """container element for all geometryPoint elements"""
		self.___unnamed_any_ = None#[]	#TODO What is this?!
		"""# @AssociationMultiplicity 0..*"""
