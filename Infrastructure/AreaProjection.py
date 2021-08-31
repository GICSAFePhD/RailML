#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import ProjectionCoordinate, ElementProjection
from typing import List

class AreaProjection(ElementProjection.ElementProjection):
	@property
	def Coordinate(self) -> ProjectionCoordinate:
		return self.___coordinate
	
	@Coordinate.setter
	def Coordinate(self, aCoordinate : ProjectionCoordinate): # TODO *aCoordinate
		self.___coordinate = aCoordinate

	def create_Coordinate(self):
		if self.Coordinate == None:
			self.Coordinate = []
		self.Coordinate.append(ProjectionCoordinate.ProjectionCoordinate())

	def __init__(self):
		super().__init__()
		self.___coordinate : ProjectionCoordinate = None
		# @AssociationType Infrastructure.ProjectionCoordinate*
		# @AssociationMultiplicity 3..*
		# """coordinates for area projection (min 3 whereas first and last coordinate have to be identical to close the polygon)"""

