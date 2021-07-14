#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tBallastType import tBallastType
from RailML.Infrastructure.tSleepersType import tSleepersType
from RailML.Infrastructure.tJointsType import tJointsType
#from RailML.Infrastructure.TrackBed import TrackBed	#TODO CIRCULAR!
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
		#self._unnamed_TrackBed_ : TrackBed = None	#TODO CIRCULAR!

