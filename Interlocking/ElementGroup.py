#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import EntityIL
from typing import List

class ElementGroup(EntityIL):
	"""For operational purpose of the interlocking some elements are grouped together. This allows e.g. commanding them with only one command."""
	def setGroupType(self, *aGroupType : EntityILref*):
		self._groupType = aGroupType

	def getGroupType(self) -> EntityILref*:
		return self._groupType

	def setRefersToMember(self, aRefersToMember : EntityILref):
		self._refersToMember = aRefersToMember

	def getRefersToMember(self) -> EntityILref:
		return self._refersToMember

	def __init__(self):
		self._groupType : EntityILref = None
		"""The reference to the IM specific element group type."""
		self._refersToMember : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the member element within this group."""

