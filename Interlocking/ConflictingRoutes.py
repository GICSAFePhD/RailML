#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.ConflictingRoute import ConflictingRoute
from typing import List

class ConflictingRoutes(object):
	"""container element for all ConflictingRoute elements"""
	def setConflictingRoute(self, *aConflictingRoute : ConflictingRoute):
		self._conflictingRoute = aConflictingRoute

	def getConflictingRoute(self) -> ConflictingRoute:
		return self._conflictingRoute

	def __init__(self):
		self._conflictingRoute : ConflictingRoute = None
		# @AssociationType Interlocking.ConflictingRoute*
		# @AssociationMultiplicity 1..*
		# """identifies the routes that may never be simultaneously allocated"""

