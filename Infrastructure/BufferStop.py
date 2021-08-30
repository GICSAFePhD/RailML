#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tBufferStopType, TrackNode
from typing import List

class BufferStop(TrackNode.TrackNode):
	@property
	def Type(self) -> tBufferStopType:
		return self.___type
	
	@Type.setter
	def Type(self, aType : tBufferStopType):
		self.___type = aType

	def create_Type(self):
		self.Type = tBufferStopType.tBufferStopType()

	def __init__(self):
		super().__init__()
		self.___type : tBufferStopType = None
		# @AssociationType Infrastructure.tBufferStopType
		# """type of the buffer stop"""