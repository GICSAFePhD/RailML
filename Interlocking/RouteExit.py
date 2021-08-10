#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, EntityIL
from typing import List

class RouteExit(EntityIL.EntityIL):
	"""The exit signal or any other track asset that acts as route exit"""
	@property
	def RefersTo(self) -> EntityILref:
		return self.___refersTo
	@property
	def HasDangerPoint(self) -> EntityILref:
		return self.___hasDangerPoint
	@property
	def HasOverlap(self) -> EntityILref:
		return self.___hasOverlap

	@RefersTo.setter
	def RefersTo(self, aRefersTo : EntityILref):
		self.___refersTo = aRefersTo
	@HasDangerPoint.setter
	def HasDangerPoint(self, *aHasDangerPoint : EntityILref):
		self.___hasDangerPoint = aHasDangerPoint
	@HasOverlap.setter
	def HasOverlap(self, aHasOverlap : EntityILref):
		self.___hasOverlap = aHasOverlap

	def __init__(self):
		self.___refersTo : EntityILref = EntityILref.EntityILref()
		"""The reference to the track asset representing the destination point of the route. In most cases this is a signal or buffer stop."""
		self.___hasDangerPoint : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to any danger point related to this route end."""
		self.___hasOverlap : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to any overlap related to this route end."""

