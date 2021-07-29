#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import anyAttribute
from RailML.Infrastructure import GmlLocations, LocationNetwork, RTM_LocatedNetEntity
from typing import List

class EntityIS(RTM_LocatedNetEntity.RTM_LocatedNetEntity):
	"""An Entity is the base element for all railway related elements that can be geo-referenced and located on the railway network topology."""
	#__metaclass__ = ABCMeta
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

	def __init__(self):
		self.___gmlLocations : GmlLocations = GmlLocations.GmlLocations()
		# @AssociationType Infrastructure.GmlLocations*
		# @AssociationMultiplicity 0..*
		self.___networkLocation : LocationNetwork = LocationNetwork.LocationNetwork()
		# @AssociationType Infrastructure.LocationNetwork*
		# @AssociationMultiplicity 0..*
		self.___unnamed_anyAttribute_ : anyAttribute = None
		self.___unnamed_any_ = []
		"""# @AssociationMultiplicity 0..*"""

