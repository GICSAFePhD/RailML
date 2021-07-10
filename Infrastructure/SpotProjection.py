#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import ProjectionCoordinate
from Infrastructure import ElementProjection
from typing import List

class SpotProjection(ElementProjection):
	def setCoordinate(self, aCoordinate : ProjectionCoordinate):
		self._coordinate = aCoordinate

	def getCoordinate(self) -> ProjectionCoordinate:
		return self._coordinate

	def __init__(self):
		self._coordinate : ProjectionCoordinate = None
		# @AssociationType Infrastructure.ProjectionCoordinate
		# @AssociationMultiplicity 1
		# """coordinate for spot projection (exact one)"""

