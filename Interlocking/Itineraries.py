#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import CombinedRoute
from typing import List

class Itineraries(object):
	"""container for all itinerary elements describing train paths through the network"""
	@property
	def Itinerary(self) -> CombinedRoute:
		return self.___itinerary
	
	@Itinerary.setter
	def Itinerary(self, *aItinerary : CombinedRoute):
		self.___itinerary = aItinerary

	def create_Itinerary(self):
		if self.Itinerary == None:
			self.Itinerary = []
		self.Itinerary.append(CombinedRoute.CombinedRoute())
	
	def __init__(self):
		self.___itinerary : CombinedRoute = None
		# @AssociationType Interlocking.CombinedRoute*
		# @AssociationMultiplicity 1..*
		# """Itinerary is a combination of single routes defining the path from A to B independent of involved signalBoxes (interlockings)."""