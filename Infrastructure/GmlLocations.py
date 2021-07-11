#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import LineTypeCoordinate,PointTypeCoordinate
from typing import List

class GmlLocations(object):
	def setLineString(self, aLineString : LineTypeCoordinate):
		self._lineString = aLineString

	def getLineString(self) -> LineTypeCoordinate:
		return self._lineString

	def setPoint(self, aPoint : PointTypeCoordinate):
		self._point = aPoint

	def getPoint(self) -> PointTypeCoordinate:
		return self._point

	def __init__(self):
		self._lineString : LineTypeCoordinate = None
		# @AssociationType Infrastructure.LineTypeCoordinate*
		# @AssociationMultiplicity 0..*
		self._point : PointTypeCoordinate = None
		# @AssociationType Infrastructure.PointTypeCoordinate*
		# @AssociationMultiplicity 0..*

