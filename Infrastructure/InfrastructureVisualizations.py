#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Visualization import Visualization
from typing import List

class InfrastructureVisualizations(object):
	def setVisualization(self, *aVisualization : Visualization):
		self._visualization = aVisualization

	def getVisualization(self) -> Visualization:
		return self._visualization

	def __init__(self):
		self._visualization : Visualization = None
		# @AssociationType Infrastructure.Visualization*
		# @AssociationMultiplicity 1..*
		# """visualization of (a part of) a railway infrastructure, e.g. on a screen or a schematic map"""

