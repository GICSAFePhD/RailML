#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tGenericRouteTypeExt
from Interlocking import EntityIL
from typing import List

class GenericRouteType(EntityIL):
	"""For train traffic control different types of routes are used. Each particular type has its IM specifics which are defined in the operational rules. Here the generic classification is done."""
	def setGenericRouteType(self, aGenericRouteType : tGenericRouteTypeExt):
		self.___genericRouteType = aGenericRouteType

	def getGenericRouteType(self) -> tGenericRouteTypeExt:
		return self.___genericRouteType

	def __init__(self):
		self.___genericRouteType : tGenericRouteTypeExt = None
		# @AssociationType Interlocking.tGenericRouteTypeExt
		# """The classification of the route types."""

