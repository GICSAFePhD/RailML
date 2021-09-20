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
	def GroupType(self, aGroupType : EntityILref):	# TODO *aGroupType
		self.___groupType = aGroupType
	@RefersToMember.setter
	def RefersToMember(self, aRefersToMember : EntityILref):
		self.___refersToMember = aRefersToMember

	def create_GroupType(self):
		self.GroupType = EntityILref.EntityILref()
	def create_RefersToMember(self):
		if self.RefersToMember == None:
			self.RefersToMember = []
		self.RefersToMember.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___groupType : EntityILref = None
		"""The reference to the IM specific element group type."""
		self.___refersToMember : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the member element within this group."""

