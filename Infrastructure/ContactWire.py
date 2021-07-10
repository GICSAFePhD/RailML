#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tLengthM
from typing import List

class ContactWire(object):
	def setMinHeight(self, aMinHeight : tLengthM):
		self.___minHeight = aMinHeight

	def getMinHeight(self) -> tLengthM:
		return self.___minHeight

	def setMaxHeight(self, aMaxHeight : tLengthM):
		self.___maxHeight = aMaxHeight

	def getMaxHeight(self) -> tLengthM:
		return self.___maxHeight

	def setMaxDisplacement(self, aMaxDisplacement : tLengthM):
		self.___maxDisplacement = aMaxDisplacement

	def getMaxDisplacement(self) -> tLengthM:
		return self.___maxDisplacement

	def __init__(self):
		self.___minHeight : tLengthM = None
		"""minimum height of contact wire above top of rail, in [m]"""
		self.___maxHeight : tLengthM = None
		# @AssociationType Common.tLengthM
		# """maximum height of contact wire above top of rail, in [m]"""
		self.___maxDisplacement : tLengthM = None
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """maximum lateral displacement of the contact wire from centre of track including stagger and wind forces, in [m]"""

