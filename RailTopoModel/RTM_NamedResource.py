#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import Name
from RailML.RailTopoModel import RTM_BaseObject
from typing import List

class RTM_NamedResource(RTM_BaseObject.RTM_BaseObject):
	@property
	def Name(self) -> Name:
		return self.___name

	@Name.setter
	def Name(self, aName : Name):
		self.___name = aName

	def create_Name(self):
		if self.Name == None:
			self.Name = []
		self.Name.append(Name.Name())

	def __init__(self):
		super().__init__()
		self.___name : Name = None
		# @AssociationType Common.Name*
		# @AssociationMultiplicity 0..*

