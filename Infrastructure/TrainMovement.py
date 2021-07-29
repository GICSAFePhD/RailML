#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tTrainMovementTypeExt
from typing import List

class TrainMovement(object):
	@property
	def Type(self) -> tTrainMovementTypeExt:
		return self.___type
	
	@Type.setter
	def Type(self, aType : tTrainMovementTypeExt):
		self.___type = aType

	def __init__(self):
		self.___type : tTrainMovementTypeExt = tTrainMovementTypeExt.tTrainMovementTypeExt()
		# @AssociationType Infrastructure.tTrainMovementTypeExt
		# """definition of train movement type for which the stopping place is valid"""

