#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, ConflictReason, EntityIL
from typing import List

class ConflictingRoute(EntityIL.EntityIL):
	"""Iness definition:
	The route conflict table identifies the routes that may never be simultaneously allocated, due to utilisation of common track elements."""
	@property
	def RefersToRoute(self) -> EntityILref:
		return self.___refersToRoute
	@property
	def ConflictsWithRoute(self) -> EntityILref:
		return self.___conflictsWithRoute
	@property
	def ReasonForConflict(self) -> ConflictReason:
		return self.___reasonForConflict

	@RefersToRoute.setter
	def RefersToRoute(self, *aRefersToRoute : EntityILref):
		self.___refersToRoute = aRefersToRoute
	@ConflictsWithRoute.setter
	def ConflictsWithRoute(self, aConflictsWithRoute : EntityILref):
		self.___conflictsWithRoute = aConflictsWithRoute
	@ReasonForConflict.setter
	def ReasonForConflict(self, *aReasonForConflict : ConflictReason):
		self.___reasonForConflict = aReasonForConflict

	def __init__(self):
		self.___refersToRoute : EntityILref = EntityILref.EntityILref()
		"""The reference to the affected route."""
		self.___conflictsWithRoute : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the route causing the conflict."""
		self.___reasonForConflict : ConflictReason = ConflictReason.ConflictReason()
		# @AssociationType Interlocking.ConflictReason*
		# @AssociationMultiplicity 0..*
		# """Description of the reason for the conflict."""

