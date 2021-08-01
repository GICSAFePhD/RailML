#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tGenericRouteTypeExt, EntityIL
from typing import List

class GenericRouteType(EntityIL.EntityIL):
	"""For train traffic control different types of routes are used. Each particular type has its IM specifics which are defined in the operational rules. Here the generic classification is done."""
	@property
	def tGenericRouteTypeExt(self) -> tGenericRouteTypeExt:
		return self.___genericRouteType
	
	@tGenericRouteTypeExt.setter
	def tGenericRouteTypeExt(self, atGenericRouteTypeExt : tGenericRouteTypeExt):
		self.___genericRouteType = atGenericRouteTypeExt

	def __init__(self):
		self.___genericRouteType : tGenericRouteTypeExt = tGenericRouteTypeExt.tGenericRouteTypeExt()
		# @AssociationType Interlocking.tGenericRouteTypeExt
		# """The classification of the route types."""

