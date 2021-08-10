#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import RouteExit
from typing import List

class DestinationPoints(object):
	"""container element for all DestinationPoint elements
	The definition of destination points which are mainly route exits. This allows definition independent of routes."""
	@property
	def DestinationPoint(self) -> RouteExit:
		return self.___destinationPoint
	
	@DestinationPoint.setter
	def DestinationPoint(self, *aDestinationPoint : RouteExit):
		self.___destinationPoint = aDestinationPoint

	def __init__(self):
		self.___destinationPoint : RouteExit = RouteExit.RouteExit()
		# @AssociationType Interlocking.RouteExit*
		# @AssociationMultiplicity 1..*
		# """destination point of a secured running path"""