#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tLengthM
from Infrastructure import FunctionalInfrastructureEntity
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

