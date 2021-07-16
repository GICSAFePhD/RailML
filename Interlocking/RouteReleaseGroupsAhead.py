#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.RouteReleaseGroupAhead import RouteReleaseGroupAhead
from typing import List

class RouteReleaseGroupsAhead(object):
	def setRouteReleaseGroupAhead(self, *aRouteReleaseGroupAhead : RouteReleaseGroupAhead):
		self._routeReleaseGroupAhead = aRouteReleaseGroupAhead

	def getRouteReleaseGroupAhead(self) -> RouteReleaseGroupAhead:
		return self._routeReleaseGroupAhead

	def __init__(self):
		self._routeReleaseGroupAhead : RouteReleaseGroupAhead = None
		# @AssociationType Interlocking.RouteReleaseGroupAhead*
		# @AssociationMultiplicity 1..*
		# """One or more TVD sections as part of the route which can be released in a group ahead of the train in standstill."""

