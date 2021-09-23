#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.RailTopoModel import IntrinsicCoordinate, RTM_BaseObject
from RailML.Infrastructure import IsValid
from typing import List

class AssociatedPositioningSystem(RTM_BaseObject.RTM_BaseObject):
	@property
	def PositioningSystemRef(self) -> tRef:
		return self.___positioningSystemRef
	@property
	def IntrinsicCoordinate(self) -> IntrinsicCoordinate:
		return self.___intrinsicCoordinate
	@property
	def IsValid(self) -> IsValid:
		return self.___isValid

	@PositioningSystemRef.setter
	def PositioningSystemRef(self, aPositioningSystemRef : tRef):
		self.___positioningSystemRef = aPositioningSystemRef
	@IntrinsicCoordinate.setter
	def IntrinsicCoordinate(self, aIntrinsicCoordinate : IntrinsicCoordinate):
		self.___intrinsicCoordinate = aIntrinsicCoordinate
	@IsValid.setter
	def IsValid(self, aIsValid : IsValid):
		self.___isValid = aIsValid

	def create_PositioningSystemRef(self):
		self.PositioningSystemRef = tRef.tRef()
	def create_IntrinsicCoordinate(self):
		if self.IntrinsicCoordinate == None:
			self.IntrinsicCoordinate = []
		self.IntrinsicCoordinate.append(IntrinsicCoordinate.IntrinsicCoordinate())
	def create_IsValid(self):
		if self.IsValid == None:
			self.IsValid = []
		self.IsValid.append(IsValid.IsValid())

	def __init__(self):
		self.___positioningSystemRef : tRef = None
		# @AssociationType Common.tRef
		self.___intrinsicCoordinate : IntrinsicCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_IntrinsicCoordinate*
		# @AssociationMultiplicity 1..*
		self.___isValid : IsValid = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 0..*