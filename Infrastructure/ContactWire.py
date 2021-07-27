#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM
from typing import List

class ContactWire(object):
	@property
	def MinHeight(self) -> tLengthM:
		return self.___minHeight
	@property
	def MaxHeight(self) -> tLengthM:
		return self.___maxHeight
	@property
	def MaxDisplacement(self) -> tLengthM:
		return self.___maxDisplacement

	@MinHeight.setter
	def MinHeight(self, aMinHeight : tLengthM):
		self.___minHeight = aMinHeight
	@MaxHeight.setter
	def MaxHeight(self, aMaxHeight : tLengthM):
		self.___maxHeight = aMaxHeight
	@MaxDisplacement.setter
	def MaxDisplacement(self, aMaxDisplacement : tLengthM):
		self.___maxDisplacement = aMaxDisplacement

	def __init__(self):
		self.___minHeight : tLengthM = tLengthM.tLengthM()
		"""minimum height of contact wire above top of rail, in [m]"""
		self.___maxHeight : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """maximum height of contact wire above top of rail, in [m]"""
		self.___maxDisplacement : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """maximum lateral displacement of the contact wire from centre of track including stagger and wind forces, in [m]"""

