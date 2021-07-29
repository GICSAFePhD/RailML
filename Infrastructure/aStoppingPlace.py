#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.OpEquipment import PositiveInteger
from RailML.Common import tRef, tLengthM
from RailML.Infrastructure import tTrainRelation, StoppingPlace
from typing import List, NewType

Long = NewType("Long", int)
PositiveInteger = NewType("PositiveInteger", int)

class aStoppingPlace(object):
	@property
	def IsSignalized(self) -> Long:
		return self.___isSignalized
	@property
	def TrainRelation(self) -> tTrainRelation:
		return self.___trainRelation
	@property
	def PlatformEdgeRef(self) -> tRef:
		return self.___platformEdgeRef
	@property
	def TrainLength(self) -> tLengthM:
		return self.___trainLength
	@property
	def AxleCount(self) -> PositiveInteger:
		return self.___axleCount
	@property
	def WagonCount(self) -> PositiveInteger:
		return self.___wagonCount
	@property
	def VerbalConstraint(self) -> str:
		return self.___verbalConstraint
	@property
	def Unnamed_StoppingPlace(self) -> StoppingPlace:
		return self.___unnamed_StoppingPlace

	@IsSignalized.setter
	def IsSignalized(self, aIsSignalized : Long):
		self.___isSignalized = aIsSignalized
	@TrainRelation.setter
	def TrainRelation(self, aTrainRelation : tTrainRelation):
		self.___trainRelation = aTrainRelation
	@TrainLength.setter
	def TrainLength(self, aTrainLength : tRef):
		self.___platformEdgeRef = aTrainLength
	@TrainLength.setter
	def TrainLength(self, aTrainLength : tLengthM):
		self.___trainLength = aTrainLength
	@AxleCount.setter
	def AxleCount(self, aAxleCount : PositiveInteger):
		self.___axleCount = aAxleCount
	@WagonCount.setter
	def WagonCount(self, aWagonCount : PositiveInteger):
		self.___wagonCount = aWagonCount
	@VerbalConstraint.setter
	def VerbalConstraint(self, aVerbalConstraint : str):
		self.___verbalConstraint = aVerbalConstraint
	@Unnamed_StoppingPlace.setter
	def Unnamed_StoppingPlace(self, aUnnamed_StoppingPlace : StoppingPlace):
		self.___unnamed_StoppingPlace = aUnnamed_StoppingPlace

	def __init__(self):
		self.___isSignalized : Long = 0
		"""indicates whether the stopping place is marked by a signal or panel (true) or only in the "driver's timetable" (false)"""
		self.___trainRelation : tTrainRelation = tTrainRelation.tTrainRelation()
		# @AssociationType Infrastructure.tTrainRelation
		# """Reference to the part of the train from where on the stopping place is valid. Normally, a stopping place relates to the head of the train."""
		self.___platformEdgeRef : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# """reference to a platform edge for which the stopping place is relevant"""
		self.___trainLength : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """set this value if the stopping place is only valid for trains with a certain train length"""
		self.___axleCount : PositiveInteger = 0
		"""set this value if the stopping place is only valid for trains with a certain number of axles"""
		self.___wagonCount : PositiveInteger = 0
		"""set this value if the stopping place is only valid for trains with a certain number of wagons"""
		self.___verbalConstraint : str = ""
		"""set this value if the stopping place is only valid for trains fulfilling a certain verbal constraint"""
		self.___unnamed_StoppingPlace : StoppingPlace = StoppingPlace.StoppingPlace()

