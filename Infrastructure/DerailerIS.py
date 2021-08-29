#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tSide, FunctionalInfrastructureEntity
from typing import List

class DerailerIS(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def tSide(self) -> tSide:
		return self.___derailSide
	
	@tSide.setter
	def tSide(self, atSide : tSide):
		self.___derailSide = atSide

	def __init__(self):
		self.___derailSide : tSide = None
		# @AssociationType Infrastructure.tSide
		# """the side to which the railway vehicle will be derailed in reference to the application direction of the derailer: possible values are left and right"""

