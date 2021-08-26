#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_LinearCoordinate, RTM_GeometricCoordinate, RTM_BaseObject
from typing import List

class RTM_IntrinsicCoordinate(RTM_BaseObject.RTM_BaseObject):
	@property
	def IntrinsicCoord(self) -> complex:
		return self.___intrinsicCoord
	@property
	def LinearCoordinate(self) -> RTM_LinearCoordinate:
		return self.___linearCoordinate
	@property
	def GeometricCoordinate(self) -> RTM_GeometricCoordinate:
		return self.___geometricCoordinate

	@IntrinsicCoord.setter
	def IntrinsicCoord(self, aIntrinsicCoord : complex):
		self.___intrinsicCoord = aIntrinsicCoord
	@LinearCoordinate.setter
	def LinearCoordinate(self, aLinearCoordinate : RTM_LinearCoordinate):
		self.___linearCoordinate = aLinearCoordinate
	@GeometricCoordinate.setter
	def GeometricCoordinate(self, aGeometricCoordinate : RTM_GeometricCoordinate):
		self.___geometricCoordinate = aGeometricCoordinate

	def create_LinearCoordinate(self):
		if self.LinearCoordinate == None:
			self.LinearCoordinate = []
		self.LinearCoordinate.append(RTM_LinearCoordinate.RTM_LinearCoordinate())
	def create_GeometricCoordinate(self):
		if self.GeometricCoordinate == None:
			self.GeometricCoordinate = []
		self.GeometricCoordinate.append(RTM_GeometricCoordinate.RTM_GeometricCoordinate())

	def __init__(self):
		self.___intrinsicCoord : complex = None
		self.___linearCoordinate : RTM_LinearCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate*
		# @AssociationMultiplicity 0..*
		self.___geometricCoordinate : RTM_GeometricCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate*
		# @AssociationMultiplicity 0..*

