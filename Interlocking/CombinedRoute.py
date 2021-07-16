#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class CombinedRoute(EntityIL):
	"""CombinedRoute is a concatenation of single routes providing a continuous path for traffic movement which the interlocking can activate by one action.
	As itinerary it is a list of routes describing the train path trough a network."""
	def setComboEntry(self, aComboEntry : EntityILref):
		self._comboEntry = aComboEntry

	def getComboEntry(self) -> EntityILref:
		return self._comboEntry

	def setComboExit(self, *aComboExit : EntityILref):
		self._comboExit = aComboExit

	def getComboExit(self) -> EntityILref:
		return self._comboExit

	def setContainsRoute(self, aContainsRoute : EntityILref):
		self._containsRoute = aContainsRoute

	def getContainsRoute(self) -> EntityILref:
		return self._containsRoute

	def __init__(self):
		self._comboEntry : EntityILref = None
		"""Reference to the entry/start of the combined route"""
		self._comboExit : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 1..*
		# """Reference to exit/destination of combined route"""
		self._containsRoute : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """Reference to a single route contained in the combined route"""

