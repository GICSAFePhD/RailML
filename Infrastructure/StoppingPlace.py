#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import TrainMovement, FunctionalInfrastructureEntity, aStoppingPlace
from typing import List

class StoppingPlace(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def ValidForTrainMovement(self) -> TrainMovement:
		return self.___validForTrainMovement
	@property
	def aStoppingPlace(self) -> aStoppingPlace:
		return self.___unnamed_aStoppingPlace_

	@ValidForTrainMovement.setter
	def ValidForTrainMovement(self, aValidForTrainMovement : TrainMovement):
		self.___validForTrainMovement = aValidForTrainMovement
	@aStoppingPlace.setter
	def aStoppingPlace(self, aaStoppingPlace : aStoppingPlace):
		self.___unnamed_aStoppingPlace_ = aaStoppingPlace

	def __init__(self):
		self.___validForTrainMovement : TrainMovement = TrainMovement.TrainMovement()
		# @AssociationType Infrastructure.TrainMovement*
		# @AssociationMultiplicity 0..*
		# """specify the train movement types for which the stopping place is valid (freight trains, passenger trains, ...)"""
		#self.___unnamed_aStoppingPlace_ : aStoppingPlace = aStoppingPlace.aStoppingPlace()	#TODO CIRCULAR!

