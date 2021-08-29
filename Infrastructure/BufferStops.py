#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import BufferStop
from typing import List

class BufferStops(object):
	@property
	def BufferStop(self) -> BufferStop:
		return self.___bufferStop
	
	@BufferStop.setter
	def BufferStop(self, aBufferStop : BufferStop):
		self.___bufferStop = aBufferStop	

	def create_BufferStop(self):
		if self.BufferStop == None:
			self.BufferStop = []
		self.BufferStop.append(BufferStop.BufferStop())

	def __init__(self):
		self.___bufferStop : BufferStop = BufferStop.BufferStop()
		# @AssociationType Infrastructure.BufferStop*
		# @AssociationMultiplicity 1..*

