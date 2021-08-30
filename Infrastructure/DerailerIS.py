#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tSide, FunctionalInfrastructureEntity
from typing import List

class DerailerIS(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def DerailSide(self) -> tSide:
		return self.___derailSide
	
	@DerailSide.setter
	def DerailSide(self, atSide : tSide):
		self.___derailSide = atSide

	def create_DerailSide(self):
		self.DerailSide = tSide.tSide()
    
	def __init__(self):
		super().__init__()
		self.___derailSide : tSide = None
		# @AssociationType Infrastructure.tSide
		# """the side to which the railway vehicle will be derailed in reference to the application direction of the derailer: possible values are left and right"""

