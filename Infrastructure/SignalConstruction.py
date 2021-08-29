#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
from RailML.Infrastructure import tWiderTrackPosition, tSignalConstructionType
from typing import List

class SignalConstruction(object):
	@property
	def Height(self) -> tLengthM:
		return self.___height
	@property
	def PositionAtTrack(self) -> tWiderTrackPosition:
		return self.___positionAtTrack
	@property
	def Type(self) -> tSignalConstructionType:
		return self.___type

	@Height.setter
	def Height(self, aHeight : tLengthM):
		self.___height = aHeight
	@PositionAtTrack.setter
	def PositionAtTrack(self, aPositionAtTrack : tWiderTrackPosition):
		self.___positionAtTrack = aPositionAtTrack
	@Type.setter
	def Type(self, aType : tSignalConstructionType):
		self.___type = aType

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

