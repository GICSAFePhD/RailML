#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tHorizontalCurveTypeExt
from Common import tAngleDeg
from Common import tLengthM
from Infrastructure import GeometryCurve
from typing import List

class HorizontalCurve(GeometryCurve):
	def setCurveType(self, aCurveType : tHorizontalCurveTypeExt):
		self.___curveType = aCurveType

	def getCurveType(self) -> tHorizontalCurveTypeExt:
		return self.___curveType

	def setAzimuth(self, aAzimuth : tAngleDeg):
		self.___azimuth = aAzimuth

	def getAzimuth(self) -> tAngleDeg:
		return self.___azimuth

	def setDeltaAzimuth(self, aDeltaAzimuth : tAngleDeg):
		self.___deltaAzimuth = aDeltaAzimuth

	def getDeltaAzimuth(self) -> tAngleDeg:
		return self.___deltaAzimuth

	def setRadius(self, aRadius : tLengthM):
		self.___radius = aRadius

	def getRadius(self) -> tLengthM:
		return self.___radius

	def setLength(self, aLength : tLengthM):
		self.___length = aLength

	def getLength(self) -> tLengthM:
		return self.___length

	def __init__(self):
		self.___curveType : tHorizontalCurveTypeExt = None
		# @AssociationType Infrastructure.tHorizontalCurveTypeExt
		# """type of the horizontal curve, e.g. arc or clothoide or straight"""
		self.___azimuth : tAngleDeg = None
		"""constant azimuth (direction angle) of the horizontal curve in degrees;
		Direction "north" has an azimuth of 0 degrees, "east" 90, "south" 180 and "west" 270 degrees."""
		self.___deltaAzimuth : tAngleDeg = None
		# @AssociationType Common.tAngleDeg
		# @AssociationType Common.tAngleDeg
		# """change of azimuth of the horizontal curve in degrees;
		# use this attribute if the azimuth of the horizontal curve is not constant, but changing;
		# delta azimuth shall be calculated as difference of azimuth value at the end and the azimuth value at the beginning of the horizontal curve."""
		self.___radius : tLengthM = None
		"""radius of the horizontal curve in meters;
		use value "0" (zero) to describe straight curves with infinite radius;
		use negative values to describe a horizontal curve going to the left (as seen from begin of curve) and use positive values to describe a horizontal curve going to the right (as seen from begin of curve)"""
		self.___length : tLengthM = None
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """length of the horizontal curve in metres;
		# for arcs and transition curves (e.g. clothoides) this attribute defines the arc length"""

