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
	def ConflictingRoute(self, aConflictingRoute : ConflictingRoute):	# *aConflictingRoute
		self.___conflictingRoute = aConflictingRoute

	def create_ConflictingRoute(self):
		if self.ConflictingRoute == None:
			self.ConflictingRoute = []
		self.ConflictingRoute.append(ConflictingRoute.ConflictingRoute())

	def __init__(self):
		self.___conflictingRoute : ConflictingRoute = None
		# @AssociationType Interlocking.ConflictingRoute*
		# @AssociationMultiplicity 1..*
		# """identifies the routes that may never be simultaneously allocated"""