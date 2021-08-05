#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import RouteReleaseGroupRear
from typing import List

class RouteReleaseGroupsRear(object):
	@property
	def RouteReleaseGroupRear(self) -> RouteReleaseGroupRear:
		return self.___routeReleaseGroupRear
	
	@RouteReleaseGroupRear.setter
	def RouteReleaseGroupRear(self, *aRouteReleaseGroupRear : RouteReleaseGroupRear):
		self.___routeReleaseGroupRear = aRouteReleaseGroupRear

	def __init__(self):
		self.___routeReleaseGroupRear : RouteReleaseGroupRear = RouteReleaseGroupRear.RouteReleaseGroupRear()
		# @AssociationType Interlocking.RouteReleaseGroupRear*
		# @AssociationMultiplicity 1..*
		# """One or more TVD sections as part of the route which can be released in a group in rear of passing train."""

