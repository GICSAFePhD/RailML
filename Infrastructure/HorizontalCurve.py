#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tAngleDeg, tLengthM
from RailML.Infrastructure import tHorizontalCurveTypeExt, GeometryCurve
from typing import List

class HorizontalCurve(GeometryCurve.GeometryCurve):  
	@property
	def CurveType(self) -> tHorizontalCurveTypeExt:
		return self.___curveType
	@property
	def Azimuth(self) -> tAngleDeg:
		return self.___azimuth
	@property
	def DeltaAzimuth(self) -> tAngleDeg:
		return self.___deltaAzimuth
	@property
	def Radius(self) -> tLengthM:
		return self.___radius
	@property
	def Length(self) -> tLengthM:
		return self.___length

	@CurveType.setter
	def CurveType(self, atHorizontalCurveTypeExt : tHorizontalCurveTypeExt):
		self.___curveType = atHorizontalCurveTypeExt
	@Azimuth.setter
	def Azimuth(self, atAngleDeg : tAngleDeg):
		self.___azimuth = atAngleDeg
	@DeltaAzimuth.setter
	def DeltaAzimuth(self, atAngleDeg : tAngleDeg):
		self.___deltaAzimuth = atAngleDeg
	@Radius.setter
	def Radius(self, atLengthM : tLengthM):
		self.___radius = atLengthM
	@Length.setter
	def Length(self, atLengthM : tLengthM):
		self.___length = atLengthM
  
	def __init__(self):
		self.___curveType : tHorizontalCurveTypeExt = tHorizontalCurveTypeExt.tHorizontalCurveTypeExt()
		# @AssociationType Infrastructure.tHorizontalCurveTypeExt
		# """type of the horizontal curve, e.g. arc or clothoide or straight"""
		self.___azimuth : tAngleDeg = tAngleDeg.tAngleDeg()
		"""constant azimuth (direction angle) of the horizontal curve in degrees;
		Direction "north" has an azimuth of 0 degrees, "east" 90, "south" 180 and "west" 270 degrees."""
		self.___deltaAzimuth : tAngleDeg = tAngleDeg.tAngleDeg()
		# @AssociationType Common.tAngleDeg
		# @AssociationType Common.tAngleDeg
		# """change of azimuth of the horizontal curve in degrees;
		# use this attribute if the azimuth of the horizontal curve is not constant, but changing;
		# delta azimuth shall be calculated as difference of azimuth value at the end and the azimuth value at the beginning of the horizontal curve."""
		self.___radius : tLengthM = tLengthM.tLengthM()
		"""radius of the horizontal curve in meters;
		use value "0" (zero) to describe straight curves with infinite radius;
		use negative values to describe a horizontal curve going to the left (as seen from begin of curve) and use positive values to describe a horizontal curve going to the right (as seen from begin of curve)"""
		self.___length : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """length of the horizontal curve in metres;
		# for arcs and transition curves (e.g. clothoides) this attribute defines the arc length"""

