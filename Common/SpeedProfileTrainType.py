#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tEtcsTrainCategoryNumber import tEtcsTrainCategoryNumber
from RailML.Common.tTrainType import tTrainType
from RailML.Common.tCantDeficiency import tCantDeficiency
from typing import List

class SpeedProfileTrainType(object):
	def setEtcsTrainCategoryNumber(self, aEtcsTrainCategoryNumber : tEtcsTrainCategoryNumber):
		self.___etcsTrainCategoryNumber = aEtcsTrainCategoryNumber

	def getEtcsTrainCategoryNumber(self) -> tEtcsTrainCategoryNumber:
		return self.___etcsTrainCategoryNumber

	def setType(self, aType : tTrainType):
		self.___type = aType

	def getType(self) -> tTrainType:
		return self.___type

	def setCantDeficiency(self, aCantDeficiency : tCantDeficiency):
		self.___cantDeficiency = aCantDeficiency

	def getCantDeficiency(self) -> tCantDeficiency:
		return self.___cantDeficiency

	def __init__(self):
		self.___etcsTrainCategoryNumber : tEtcsTrainCategoryNumber = None
		# @AssociationType Common.tEtcsTrainCategoryNumber
		self.___type : tTrainType = None
		# @AssociationType Common.tTrainType
		self.___cantDeficiency : tCantDeficiency = None
		# @AssociationType Common.tCantDeficiency

