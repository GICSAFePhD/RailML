#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import RouteRelation
from typing import List

class RouteRelations(object):
	"""container element for all RouteRelation elements"""
	@property
	def RouteRelation(self) -> RouteRelation:
		return self.___routeRelation
	
	@RouteRelation.setter
	def RouteRelation(self, aRouteRelation : RouteRelation):	# *aRouteRelation
		self.___routeRelation = aRouteRelation

	def create_RouteRelation(self):
		if self.RouteRelation == None:
			self.RouteRelation = []
		self.RouteRelation.append(RouteRelation.RouteRelation())
	
	def __init__(self):
		self.___routeRelation : RouteRelation = None
		# @AssociationType Interlocking.RouteRelation*
		# @AssociationMultiplicity 1..*
		# """states the conditions that must be fulfilled for a given signal to be open"""