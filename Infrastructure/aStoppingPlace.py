#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tTrainRelation
from Common import tRef
from Common import tLengthM
from Infrastructure import StoppingPlace
from typing import List

class aStoppingPlace(object):
	def setIsSignalized(self, aIsSignalized : long):
		self.___isSignalized = aIsSignalized

	def getIsSignalized(self) -> long:
		return self.___isSignalized

	def setTrainRelation(self, aTrainRelation : tTrainRelation):
		self.___trainRelation = aTrainRelation

	def getTrainRelation(self) -> tTrainRelation:
		return self.___trainRelation

	def setPlatformEdgeRef(self, aPlatformEdgeRef : tRef):
		self.___platformEdgeRef = aPlatformEdgeRef

	def getPlatformEdgeRef(self) -> tRef:
		return self.___platformEdgeRef

	def setTrainLength(self, aTrainLength : tLengthM):
		self.___trainLength = aTrainLength

	def getTrainLength(self) -> tLengthM:
		return self.___trainLength

	def setAxleCount(self, aAxleCount : positiveInteger):
		self.___axleCount = aAxleCount

	def getAxleCount(self) -> positiveInteger:
		return self.___axleCount

	def setWagonCount(self, aWagonCount : positiveInteger):
		self.___wagonCount = aWagonCount

	def getWagonCount(self) -> positiveInteger:
		return self.___wagonCount

	def setVerbalConstraint(self, aVerbalConstraint : str):
		self.___verbalConstraint = aVerbalConstraint

	def getVerbalConstraint(self) -> str:
		return self.___verbalConstraint

	def __init__(self):
		self.___isSignalized : long = None
		"""indicates whether the stopping place is marked by a signal or panel (true) or only in the "driver's timetable" (false)"""
		self.___trainRelation : tTrainRelation = None
		# @AssociationType Infrastructure.tTrainRelation
		# """Reference to the part of the train from where on the stopping place is valid. Normally, a stopping place relates to the head of the train."""
		self.___platformEdgeRef : tRef = None
		# @AssociationType Common.tRef
		# """reference to a platform edge for which the stopping place is relevant"""
		self.___trainLength : tLengthM = None
		# @AssociationType Common.tLengthM
		# """set this value if the stopping place is only valid for trains with a certain train length"""
		self.___axleCount : positiveInteger = None
		"""set this value if the stopping place is only valid for trains with a certain number of axles"""
		self.___wagonCount : positiveInteger = None
		"""set this value if the stopping place is only valid for trains with a certain number of wagons"""
		self.___verbalConstraint : str = None
		"""set this value if the stopping place is only valid for trains fulfilling a certain verbal constraint"""
		self._unnamed_StoppingPlace_ : StoppingPlace = None

