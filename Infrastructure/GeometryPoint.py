#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM, tGradientPerMille, tAngleDeg
from RailML.Infrastructure import GeometryEntity
from typing import List

class GeometryPoint(GeometryEntity.GeometryEntity): 
	@property
	def Radius(self) -> tLengthM:
		return self.___radius
	@property
	def Gradient(self) -> tGradientPerMille:
		return self.___gradient
	@property
	def Azimuth(self) -> tAngleDeg:
		return self.___azimuth

	@Radius.setter
	def Radius(self, aRadius : tLengthM):
		self.___radius = aRadius
	@Gradient.setter
	def Gradient(self, aGradient : tGradientPerMille):
		self.___gradient = aGradient
	@Azimuth.setter
	def Azimuth(self, aAzimuth : tAngleDeg):
		self.___azimuth = aAzimuth

	def create_Radius(self):
		self.Radius.append(tLengthM.tLengthM())
	def create_Gradient(self):
		self.Gradient.append(tGradientPerMille.tGradientPerMille())
	def create_Azimuth(self):
		self.Azimuth.append(tAngleDeg.tAngleDeg())

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