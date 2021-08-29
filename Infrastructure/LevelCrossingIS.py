#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.Infrastructure import tLevelCrossingObstacleDetection, tLevelCrossingActivation, tLevelCrossingSupervision, LevelCrossingProtection, XCrossing

from typing import List, NewType
Long = NewType("Long", int)

class LevelCrossingIS(XCrossing.XCrossing):
	@property
	def ObstacleDetection(self) -> tLevelCrossingObstacleDetection:
		return self.___obstacleDetection
	@property
	def OpensOnDemand(self) -> Long:
		return self.___opensOnDemand
	@property
	def Activation(self) -> tLevelCrossingActivation:
		return self.___activation
	@property
	def Supervision(self) -> tLevelCrossingSupervision:
		return self.___supervision
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def Protection(self) -> LevelCrossingProtection:
		return self.___protection

	@ObstacleDetection.setter
	def ObstacleDetection(self, aObstacleDetection : tLevelCrossingObstacleDetection):
		self.___obstacleDetection = aObstacleDetection
	@OpensOnDemand.setter
	def OpensOnDemand(self, aOpensOnDemand : Long):
		self.___opensOnDemand = aOpensOnDemand
	@Activation.setter
	def Activation(self, aActivation : tLevelCrossingActivation):
		self.___activation = aActivation
	@Supervision.setter
	def Supervision(self, aSupervision : tLevelCrossingSupervision):
		self.___supervision = aSupervision
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___belongsToParent = aBasedOnTemplate
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@Protection.setter
	def Protection(self, aProtection : LevelCrossingProtection):
		self.___protection = aProtection

	def __init__(self):
		self.___obstacleDetection : tLevelCrossingObstacleDetection = None
		# @AssociationType Infrastructure.tLevelCrossingObstacleDetection
		# """obstacle detection: automatic (technical system, e.g. radar) or manual (e.g. by operator);
		# missing attribute means that the information is not known"""
		self.___opensOnDemand : Long = 0
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
		self.___protection : LevelCrossingProtection = None
		# @AssociationType Infrastructure.LevelCrossingProtection
		# @AssociationMultiplicity 0..1
		# """summary of technical protection of the level crossing"""

