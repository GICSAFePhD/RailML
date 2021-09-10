#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import Route
from typing import List

class Routes(object):
	"""container element for all Route elements"""
	@property
	def Route(self) -> Route:
		return self.___route
	
	@Route.setter
	def Route(self, aRoute : Route): # TODO *aRoute
		self.___route = aRoute

	def create_Route(self):
		if self.Route == None:
			self.Route = []
		self.Route.append(Route.Route())

	def __init__(self):
		self.___route : Route = None
		# @AssociationType Interlocking.Route*
		# @AssociationMultiplicity 1..*
		# """path for train movements in railway network secured by interlocking system"""