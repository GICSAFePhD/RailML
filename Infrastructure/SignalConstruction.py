#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tLengthM
from Infrastructure import tWiderTrackPosition
from Infrastructure import tSignalConstructionType
from typing import List

class SignalConstruction(object):
	def setHeight(self, aHeight : tLengthM):
		self.___height = aHeight

	def getHeight(self) -> tLengthM:
		return self.___height

	def setPositionAtTrack(self, aPositionAtTrack : tWiderTrackPosition):
		self.___positionAtTrack = aPositionAtTrack

	def getPositionAtTrack(self) -> tWiderTrackPosition:
		return self.___positionAtTrack

	def setType(self, aType : tSignalConstructionType):
		self.___type = aType

	def getType(self) -> tSignalConstructionType:
		return self.___type

	def __init__(self):
		self.___height : tLengthM = None
		# @AssociationType Common.tLengthM
		# """height of the (physical) signal/panel, in [m]"""
		self.___positionAtTrack : tWiderTrackPosition = None
		# @AssociationType Infrastructure.tWiderTrackPosition
		# """position of the (physical) signal/panel in relation to the railway track where it belongs to and the signal/panel application direction"""
		self.___type : tSignalConstructionType = None
		# @AssociationType Infrastructure.tSignalConstructionType
		# """distinguish between light, form and virtual signals"""

