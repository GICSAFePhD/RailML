#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tForceN import tForceN
from RailML.Infrastructure.tRSFireCategoryType import tRSFireCategoryType
from typing import List

class EnergyRollingstock(object):
	def setRequiresPowerLimitation(self, aRequiresPowerLimitation : int): #TODO DEFINED AS LONG
		self.___requiresPowerLimitation = aRequiresPowerLimitation

	def getRequiresPowerLimitation(self) -> int:	 #TODO DEFINED AS LONG
		return self.___requiresPowerLimitation

	def setPermittedStaticContactForce(self, aPermittedStaticContactForce : tForceN):
		self.___permittedStaticContactForce = aPermittedStaticContactForce

	def getPermittedStaticContactForce(self) -> tForceN:
		return self.___permittedStaticContactForce

	def setPermittedMaxContactForce(self, aPermittedMaxContactForce : tForceN):
		self.___permittedMaxContactForce = aPermittedMaxContactForce

	def getPermittedMaxContactForce(self) -> tForceN:
		return self.___permittedMaxContactForce

	def setRequiresAutomaticDroppingDevice(self, aRequiresAutomaticDroppingDevice : int): #TODO DEFINED AS LONG
		self.___requiresAutomaticDroppingDevice = aRequiresAutomaticDroppingDevice

	def getRequiresAutomaticDroppingDevice(self) -> int:	#TODO DEFINED AS LONG
		return self.___requiresAutomaticDroppingDevice

	def setRequiredFireCategory(self, aRequiredFireCategory : tRSFireCategoryType):
		self.___requiredFireCategory = aRequiredFireCategory

	def getRequiredFireCategory(self) -> tRSFireCategoryType:
		return self.___requiredFireCategory

	def __init__(self):
		self.___requiresPowerLimitation : long = None
		"""flag, whether a current or power limitation on board is required"""
		self.___permittedStaticContactForce : tForceN = None
		"""value of the permitted static contact force of the pantograph, in [N]"""
		self.___permittedMaxContactForce : tForceN = None
		# @AssociationType Common.tForceN
		# @AssociationType Common.tForceN
		# """value of the permitted maximum (dynamic) contact force of the pantograph, in [N]"""
		self.___requiresAutomaticDroppingDevice : long = None
		"""flag, whether an automatic dropping device at the pantographs is required"""
		self.___requiredFireCategory : tRSFireCategoryType = None
		# @AssociationType Infrastructure.tRSFireCategoryType
		# """information on the required fire category of the rolling stock"""

