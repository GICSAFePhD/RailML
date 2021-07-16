#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.RouteRelation import RouteRelation
from typing import List

class RouteRelations(object):
	"""container element for all RouteRelation elements"""
	def setRouteRelation(self, *aRouteRelation : RouteRelation):
		self._routeRelation = aRouteRelation

	def getRouteRelation(self) -> RouteRelation:
		return self._routeRelation

	def __init__(self):
		self._routeRelation : RouteRelation = None
		# @AssociationType Interlocking.RouteRelation*
		# @AssociationMultiplicity 1..*
		# """states the conditions that must be fulfilled for a given signal to be open"""

