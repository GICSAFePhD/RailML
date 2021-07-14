#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.TrainMovement import TrainMovement
#from RailML.Infrastructure.aStoppingPlace import aStoppingPlace	#TODO CIRCULAR!
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class StoppingPlace(FunctionalInfrastructureEntity):
	def setValidForTrainMovement(self, *aValidForTrainMovement : TrainMovement):
		self._validForTrainMovement = aValidForTrainMovement

	def getValidForTrainMovement(self) -> TrainMovement:
		return self._validForTrainMovement

	def __init__(self):
		self._validForTrainMovement : TrainMovement = None
		# @AssociationType Infrastructure.TrainMovement*
		# @AssociationMultiplicity 0..*
		# """specify the train movement types for which the stopping place is valid (freight trains, passenger trains, ...)"""
		#self._unnamed_aStoppingPlace_ : aStoppingPlace = None	#TODO CIRCULAR!

