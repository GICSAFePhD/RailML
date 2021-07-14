#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tSide import tSide
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class DerailerIS(FunctionalInfrastructureEntity):
	def setDerailSide(self, aDerailSide : tSide):
		self.___derailSide = aDerailSide

	def getDerailSide(self) -> tSide:
		return self.___derailSide

	def __init__(self):
		self.___derailSide : tSide = None
		# @AssociationType Infrastructure.tSide
		# """the side to which the railway vehicle will be derailed in reference to the application direction of the derailer: possible values are left and right"""

