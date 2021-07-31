#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import ProjectionCoordinate, ElementProjection
from typing import List

class SpotProjection(ElementProjection.ElementProjection):
	@property
	def ProjectionCoordinate(self) -> ProjectionCoordinate:
		return self.___coordinate
	
	@ProjectionCoordinate.setter
	def ProjectionCoordinate(self, *aProjectionCoordinate : ProjectionCoordinate):
		self.___coordinate = aProjectionCoordinate

	def __init__(self):
		self.___coordinate : ProjectionCoordinate = ProjectionCoordinate.ProjectionCoordinate()
		# @AssociationType Infrastructure.ProjectionCoordinate
		# @AssociationMultiplicity 1
		# """coordinate for spot projection (exact one)"""

