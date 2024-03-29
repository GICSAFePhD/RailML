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
		super().__init__()
		self.___value : tLengthM = None
		# @AssociationType Common.tLengthM
		# """the track gauge is the distance between the rails, in metres"""