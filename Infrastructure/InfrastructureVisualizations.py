#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Visualization
from typing import List

class InfrastructureVisualizations(object):
	@property
	def Visualization(self) -> Visualization:
		return self.___visualization
	
	@Visualization.setter
	def Visualization(self, aVisualization : Visualization): # TODO *aVisualization
		self.___visualization = aVisualization

	def create_Visualization(self):
		if self.Visualization == None:
			self.Visualization = []
		self.Visualization.append(Visualization.Visualization())

	def __init__(self):
		self.___visualization : Visualization = None
		# @AssociationType Infrastructure.Visualization*
		# @AssociationMultiplicity 1..*
		# """visualization of (a part of) a railway infrastructure, e.g. on a screen or a schematic map"""