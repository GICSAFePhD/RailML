#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import SpeedProfileTilting
from Common import SpeedProfileLoad
from Common import SpeedProfileBraking
from Common import SpeedProfileTrainType
from Common import aSpeedProfile
from Common import tElementWithIDandName
from typing import List

class SpeedProfile(tElementWithIDandName):
	def setTilting(self, aTilting : SpeedProfileTilting):
		self._tilting = aTilting

	def getTilting(self) -> SpeedProfileTilting:
		return self._tilting

	def setLoad(self, aLoad : SpeedProfileLoad):
		self._load = aLoad

	def getLoad(self) -> SpeedProfileLoad:
		return self._load

	def setBraking(self, aBraking : SpeedProfileBraking):
		self._braking = aBraking

	def getBraking(self) -> SpeedProfileBraking:
		return self._braking

	def setTrainType(self, aTrainType : SpeedProfileTrainType):
		self._trainType = aTrainType

	def getTrainType(self) -> SpeedProfileTrainType:
		return self._trainType

	def __init__(self):
		self._tilting : SpeedProfileTilting = None
		# @AssociationType Common.SpeedProfileTilting
		# @AssociationMultiplicity 0..1
		self._load : SpeedProfileLoad = None
		# @AssociationType Common.SpeedProfileLoad
		# @AssociationMultiplicity 0..1
		self._braking : SpeedProfileBraking = None
		# @AssociationType Common.SpeedProfileBraking
		# @AssociationMultiplicity 0..1
		self._trainType : SpeedProfileTrainType = None
		# @AssociationType Common.SpeedProfileTrainType
		# @AssociationMultiplicity 0..1
		self._unnamed_aSpeedProfile_ : aSpeedProfile = None

