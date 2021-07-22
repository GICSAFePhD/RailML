#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import LevelCrossingIS
from typing import List

class LevelCrossingsIS(object):
	@property
	def LevelCrossingIS(self) -> LevelCrossingIS:
		return self.___levelCrossingIS
	
	@LevelCrossingIS.setter
	def LevelCrossingIS(self, aLevelCrossingIS : LevelCrossingIS):
		self.___levelCrossingIS = aLevelCrossingIS

	def __init__(self):
		self.___levelCrossingIS : LevelCrossingIS = LevelCrossingIS.LevelCrossingIS()
		# @AssociationType Infrastructure.LevelCrossingIS*
		# @AssociationMultiplicity 1..*

