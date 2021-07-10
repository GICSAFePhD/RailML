#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tTrainMovementTypeExt
from typing import List

class TrainMovement(object):
	def setType(self, aType : tTrainMovementTypeExt):
		self.___type = aType

	def getType(self) -> tTrainMovementTypeExt:
		return self.___type

	def __init__(self):
		self.___type : tTrainMovementTypeExt = None
		# @AssociationType Infrastructure.tTrainMovementTypeExt
		# """definition of train movement type for which the stopping place is valid"""

