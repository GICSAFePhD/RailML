#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import EntityIL
from typing import List

class RouteExit(EntityIL):
	"""The exit signal or any other track asset that acts as route exit"""
	def setRefersTo(self, aRefersTo : EntityILref):
		self._refersTo = aRefersTo

	def getRefersTo(self) -> EntityILref:
		return self._refersTo

	def setHasDangerPoint(self, *aHasDangerPoint : EntityILref*):
		self._hasDangerPoint = aHasDangerPoint

	def getHasDangerPoint(self) -> EntityILref*:
		return self._hasDangerPoint

	def setHasOverlap(self, aHasOverlap : EntityILref):
		self._hasOverlap = aHasOverlap

	def getHasOverlap(self) -> EntityILref:
		return self._hasOverlap

	def __init__(self):
		self._refersTo : EntityILref = None
		"""The reference to the track asset representing the destination point of the route. In most cases this is a signal or buffer stop."""
		self._hasDangerPoint : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to any danger point related to this route end."""
		self._hasOverlap : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to any overlap related to this route end."""

