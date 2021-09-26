#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tGenericRouteTypeExt, EntityIL
from typing import List

class GenericRouteType(EntityIL.EntityIL):
	"""For train traffic control different types of routes are used. Each particular type has its IM specifics which are defined in the operational rules. Here the generic classification is done."""
	@property
	def GenericRouteType(self) -> tGenericRouteTypeExt:
		return self.___genericRouteType
	
	@GenericRouteType.setter
	def GenericRouteType(self, aGenericRouteType : tGenericRouteTypeExt):
		self.___genericRouteType = aGenericRouteType

	#def create_HasAspect(self):
#		self.HasAspect = tGenericRouteTypeExt.tGenericRouteTypeExt()
	
	def __init__(self):
		super().__init__()
		self.___genericRouteType : tGenericRouteTypeExt = None
		# @AssociationType Interlocking.tGenericRouteTypeExt
		# """The classification of the route types."""