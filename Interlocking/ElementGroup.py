#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, EntityIL
from typing import List

class ElementGroup(EntityIL.EntityIL):
	"""For operational purpose of the interlocking some elements are grouped together. This allows e.g. commanding them with only one command."""
	@property
	def GroupType(self) -> EntityILref:
		return self.___groupType
	@property
	def RefersToMember(self) -> EntityILref:
		return self.___refersToMember

	@GroupType.setter
	def GroupType(self, *aGroupType : EntityILref):
		self.___groupType = aGroupType
	@RefersToMember.setter
	def RefersToMember(self, aRefersToMember : EntityILref):
		self.___refersToMember = aRefersToMember

	def __init__(self):
		self.___groupType : EntityILref = EntityILref.EntityILref()
		"""The reference to the IM specific element group type."""
		self.___refersToMember : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the member element within this group."""

