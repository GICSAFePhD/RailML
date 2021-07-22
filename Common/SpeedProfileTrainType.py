#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tEtcsTrainCategoryNumber, tTrainType, tCantDeficiency
from typing import List

class SpeedProfileTrainType(object):
	@property
	def tEtcsTrainCategoryNumber(self) -> tEtcsTrainCategoryNumber:
		return self.___etcsTrainCategoryNumber
	@property
	def tTrainType(self) -> tTrainType:
		return self.___type
	@property
	def tCantDeficiency(self) -> tCantDeficiency:
		return self.___cantDeficiency

	@tEtcsTrainCategoryNumber.setter
	def tEtcsTrainCategoryNumber(self, atEtcsTrainCategoryNumber : tEtcsTrainCategoryNumber):
		self.___etcsTrainCategoryNumber = atEtcsTrainCategoryNumber
	@tTrainType.setter
	def tTrainType(self, atTrainType : tTrainType):
		self.___type = atTrainType
	@tCantDeficiency.setter
	def tCantDeficiency(self, atCantDeficiency : tCantDeficiency):
		self.___cantDeficiency = atCantDeficiency

	def __init__(self):
		self.___etcsTrainCategoryNumber : tEtcsTrainCategoryNumber = tEtcsTrainCategoryNumber.tEtcsTrainCategoryNumber()
		# @AssociationType Common.tEtcsTrainCategoryNumber
		self.___type : tTrainType = tTrainType.tTrainType()
		# @AssociationType Common.tTrainType
		self.___cantDeficiency : tCantDeficiency = tCantDeficiency.tCantDeficiency()
		# @AssociationType Common.tCantDeficiency

