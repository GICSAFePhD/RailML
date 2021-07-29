#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tBallastType, tSleepersType, tJointsType, TrackBed #TODO CIRCULAR!
from typing import List

class aTrackbed(object):
	@property
	def tBallastType(self) -> tBallastType:
		return self.___ballastType
	@property
	def RailType(self) -> str:
		return self.___railType
	@property
	def tSleepersType(self) -> tSleepersType:
		return self.___sleepersType
	@property
	def tJointsType(self) -> tJointsType:
		return self.___jointsType
	@property
	def TrackBed(self) -> TrackBed:
		return self.___unnamed_TrackBed

	@tBallastType.setter
	def tBallastType(self, atBallastType : tBallastType):
		self.___ballastType = atBallastType
	@RailType.setter
	def RailType(self, aRailType : str):
		self.___railType = aRailType
	@tSleepersType.setter
	def tSleepersType(self, atSleepersType : tSleepersType):
		self.___sleepersType = atSleepersType
	@tJointsType.setter
	def tJointsType(self, atJointsType : tJointsType):
		self.___jointsType = atJointsType
	@TrackBed.setter
	def TrackBed(self, aTrackBed : TrackBed):
		self.___unnamed_TrackBed = aTrackBed

	def __init__(self):
		self.___ballastType : tBallastType = tBallastType.tBallastType()
		# @AssociationType Infrastructure.tBallastType
		# """type of ballast"""
		self.___railType : str = ""
		"""type of installed rails"""
		self.___sleepersType : tSleepersType = tSleepersType.tSleepersType()
		# @AssociationType Infrastructure.tSleepersType
		# """type of sleepers"""
		self.___jointsType : tJointsType = tJointsType.tJointsType()
		# @AssociationType Infrastructure.tJointsType
		# """type of rail joints"""
		self.___unnamed_TrackBed : TrackBed = None	#TODO CIRCULAR!

