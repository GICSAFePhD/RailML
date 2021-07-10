#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tGradientCurveType
from Common import tGradientPerMille
from Common import tLengthM
from Infrastructure import GeometryCurve
from typing import List

class GradientCurve(GeometryCurve):
	def setCurveType(self, aCurveType : tGradientCurveType):
		self.___curveType = aCurveType

	def getCurveType(self) -> tGradientCurveType:
		return self.___curveType

	def setGradient(self, aGradient : tGradientPerMille):
		self.___gradient = aGradient

	def getGradient(self) -> tGradientPerMille:
		return self.___gradient

	def setDeltaGradient(self, aDeltaGradient : tGradientPerMille):
		self.___deltaGradient = aDeltaGradient

	def getDeltaGradient(self) -> tGradientPerMille:
		return self.___deltaGradient

	def setRadius(self, aRadius : tLengthM):
		self.___radius = aRadius

	def getRadius(self) -> tLengthM:
		return self.___radius

	def setLength(self, aLength : tLengthM):
		self.___length = aLength

	def getLength(self) -> tLengthM:
		return self.___length

	def __init__(self):
		self.___curveType : tGradientCurveType = None
		# @AssociationType Infrastructure.tGradientCurveType
		# """type of vertical curve, e.g. arc or straight"""
		self.___gradient : tGradientPerMille = None
		"""constant gradient of the gradient curve in per million;
		positive values indicate an upward slope (rise), negative values indicate a downward slope (fall)"""
		self.___deltaGradient : tGradientPerMille = None
		# @AssociationType Common.tGradientPerMille
		# @AssociationType Common.tGradientPerMille
		# """change of gradient of the gradient curve in per million;
		# use this attribute if the gradient value of the gradient curve is not constant, but changing;
		# the delta gradient shall be calculated as difference of gradient at the end and gradient at the beginning of the gradient curve"""
		self.___radius : tLengthM = None
		"""radius of the gradient curve in metres;
		use negative values to describe the arc curve of a valley and use positive values to describe the arc curve of a hill"""
		self.___length : tLengthM = None
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """length of the gradient curve in metres;
		# use this attribute in particular to define the arc length"""

