#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tGradientPerMille, tLengthM
from RailML.Infrastructure import tGradientCurveType, GeometryCurve
from typing import List

class GradientCurve(GeometryCurve.GeometryCurve):  
	@property
	def CurveType(self) -> tGradientCurveType:
		return self.___curveType
	@property
	def Gradient(self) -> tGradientPerMille:
		return self.___gradient
	@property
	def DeltaGradient(self) -> tGradientPerMille:
		return self.___deltaGradient
	@property
	def Radius(self) -> tLengthM:
		return self.___radius
	@property
	def Length(self) -> tLengthM:
		return self.___length

	@CurveType.setter
	def CurveType(self, atGradientCurveType : tGradientCurveType):
		self.___curveType = atGradientCurveType
	@Gradient.setter
	def Gradient(self, atGradientPerMille : tGradientPerMille):
		self.___gradient = atGradientPerMille
	@DeltaGradient.setter
	def DeltaGradient(self, atGradientPerMille : tGradientPerMille):
		self.___deltaGradient = atGradientPerMille
	@Radius.setter
	def Radius(self, atLengthM : tLengthM):
		self.___radius = atLengthM
	@Length.setter
	def Length(self, atLengthM : tLengthM):
		self.___length = atLengthM
  
	def __init__(self):
		self.___curveType : tGradientCurveType = tGradientCurveType.tGradientCurveType()
		# @AssociationType Infrastructure.tGradientCurveType
		# """type of vertical curve, e.g. arc or straight"""
		self.___gradient : tGradientPerMille = tGradientPerMille.tGradientPerMille()
		"""constant gradient of the gradient curve in per million;
		positive values indicate an upward slope (rise), negative values indicate a downward slope (fall)"""
		self.___deltaGradient : tGradientPerMille = tGradientPerMille.tGradientPerMille()
		# @AssociationType Common.tGradientPerMille
		# @AssociationType Common.tGradientPerMille
		# """change of gradient of the gradient curve in per million;
		# use this attribute if the gradient value of the gradient curve is not constant, but changing;
		# the delta gradient shall be calculated as difference of gradient at the end and gradient at the beginning of the gradient curve"""
		self.___radius : tLengthM = tLengthM.tLengthM()
		"""radius of the gradient curve in metres;
		use negative values to describe the arc curve of a valley and use positive values to describe the arc curve of a hill"""
		self.___length : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """length of the gradient curve in metres;
		# use this attribute in particular to define the arc length"""

