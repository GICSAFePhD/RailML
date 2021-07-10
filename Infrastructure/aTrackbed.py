#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tBallastType
from Infrastructure import tSleepersType
from Infrastructure import tJointsType
from Infrastructure import TrackBed
from typing import List

class aTrackbed(object):
	def setBallastType(self, aBallastType : tBallastType):
		self.___ballastType = aBallastType

	def getBallastType(self) -> tBallastType:
		return self.___ballastType

	def setRailType(self, aRailType : str):
		self.___railType = aRailType

	def getRailType(self) -> str:
		return self.___railType

	def setSleepersType(self, aSleepersType : tSleepersType):
		self.___sleepersType = aSleepersType

	def getSleepersType(self) -> tSleepersType:
		return self.___sleepersType

	def setJointsType(self, aJointsType : tJointsType):
		self.___jointsType = aJointsType

	def getJointsType(self) -> tJointsType:
		return self.___jointsType

	def __init__(self):
		self.___ballastType : tBallastType = None
		# @AssociationType Infrastructure.tBallastType
		# """type of ballast"""
		self.___railType : str = None
		"""type of installed rails"""
		self.___sleepersType : tSleepersType = None
		# @AssociationType Infrastructure.tSleepersType
		# """type of sleepers"""
		self.___jointsType : tJointsType = None
		# @AssociationType Infrastructure.tJointsType
		# """type of rail joints"""
		self._unnamed_TrackBed_ : TrackBed = None

