#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
from RailML.Infrastructure import tLengthTypeExt, tExtendedDirection
from typing import List

class Length(object):
	@property
	def tLengthM(self) -> tLengthM:
		return self.___value
	@property
	def tLengthTypeExt(self) -> tLengthTypeExt:
		return self.___type
	@property
	def tExtendedDirection(self) -> tExtendedDirection:
		return self.___validForDirection

	@tLengthM.setter
	def tLengthM(self, atLengthM : tLengthM):
		self.___value = atLengthM
	@tLengthTypeExt.setter
	def tLengthTypeExt(self, atLengthTypeExt : tLengthTypeExt):
		self.___type = atLengthTypeExt
	@tExtendedDirection.setter
	def tExtendedDirection(self, atExtendedDirection : tExtendedDirection):
		self.___validForDirection = atExtendedDirection

	def __init__(self):
		self.___value : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """the distance value given in meters"""
		self.___type : tLengthTypeExt = tLengthTypeExt.tLengthTypeExt()
		# @AssociationType Infrastructure.tLengthTypeExt
		# """type of length (operational, physical, administrative...)"""
		self.___validForDirection : tExtendedDirection = tExtendedDirection.tExtendedDirection()
		# @AssociationType Infrastructure.tExtendedDirection
		# """indicate the direction for which the length information applies"""

