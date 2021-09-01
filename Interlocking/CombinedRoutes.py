#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import CombinedRoute
from typing import List

class CombinedRoutes(object):
	"""container element for all CombinedRoute elements"""
	@property
	def CombinedRoute(self) -> CombinedRoute:
		return self.___combinedRoute
	
	@CombinedRoute.setter
	def CombinedRoute(self, *aCombinedRoute : CombinedRoute):
		self.___combinedRoute = aCombinedRoute

	def __init__(self):
		self.___combinedRoute : CombinedRoute = None
		# @AssociationType Interlocking.CombinedRoute*
		# @AssociationMultiplicity 1..*
		# """a concatenation of single routes providing a continuous path for traffic movement"""