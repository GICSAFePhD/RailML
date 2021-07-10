#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import RouteReleaseGroupRear
from typing import List

class RouteReleaseGroupsRear(object):
	def setRouteReleaseGroupRear(self, *aRouteReleaseGroupRear : RouteReleaseGroupRear*):
		self._routeReleaseGroupRear = aRouteReleaseGroupRear

	def getRouteReleaseGroupRear(self) -> RouteReleaseGroupRear*:
		return self._routeReleaseGroupRear

	def __init__(self):
		self._routeReleaseGroupRear : RouteReleaseGroupRear = None
		# @AssociationType Interlocking.RouteReleaseGroupRear*
		# @AssociationMultiplicity 1..*
		# """One or more TVD sections as part of the route which can be released in a group in rear of passing train."""

