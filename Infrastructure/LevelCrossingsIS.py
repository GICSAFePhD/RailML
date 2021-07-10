#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import LevelCrossingIS
from typing import List

class LevelCrossingsIS(object):
	def setLevelCrossingIS(self, *aLevelCrossingIS : LevelCrossingIS*):
		self._levelCrossingIS = aLevelCrossingIS

	def getLevelCrossingIS(self) -> LevelCrossingIS*:
		return self._levelCrossingIS

	def __init__(self):
		self._levelCrossingIS : LevelCrossingIS = None
		# @AssociationType Infrastructure.LevelCrossingIS*
		# @AssociationMultiplicity 1..*

