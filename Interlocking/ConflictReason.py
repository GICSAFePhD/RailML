#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.Interlocking import tRouteConflictTypesExt, EntityIL
from typing import List

class ConflictReason(EntityIL.EntityIL):
	"""The list of applicable conflict reasons for this route pair."""
	@property
	def Origin(self) -> tRouteConflictTypesExt:
		return self.___origin
	@property
	def RefersTo(self) -> tRef:
		return self.___refersTo

	@Origin.setter
	def Origin(self, aOrigin : tRouteConflictTypesExt):
		self.___origin = aOrigin
	@RefersTo.setter
	def RefersTo(self, aRefersTo : tRef):
		self.___refersTo = aRefersTo

	def __init__(self):
		self.___origin : tRouteConflictTypesExt = tRouteConflictTypesExt.tRouteConflictTypesExt()
		# @AssociationType Interlocking.tRouteConflictTypesExt
		# """The type of route conflict."""
		self.___refersTo : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# """The reference to the track asset (movable element, TVD section or signal) causing the conflict."""

