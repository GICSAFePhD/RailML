#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import RouteReleaseGroupAhead
from typing import List

class RouteReleaseGroupsAhead(object):
	@property
	def RouteReleaseGroupAhead(self) -> RouteReleaseGroupAhead:
		return self.___routeReleaseGroupAhead
	
	@RouteReleaseGroupAhead.setter
	def RouteReleaseGroupAhead(self, aRouteReleaseGroupAhead : RouteReleaseGroupAhead): # TODO *aRouteReleaseGroupAhead
		self.___routeReleaseGroupAhead = aRouteReleaseGroupAhead

	def create_RouteReleaseGroupAhead(self):
		if self.RouteReleaseGroupAhead == None:
			self.RouteReleaseGroupAhead = []
		self.RouteReleaseGroupAhead.append(RouteReleaseGroupAhead.RouteReleaseGroupAhead())

	def __init__(self):
		self.___routeReleaseGroupAhead : RouteReleaseGroupAhead = None
		# @AssociationType Interlocking.RouteReleaseGroupAhead*
		# @AssociationMultiplicity 1..*
		# """One or more TVD sections as part of the route which can be released in a group ahead of the train in standstill."""