#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tBufferStopType, TrackNode
from typing import List

class BufferStop(TrackNode.TrackNode):
	@property
	def tBufferStopType(self) -> tBufferStopType:
		return self.___type
	
	@tBufferStopType.setter
	def tBufferStopType(self, atBufferStopType : tBufferStopType):
		self.___type = atBufferStopType

	def __init__(self):
		self.___type : tBufferStopType = None
		# @AssociationType Infrastructure.tBufferStopType
		# """type of the buffer stop"""

