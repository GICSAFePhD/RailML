#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
from RailML.Infrastructure import RTM_PositioningNetElement
from typing import List

class NetElement(RTM_PositioningNetElement.RTM_PositioningNetElement):
	"""The NetElement type is derived from the RailTopoModel class PositioningNetElement."""
	@property
	def tLengthM(self) -> tLengthM:
		return self.___length
	
	@tLengthM.setter
	def tLengthM(self, atLengthM : tLengthM):
		self.___length = atLengthM

	def __init__(self):
		self.___length : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """length of the NetElement in metres"""

