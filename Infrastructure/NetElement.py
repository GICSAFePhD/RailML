#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('.')
from RailML.Common import tLengthM,Name
from RailML.Infrastructure import IsValid
from RailML.RailTopoModel import RTM_OrderedCollection, RTM_UnorderedCollection, RTM_PositioningNetElement, Relation,  AssociatedPositioningSystem
from typing import List

class NetElement(RTM_PositioningNetElement.RTM_PositioningNetElement):
	"""The NetElement type is derived from the RailTopoModel class PositioningNetElement."""
	@property
	def Length(self) -> tLengthM:
		return self.___length

	@Length.setter
	def Length(self, aLength : Length):
		self.___length = aLength

	def create_Length(self):
		self.Length = tLengthM.tLengthM()

	def __init__(self):
		super().__init__()
		self.___length : tLengthM = None
		# @AssociationType Common.tLengthM
		# """length of the NetElement in metres"""