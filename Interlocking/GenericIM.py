#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import GenericTypes
from Interlocking import EntityIL
from typing import List

class GenericIM(EntityIL):
	"""The container for the IM specific type definitions."""
	def setOwnsSetsOfAssets(self, *aOwnsSetsOfAssets : EntityILref*):
		self._ownsSetsOfAssets = aOwnsSetsOfAssets

	def getOwnsSetsOfAssets(self) -> EntityILref*:
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

