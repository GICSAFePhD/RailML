#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.Route import Route
from typing import List

class Routes(object):
	"""container element for all Route elements"""
	def setRoute(self, *aRoute : Route):
		self._route = aRoute

	def getRoute(self) -> Route:
		return self._route

	def __init__(self):
		self._route : Route = None
		# @AssociationType Interlocking.Route*
		# @AssociationMultiplicity 1..*
		# """path for train movements in railway network secured by interlocking system"""

