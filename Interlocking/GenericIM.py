#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, GenericTypes, EntityIL
from typing import List

class GenericIM(EntityIL.EntityIL):
	"""The container for the IM specific type definitions."""
	@property
	def OwnsSetsOfAssets(self) -> EntityILref:
		return self.___ownsSetsOfAssets
	@property
	def UsesTypes(self) -> GenericTypes:
		return self.___usesTypes

	@OwnsSetsOfAssets.setter
	def OwnsSetsOfAssets(self, *aOwnsSetsOfAssets : EntityILref):
		self.___ownsSetsOfAssets = aOwnsSetsOfAssets
	@UsesTypes.setter
	def UsesTypes(self, aUsesTypes : GenericTypes):
		self.___usesTypes = aUsesTypes


	def __init__(self):
		self.___ownsSetsOfAssets : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the associated lists of assets."""
		self.___usesTypes : GenericTypes = GenericTypes.GenericTypes()
		# @AssociationType Interlocking.GenericTypes
		# @AssociationMultiplicity 1
		# """The types defined for this IM."""

