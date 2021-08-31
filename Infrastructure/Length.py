#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
from RailML.Infrastructure import tLengthTypeExt, tExtendedDirection
from typing import List

class Length(object):
	@property
	def Value(self) -> tLengthM:
		return self.___value
	@property
	def Type(self) -> tLengthTypeExt:
		return self.___type
	@property
	def ValidForDirection(self) -> tExtendedDirection:
		return self.___validForDirection

	@Value.setter
	def Value(self, aValue : tLengthM):
		self.___value = aValue
	@Type.setter
	def Type(self, aType : tLengthTypeExt):
		self.___type = aType
	@ValidForDirection.setter
	def ValidForDirection(self, aValidForDirection : tExtendedDirection):
		self.___validForDirection = aValidForDirection

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

