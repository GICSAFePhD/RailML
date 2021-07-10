#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import CombinedRoute
from typing import List

class Itineraries(object):
	"""container for all itinerary elements describing train paths through the network"""
	def setItinerary(self, *aItinerary : CombinedRoute*):
		self._itinerary = aItinerary

	def getItinerary(self) -> CombinedRoute*:
		return self._itinerary

	def __init__(self):
		self._itinerary : CombinedRoute = None
		# @AssociationType Interlocking.CombinedRoute*
		# @AssociationMultiplicity 1..*
		# """Itinerary is a combination of single routes defining the path from A to B independent of involved signalBoxes (interlockings)."""

