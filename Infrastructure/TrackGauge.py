#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
from RailML.Infrastructure import FunctionalInfrastructureEntity
from typing import List

class TrackGauge(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def Value(self) -> tLengthM:
		return self.___value
	
	@Value.setter
	def Value(self, aValue : tLengthM):
		self.___value = aValue

	def __init__(self):
		self.___value : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """the track gauge is the distance between the rails, in metres"""

