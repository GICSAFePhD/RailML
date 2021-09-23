#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tDescriptionLevel
from RailML.RailTopoModel import RTM_BaseObject
from typing import List

class RTM_LevelNetwork(RTM_BaseObject.RTM_BaseObject):
	@property
	def DescriptionLevel(self) -> tDescriptionLevel:
		return self.___descriptionLevel
	@property
	def NetworkResource(self) -> tElementWithIDref:
		return self.___networkResource

	@DescriptionLevel.setter
	def DescriptionLevel(self, aDescriptionLevel : tDescriptionLevel):
		self.___descriptionLevel = aDescriptionLevel
	@NetworkResource.setter
	def NetworkResource(self, aNetworkResource : tElementWithIDref):
		self.___networkResource = aNetworkResource

	def create_NetworkResource(self):
		if self.NetworkResource == None:
			self.NetworkResource = []
		self.NetworkResource.append(tElementWithIDref.tElementWithIDref())

	def __init__(self):
		super().__init__()
		self.___descriptionLevel : tDescriptionLevel = None
		# @AssociationType schemas.3.1.tDescriptionLevel
		self.___networkResource : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*