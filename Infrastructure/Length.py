#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tLengthM
from Infrastructure import tLengthTypeExt
from Infrastructure import tExtendedDirection
from typing import List

class Length(object):
	def setValue(self, aValue : tLengthM):
		self.___value = aValue

	def getValue(self) -> tLengthM:
		return self.___value

	def setType(self, aType : tLengthTypeExt):
		self.___type = aType

	def getType(self) -> tLengthTypeExt:
		return self.___type

	def setValidForDirection(self, aValidForDirection : tExtendedDirection):
		self.___validForDirection = aValidForDirection

	def getValidForDirection(self) -> tExtendedDirection:
		return self.___validForDirection

	def __init__(self):
		self.___value : tLengthM = None
		# @AssociationType Common.tLengthM
		# """the distance value given in meters"""
		self.___type : tLengthTypeExt = None
		# @AssociationType Infrastructure.tLengthTypeExt
		# """type of length (operational, physical, administrative...)"""
		self.___validForDirection : tExtendedDirection = None
		# @AssociationType Infrastructure.tExtendedDirection
		# """indicate the direction for which the length information applies"""

