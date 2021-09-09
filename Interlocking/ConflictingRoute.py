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
	def RefersToRoute(self, aRefersToRoute : EntityILref):	# TODO *aRefersToRoute
		self.___refersToRoute = aRefersToRoute
	@ConflictsWithRoute.setter
	def ConflictsWithRoute(self, aConflictsWithRoute : EntityILref):
		self.___conflictsWithRoute = aConflictsWithRoute
	@ReasonForConflict.setter
	def ReasonForConflict(self, aReasonForConflict : ConflictReason):	# TODO *aReasonForConflict
		self.___reasonForConflict = aReasonForConflict

	def create_RefersToRoute(self):
		self.RefersToRoute = EntityILref.EntityILref()
	def create_ConflictsWithRoute(self):
		if self.ConflictsWithRoute == None:
			self.ConflictsWithRoute = []
		self.ConflictsWithRoute.append(EntityILref.EntityILref())
	def create_ReasonForConflict(self):
		if self.ReasonForConflict == None:
			self.ReasonForConflict = []
		self.ReasonForConflict.append(ConflictReason.ConflictReason())

	def __init__(self):
		super().__init__()
		self.___refersToRoute : EntityILref = None
		"""The reference to the affected route."""
		self.___conflictsWithRoute : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the route causing the conflict."""
		self.___reasonForConflict : ConflictReason = None
		# @AssociationType Interlocking.ConflictReason*
		# @AssociationMultiplicity 0..*
		# """Description of the reason for the conflict."""