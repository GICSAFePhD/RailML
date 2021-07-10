#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tLengthM
from Infrastructure.RTM import RTM_PositioningNetElement
from typing import List

class NetElement(RTM_PositioningNetElement):
	"""The NetElement type is derived from the RailTopoModel class PositioningNetElement."""
	def setLength(self, aLength : tLengthM):
		self.___length = aLength

	def getLength(self) -> tLengthM:
		return self.___length

	def __init__(self):
		self.___length : tLengthM = None
		# @AssociationType Common.tLengthM
		# """length of the NetElement in metres"""

