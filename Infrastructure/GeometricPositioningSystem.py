#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_NamedResource, RTM_PositioningSystem
from RailML.Common import Name
from RailML.Infrastructure import Validity
from typing import List

class GeometricPositioningSystem(RTM_PositioningSystem.RTM_PositioningSystem,RTM_NamedResource.RTM_NamedResource):
	@property
	def Name(self) -> Name:
		return self.___name
	@property
	def IsValid(self) -> Validity:
		return self.___isValid	

	@Name.setter
	def Name(self, aName : Name):
		self.___name = aName
	@IsValid.setter
	def IsValid(self, aIsValid : Validity):
		self.___isValid = aIsValid

	def create_Name(self):
		self.Name = Name.Name()
	def create_IsValid(self):
		self.IsValid = Validity.Validity()

	def __init__(self):
		self.___name : Name = None
		self.___isValid : Validity = None

