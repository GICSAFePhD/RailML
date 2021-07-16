#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.CombinedRoute import CombinedRoute
from typing import List

class CombinedRoutes(object):
	"""container element for all CombinedRoute elements"""
	def setCombinedRoute(self, *aCombinedRoute : CombinedRoute):
		self._combinedRoute = aCombinedRoute

	def getCombinedRoute(self) -> CombinedRoute:
		return self._combinedRoute

	def __init__(self):
		self._combinedRoute : CombinedRoute = None
		# @AssociationType Interlocking.CombinedRoute*
		# @AssociationMultiplicity 1..*
		# """a concatenation of single routes providing a continuous path for traffic movement"""

