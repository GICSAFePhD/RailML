#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tLevelCrossingObstacleDetection import tLevelCrossingObstacleDetection
from RailML.Infrastructure.tLevelCrossingActivation import tLevelCrossingActivation
from RailML.Infrastructure.tLevelCrossingSupervision import tLevelCrossingSupervision
from RailML.Common.tRef import tRef
from RailML.Infrastructure.LevelCrossingProtection import LevelCrossingProtection
from RailML.Infrastructure.XCrossing import XCrossing
from typing import List

class LevelCrossingIS(XCrossing):
	def setObstacleDetection(self, aObstacleDetection : tLevelCrossingObstacleDetection):
		self.___obstacleDetection = aObstacleDetection

	def getObstacleDetection(self) -> tLevelCrossingObstacleDetection:
		return self.___obstacleDetection

	def setOpensOnDemand(self, aOpensOnDemand : int):	#TODO DEFINED AS LONG
		self.___opensOnDemand = aOpensOnDemand

	def getOpensOnDemand(self) -> int:	#TODO DEFINED AS LONG
		return self.___opensOnDemand

	def setActivation(self, aActivation : tLevelCrossingActivation):
		self.___activation = aActivation

	def getActivation(self) -> tLevelCrossingActivation:
		return self.___activation

	def setSupervision(self, aSupervision : tLevelCrossingSupervision):
		self.___supervision = aSupervision

	def getSupervision(self) -> tLevelCrossingSupervision:
		return self.___supervision

	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def setProtection(self, aProtection : LevelCrossingProtection):
		self._protection = aProtection

	def getProtection(self) -> LevelCrossingProtection:
		return self._protection

	def __init__(self):
		self.___obstacleDetection : tLevelCrossingObstacleDetection = None
		# @AssociationType Infrastructure.tLevelCrossingObstacleDetection
		# """obstacle detection: automatic (technical system, e.g. radar) or manual (e.g. by operator);
		# missing attribute means that the information is not known"""
		self.___opensOnDemand : int = None	 #TODO DEFINED AS LONG
		"""set TRUE if the level crossing is closed for road users by default and gates are only opened on demand;
		missing attribute means that the information is not known"""
		self.___activation : tLevelCrossingActivation = None
		# @AssociationType Infrastructure.tLevelCrossingActivation
		# """describes how the level crossing is being activated;
		# missing attribute means that the information is not known"""
		self.___supervision : tLevelCrossingSupervision = None
		# @AssociationType Infrastructure.tLevelCrossingSupervision
		# """describes how the state of the level crossing is being supervised;
		# missing attribute means that the information is not known"""
		self.___belongsToParent : tRef = None
		"""reference to the (one and only) parent level crossing"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a template level crossing"""
		self._protection : LevelCrossingProtection = None
		# @AssociationType Infrastructure.LevelCrossingProtection
		# @AssociationMultiplicity 0..1
		# """summary of technical protection of the level crossing"""

