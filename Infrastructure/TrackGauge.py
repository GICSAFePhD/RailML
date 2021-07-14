#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tLengthM import tLengthM
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class TrackGauge(FunctionalInfrastructureEntity):
	def setValue(self, aValue : tLengthM):
		self.___value = aValue

	def getValue(self) -> tLengthM:
		return self.___value

	def __init__(self):
		self.___value : tLengthM = None
		# @AssociationType Common.tLengthM
		# """the track gauge is the distance between the rails, in metres"""

