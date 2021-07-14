#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tBufferStopType import tBufferStopType
from RailML.Infrastructure.TrackNode import TrackNode
from typing import List

class BufferStop(TrackNode):
	def setType(self, aType : tBufferStopType):
		self.___type = aType

	def getType(self) -> tBufferStopType:
		return self.___type

	def __init__(self):
		self.___type : tBufferStopType = None
		# @AssociationType Infrastructure.tBufferStopType
		# """type of the buffer stop"""

