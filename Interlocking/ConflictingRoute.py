#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.ConflictReason import ConflictReason
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class ConflictingRoute(EntityIL):
	"""Iness definition:
	The route conflict table identifies the routes that may never be simultaneously allocated, due to utilisation of common track elements."""
	def setRefersToRoute(self, *aRefersToRoute : EntityILref):
		self._refersToRoute = aRefersToRoute

	def getRefersToRoute(self) -> EntityILref:
		return self._refersToRoute

	def setConflictsWithRoute(self, aConflictsWithRoute : EntityILref):
		self._conflictsWithRoute = aConflictsWithRoute

	def getConflictsWithRoute(self) -> EntityILref:
		return self._conflictsWithRoute

	def setReasonForConflict(self, *aReasonForConflict : ConflictReason):
		self._reasonForConflict = aReasonForConflict

	def getReasonForConflict(self) -> ConflictReason:
		return self._reasonForConflict

	def __init__(self):
		self._refersToRoute : EntityILref = None
		"""The reference to the affected route."""
		self._conflictsWithRoute : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the route causing the conflict."""
		self._reasonForConflict : ConflictReason = None
		# @AssociationType Interlocking.ConflictReason*
		# @AssociationMultiplicity 0..*
		# """Description of the reason for the conflict."""

