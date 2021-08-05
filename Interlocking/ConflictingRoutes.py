#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import ConflictingRoute
from typing import List

class ConflictingRoutes(object):
	"""container element for all ConflictingRoute elements"""
	@property
	def ConflictingRoute(self) -> ConflictingRoute:
		return self.___conflictingRoute
	
	@ConflictingRoute.setter
	def ConflictingRoute(self, *aConflictingRoute : ConflictingRoute):
		self.___conflictingRoute = aConflictingRoute

	def __init__(self):
		self.___conflictingRoute : ConflictingRoute = ConflictingRoute.ConflictingRoute()
		# @AssociationType Interlocking.ConflictingRoute*
		# @AssociationMultiplicity 1..*
		# """identifies the routes that may never be simultaneously allocated"""

