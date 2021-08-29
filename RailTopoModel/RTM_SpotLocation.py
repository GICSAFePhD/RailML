#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tLengthM
from RailML.Infrastructure import tApplicationDirection
from RailML.RailTopoModel import RTM_LinearCoordinate, RTM_GeometricCoordinate, RTM_EntityLocation
from typing import List

class RTM_SpotLocation(RTM_EntityLocation.RTM_EntityLocation):
	@property
	def NetElementRef(self) -> tRef:
		return self.___netElementRef
	@property
	def IntrinsicCoord(self) -> complex:
		return self.___intrinsicCoord
	@property
	def ApplicationDirection(self) -> tApplicationDirection:
		return self.___applicationDirection
	@property
	def Pos(self) -> tLengthM:
		return self.___pos
	@property
	def LinearCoordinate(self) -> RTM_LinearCoordinate:
		return self.___linearCoordinate
	@property
	def GeometricCoordinate(self) -> RTM_GeometricCoordinate:
		return self.___geometricCoordinate

	@NetElementRef.setter
	def NetElementRef(self, aNetElementRef : tRef):
		self.___netElementRef = aNetElementRef
	@IntrinsicCoord.setter
	def IntrinsicCoord(self, aIntrinsicCoord : complex):
		self.___intrinsicCoord = aIntrinsicCoord
	@ApplicationDirection.setter
	def ApplicationDirection(self, aApplicationDirection : tApplicationDirection):
		self.___applicationDirection = aApplicationDirection
	@Pos.setter
	def Pos(self, aPos : tLengthM):
		self.___pos = aPos
	@LinearCoordinate.setter
	def LinearCoordinate(self, aLinearCoordinate : RTM_LinearCoordinate):
		self.___linearCoordinate = aLinearCoordinate
	@GeometricCoordinate.setter
	def GeometricCoordinate(self, aGeometricCoordinate : RTM_GeometricCoordinate):
		self.___geometricCoordinate = aGeometricCoordinate

	def __init__(self):
		super().__init__()
		self.___netElementRef : tRef = None
		# @AssociationType Common.tRef
		# """reference to a railway topology <netElement> element"""
		self.___intrinsicCoord : complex = None
		"""location on the <netElement> in normalized form (value in range 0..1)"""
		self.___applicationDirection : tApplicationDirection = None
		# @AssociationType schemas.3.1.tApplicationDirection
		# """direction in which the element is applied, related to the orientation of the <netElement>"""
		self.___pos : tLengthM = None
		# @AssociationType Common.tLengthM
		self.___linearCoordinate : RTM_LinearCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate
		# @AssociationMultiplicity 0..1
		self.___geometricCoordinate : RTM_GeometricCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate
		# @AssociationMultiplicity 0..1

