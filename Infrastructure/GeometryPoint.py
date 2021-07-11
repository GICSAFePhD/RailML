#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM, tGradientPerMille, tAngleDeg
from RailML.Infrastructure import GeometryEntity
from typing import List

#class GeometryPoint(GeometryEntity): #TODO CON ESTA HERENCIA SE ROMPE
class GeometryPoint():
	def setRadius(self, aRadius : tLengthM):
		self.___radius = aRadius

	def getRadius(self) -> tLengthM:
		return self.___radius

	def setGradient(self, aGradient : tGradientPerMille):
		self.___gradient = aGradient

	def getGradient(self) -> tGradientPerMille:
		return self.___gradient

	def setAzimuth(self, aAzimuth : tAngleDeg):
		self.___azimuth = aAzimuth

	def getAzimuth(self) -> tAngleDeg:
		return self.___azimuth

	def __init__(self):
		self.___radius : tLengthM = None
		# @AssociationType Common.tLengthM
		# """radius in metres
		# use value "0" (zero) to describe a point that is located in a straight curve with infinite radius;
		# use negative values to describe a horizontal curve going to the left (as seen according application direction) and use positive values to describe a horizontal curve going to the right (as seen according application direction)"""
		self.___gradient : tGradientPerMille = None
		# @AssociationType Common.tGradientPerMille
		# """gradient in per million"""
		self.___azimuth : tAngleDeg = None
		# @AssociationType Common.tAngleDeg
		# """azimuth in degrees"""

