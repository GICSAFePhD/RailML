#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
#from RailML.Common import tRef
from RailML.RailTopoModel import RTM_GeometricCoordinate,RTM_LinearCoordinate
from typing import List, NewType

Long = NewType("Long", int)

class RTM_AssociatedNetElement(object):
	@property
	def IntrinsicCoordBegin(self) -> complex:
		return self.___intrinsicCoordBegin
	@property
	def IntrinsicCoordEnd(self) -> complex:
		return self.___intrinsicCoordEnd
	@property
	def KeepsOrientation(self) -> Long:
		return self.___keepsOrientation
	@property
	def Sequence(self) -> int:
		return self.___sequence
	@property
	def PosBegin(self) -> tLengthM:
		return self.___posBegin
	@property
	def PosEnd(self) -> tLengthM:
		return self.___posEnd
	@property
	def GeometricCoordinateBegin(self) -> RTM_GeometricCoordinate:
		return self.___geometricCoordinateBegin
	@property
	def LinearCoordinateBegin(self) -> RTM_LinearCoordinate:
		return self.___linearCoordinateBegin
	@property
	def GeometricCoordinateEnd(self) -> RTM_GeometricCoordinate:
		return self.___geometricCoordinateEnd
	@property
	def LinearCoordinateEnd(self) -> RTM_LinearCoordinate:
		return self.___linearCoordinateEnd

	@IntrinsicCoordBegin.setter
	def IntrinsicCoordBegin(self, aIntrinsicCoordBegin : complex):
		self.___intrinsicCoordBegin = aIntrinsicCoordBegin
	@IntrinsicCoordBegin.setter
	def IntrinsicCoordEnd(self, aIntrinsicCoordEnd : complex):
		self.___intrinsicCoordEnd = aIntrinsicCoordEnd
	@IntrinsicCoordBegin.setter
	def KeepsOrientation(self, aKeepsOrientation : Long):
		self.___keepsOrientation = aKeepsOrientation
	@IntrinsicCoordBegin.setter
	def Sequence(self, aSequence : int):
		self.___sequence = aSequence
	@IntrinsicCoordBegin.setter
	def PosBegin(self, aPosBegin : tLengthM):
		self.___posBegin = aPosBegin
	@IntrinsicCoordBegin.setter
	def PosEnd(self, aPosEnd : tLengthM):
		self.___posEnd = aPosEnd
	@IntrinsicCoordBegin.setter
	def GeometricCoordinateBegin(self, aGeometricCoordinateBegin : RTM_GeometricCoordinate):
		self.___geometricCoordinateBegin = aGeometricCoordinateBegin
	@IntrinsicCoordBegin.setter
	def LinearCoordinateBegin(self, aLinearCoordinateBegin : RTM_LinearCoordinate):
		self.___linearCoordinateBegin = aLinearCoordinateBegin
	@IntrinsicCoordBegin.setter
	def GeometricCoordinateEnd(self, aGeometricCoordinateEnd : RTM_GeometricCoordinate):
		self.___geometricCoordinateEnd = aGeometricCoordinateEnd
	@IntrinsicCoordBegin.setter
	def LinearCoordinateEnd(self, aLinearCoordinateEnd : RTM_LinearCoordinate):
		self.___linearCoordinateEnd = aLinearCoordinateEnd

	def create_GeometricCoordinateBegin(self):
		self.GeometricCoordinateBegin = RTM_GeometricCoordinate.RTM_GeometricCoordinate()
	def create_LinearCoordinateBegin(self):
		self.LinearCoordinateBegin = RTM_LinearCoordinate.RTM_LinearCoordinate()
	def create_GeometricCoordinateEnd(self):
		self.GeometricCoordinateEnd = RTM_GeometricCoordinate.RTM_GeometricCoordinate()
	def create_LinearCoordinateEnd(self):
		self.LinearCoordinateEnd = RTM_LinearCoordinate.RTM_LinearCoordinate()

	def __init__(self):
		#self.___netElementRef : tRef = None
		# @AssociationType Common.tRef
		self.___intrinsicCoordBegin : complex = None
		self.___intrinsicCoordEnd : complex = None
		self.___keepsOrientation : Long = None
		self.___sequence : int = None
		self.___posBegin : tLengthM = None
		self.___posEnd : tLengthM = None
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		self.___geometricCoordinateBegin : RTM_GeometricCoordinate = None
		self.___linearCoordinateBegin : RTM_LinearCoordinate = None
		self.___geometricCoordinateEnd : RTM_GeometricCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate
		# @AssociationMultiplicity 0..1
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate
		# @AssociationMultiplicity 0..1
		self.___linearCoordinateEnd : RTM_LinearCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate
		# @AssociationMultiplicity 0..1
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate
		# @AssociationMultiplicity 0..1

