#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import LevelCrossingIL
from typing import List

class LevelCrossingsIL(object):
	"""container element for all LevelCrossingIL elements"""
	@property
	def LevelCrossingIL(self) -> LevelCrossingIL:
		return self.___levelCrossingIL
	
	@LevelCrossingIL.setter
	def LevelCrossingIL(self, *aLevelCrossingIL : LevelCrossingIL):
		self.___levelCrossingIL = aLevelCrossingIL

	def __init__(self):
		self.___levelCrossingIL : LevelCrossingIL = None
		# @AssociationType Interlocking.LevelCrossingIL*
		# @AssociationMultiplicity 1..*
		# """The level crossing is a track asset allowing road traffic to cross the railway track in a secure way on the same level. Here the functional aspects for interlocking operation are considered."""