#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tLateralSide, tVerticalSide
from RailML.RailTopoModel import PositioningSystemCoordinate
from typing import List

class RTM_LinearCoordinate(PositioningSystemCoordinate.PositioningSystemCoordinate): 
	@property
	def LateralDistance(self) -> complex:
		return self.___lateralDistance
	@property
	def Measure(self) -> complex:
		return self.___measure
	@property
	def VerticalDistance(self) -> complex:
		return self.___verticalDistance
	@property
	def LateralSide(self) -> tLateralSide:
		return self.___lateralSide
	@property
	def VerticalSide(self) -> tVerticalSide:
		return self.___verticalSide

	@LateralDistance.setter
	def LateralDistance(self, aLateralDistance : complex):
		self.___lateralDistance = aLateralDistance
	@Measure.setter
	def Measure(self, aMeasure : complex):
		self.___measure = aMeasure
	@VerticalDistance.setter
	def VerticalDistance(self, aVerticalDistance : complex):
		self.___verticalDistance = aVerticalDistance
	@LateralSide.setter
	def LateralSide(self, aLateralSide : tLateralSide):
		self.___lateralSide = aLateralSide
	@VerticalSide.setter
	def VerticalSide(self, aVerticalSide : tVerticalSide):
		self.___verticalSide = aVerticalSide

	def create_LateralSide(self):
		if self.LateralSide == None:
			self.LateralSide = []
		self.LateralSide.append(tLateralSide.tLateralSide())
	def create_VerticalSide(self):
		if self.VerticalSide == None:
			self.VerticalSide = []
		self.VerticalSide.append(tVerticalSide.tVerticalSide())

	def __init__(self):
		self.___lateralDistance : complex = None
		"""absolute value of the lateral offset in unit specified by the referenced positioning system"""
		self.___measure : complex = None
		self.___verticalDistance : complex = None
		"""absolute value of the lateral offset in unit specified by the referenced positioning system"""
		self.___lateralSide : tLateralSide = None
		# @AssociationType schemas.3.1.tLateralSide
		# """lateral side (left or right) in relation to the topology NetElement (as seen in application direction)"""
		self.___verticalSide : tVerticalSide = None
		# @AssociationType schemas.3.1.tVerticalSide
		# """vertical side (above or under) in relation to the topology NetElement"""

