#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import RouteReleaseGroupRear
from typing import List

class RouteReleaseGroupsRear(object):
	@property
	def RouteReleaseGroupRear(self) -> RouteReleaseGroupRear:
		return self.___routeReleaseGroupRear
	
	@RouteReleaseGroupRear.setter
	def RouteReleaseGroupRear(self, aRouteReleaseGroupRear : RouteReleaseGroupRear):	# *aRouteReleaseGroupRear 
		self.___routeReleaseGroupRear = aRouteReleaseGroupRear

	def create_RouteReleaseGroupRear(self):
		if self.RouteReleaseGroupRear == None:
			self.RouteReleaseGroupRear = []
		self.RouteReleaseGroupRear.append(RouteReleaseGroupRear.RouteReleaseGroupRear())

	def __init__(self):
		self.___routeReleaseGroupRear : RouteReleaseGroupRear = None
		# @AssociationType Interlocking.RouteReleaseGroupRear*
		# @AssociationMultiplicity 1..*
		# """One or more TVD sections as part of the route which can be released in a group in rear of passing train."""