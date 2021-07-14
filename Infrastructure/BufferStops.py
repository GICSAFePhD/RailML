#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.BufferStop import BufferStop
from typing import List

class BufferStops(object):
	def setBufferStop(self, *aBufferStop : BufferStop):
		self._bufferStop = aBufferStop

	def getBufferStop(self) -> BufferStop:
		return self._bufferStop

	def __init__(self):
		self._bufferStop : BufferStop = None
		# @AssociationType Infrastructure.BufferStop*
		# @AssociationMultiplicity 1..*

