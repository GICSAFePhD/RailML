#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import ProjectionCoordinate, ElementProjection
from typing import List

class LinearProjection(ElementProjection.ElementProjection):
	@property
	def ProjectionCoordinate(self) -> ProjectionCoordinate:
		return self.___coordinate
	
	@ProjectionCoordinate.setter
	def ProjectionCoordinate(self, *aProjectionCoordinate : ProjectionCoordinate):
		self.___coordinate = aProjectionCoordinate

	def __init__(self):
		self.___coordinate : ProjectionCoordinate = ProjectionCoordinate.ProjectionCoordinate()
		# @AssociationType Infrastructure.ProjectionCoordinate*
		# @AssociationMultiplicity 2..*
		# """coordinates for linear projection (min 2)"""

