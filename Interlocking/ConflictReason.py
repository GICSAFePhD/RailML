#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tRouteConflictTypesExt
from Common import tRef
from Interlocking import EntityIL
from typing import List

class ConflictReason(EntityIL):
	"""The list of applicable conflict reasons for this route pair."""
	def setOrigin(self, aOrigin : tRouteConflictTypesExt):
		self.___origin = aOrigin

	def getOrigin(self) -> tRouteConflictTypesExt:
		return self.___origin

	def setRefersTo(self, aRefersTo : tRef):
		self.___refersTo = aRefersTo

	def getRefersTo(self) -> tRef:
		return self.___refersTo

	def __init__(self):
		self.___origin : tRouteConflictTypesExt = None
		# @AssociationType Interlocking.tRouteConflictTypesExt
		# """The type of route conflict."""
		self.___refersTo : tRef = None
		# @AssociationType Common.tRef
		# """The reference to the track asset (movable element, TVD section or signal) causing the conflict."""

