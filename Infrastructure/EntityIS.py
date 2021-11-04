#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import anyAttribute
from RailML.Infrastructure import GmlLocations, LocationNetwork
from RailML.RailTopoModel import RTM_LocatedNetEntity
from typing import List

class EntityIS(RTM_LocatedNetEntity.RTM_LocatedNetEntity):
	"""An Entity is the base element for all railway related elements that can be geo-referenced and located on the railway network topology."""
	@property
	def GmlLocations(self) -> GmlLocations:
		return self.___gmlLocations
	@property
	def LocationNetwork(self) -> LocationNetwork:
		return self.___networkLocation
	@property
	def AnyAttribute(self) -> anyAttribute:
		return self.___unnamed_anyAttribute_
	@property
	def Unnamed_any(self) -> list:
		return self.___unnamed_any_

	@GmlLocations.setter
	def GmlLocations(self, aGmlLocations : GmlLocations):
		self.___gmlLocations = aGmlLocations
	@LocationNetwork.setter
	def LocationNetwork(self, aLocationNetwork : LocationNetwork):
		self.___networkLocation = aLocationNetwork
	@AnyAttribute.setter
	def AnyAttribute(self, aAnyAttribute : anyAttribute):
		self.___unnamed_anyAttribute_ = aAnyAttribute
	@Unnamed_any.setter
	def Unnamed_any(self, aUnnamed_any : list):
		self.___unnamed_any_ = aUnnamed_any

	def create_GmlLocations(self):
		if self.GmlLocations == None:
			self.GmlLocations = []
		self.GmlLocations.append(GmlLocations.GmlLocations())
	def create_LocationNetwork(self):
		if self.LocationNetwork == None:
			self.LocationNetwork = []
		self.LocationNetwork.append(LocationNetwork.LocationNetwork())
	
	def __init__(self):
		super().__init__()
		self.___gmlLocations : GmlLocations = None
		# @AssociationType Infrastructure.GmlLocations*
		# @AssociationMultiplicity 0..*
		self.___networkLocation : LocationNetwork = None
		# @AssociationType Infrastructure.LocationNetwork*
		# @AssociationMultiplicity 0..*
		self.___unnamed_anyAttribute_ : anyAttribute = None
		self.___unnamed_any_ = None
		"""# @AssociationMultiplicity 0..*"""