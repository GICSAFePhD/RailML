#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.GenericTypes import GenericTypes
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class GenericIM(EntityIL):
	"""The container for the IM specific type definitions."""
	def setOwnsSetsOfAssets(self, *aOwnsSetsOfAssets : EntityILref):
		self._ownsSetsOfAssets = aOwnsSetsOfAssets

	def getOwnsSetsOfAssets(self) -> EntityILref:
		return self._ownsSetsOfAssets

	def setUsesTypes(self, aUsesTypes : GenericTypes):
		self._usesTypes = aUsesTypes

	def getUsesTypes(self) -> GenericTypes:
		return self._usesTypes

	def __init__(self):
		self._ownsSetsOfAssets : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the associated lists of assets."""
		self._usesTypes : GenericTypes = None
		# @AssociationType Interlocking.GenericTypes
		# @AssociationMultiplicity 1
		# """The types defined for this IM."""

