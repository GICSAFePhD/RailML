#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, EntityIL
from typing import List

class CombinedRoute(EntityIL.EntityIL):
	"""CombinedRoute is a concatenation of single routes providing a continuous path for traffic movement which the interlocking can activate by one action.
	As itinerary it is a list of routes describing the train path trough a network."""
	@property
	def ComboEntry(self) -> EntityILref:
		return self.___comboEntry
	@property
	def ComboExit(self) -> EntityILref:
		return self.___comboExit
	@property
	def ContainsRoute(self) -> EntityILref:
		return self.___containsRoute

	@ComboEntry.setter
	def ComboEntry(self, aComboEntry : EntityILref):
		self.___comboEntry = aComboEntry
	@ComboExit.setter
	def ComboExit(self, *aComboExit : EntityILref):
		self.___comboExit = aComboExit
	@ContainsRoute.setter
	def ContainsRoute(self, aContainsRoute : EntityILref):
		self.___containsRoute = aContainsRoute

	def __init__(self):
		self.___comboEntry : EntityILref = EntityILref.EntityILref()
		"""Reference to the entry/start of the combined route"""
		self.___comboExit : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# """Reference to exit/destination of combined route"""
		self.___containsRoute : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """Reference to a single route contained in the combined route"""

