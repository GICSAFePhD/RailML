#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import RouteExit
from typing import List

class DestinationPoints(object):
	"""container element for all DestinationPoint elements
	The definition of destination points which are mainly route exits. This allows definition independent of routes."""
	def setDestinationPoint(self, *aDestinationPoint : RouteExit*):
		self._destinationPoint = aDestinationPoint

	def getDestinationPoint(self) -> RouteExit*:
		return self._destinationPoint

	def __init__(self):
		self._destinationPoint : RouteExit = None
		# @AssociationType Interlocking.RouteExit*
		# @AssociationMultiplicity 1..*
		# """destination point of a secured running path"""

