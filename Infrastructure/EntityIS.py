#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Infrastructure import GmlLocations, LocationNetwork, RTM_LocatedNetEntity
from RailML.Common import anyAttribute
from typing import List

#class EntityIS(RTM_LocatedNetEntity): #TODO CON ESTA HERENCIA SE ROMPE
class EntityIS():
	"""An Entity is the base element for all railway related elements that can be geo-referenced and located on the railway network topology."""
	__metaclass__ = ABCMeta
	@classmethod
	def setGmlLocations(self, aGmlLocations : GmlLocations):
		self._gmlLocations = aGmlLocations

	@classmethod
	def getGmlLocations(self) -> GmlLocations:
		return self._gmlLocations

	@classmethod
	def setNetworkLocation(self, aNetworkLocation : LocationNetwork):
		self._networkLocation = aNetworkLocation

	@classmethod
	def getNetworkLocation(self) -> LocationNetwork:
		return self._networkLocation

	@classmethod
	def __init__(self):
		self._gmlLocations : GmlLocations = None
		# @AssociationType Infrastructure.GmlLocations*
		# @AssociationMultiplicity 0..*
		self._networkLocation : LocationNetwork = None
		# @AssociationType Infrastructure.LocationNetwork*
		# @AssociationMultiplicity 0..*
		self._unnamed_anyAttribute_ : anyAttribute = None
		self._unnamed_any_ = []
		"""# @AssociationMultiplicity 0..*"""

