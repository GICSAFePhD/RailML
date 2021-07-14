#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.ProjectionCoordinate import ProjectionCoordinate
from RailML.Infrastructure.ElementProjection import ElementProjection
from typing import List

class AreaProjection(ElementProjection):
	def setCoordinate(self, *aCoordinate : ProjectionCoordinate):
		self._coordinate = aCoordinate

	def getCoordinate(self) -> ProjectionCoordinate:
		return self._coordinate

	def __init__(self):
		self._coordinate : ProjectionCoordinate = None
		# @AssociationType Infrastructure.ProjectionCoordinate*
		# @AssociationMultiplicity 3..*
		# """coordinates for area projection (min 3 whereas first and last coordinate have to be identical to close the polygon)"""

