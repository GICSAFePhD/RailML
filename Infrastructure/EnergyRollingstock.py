#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tForceN
from RailML.Infrastructure import tRSFireCategoryType
from typing import List, NewType
Long = NewType("Long", int)

class EnergyRollingstock(object):
	@property
	def RequiresPowerLimitation(self) -> Long:
		return self.___requiresPowerLimitation
	@property
	def PermittedStaticContactForce(self) -> tForceN:
		return self.___permittedStaticContactForce
	@property
	def PermittedMaxContactForce(self) -> tForceN:
		return self.___permittedMaxContactForce
	@property
	def RequiresAutomaticDroppingDevice(self) -> Long:
		return self.___requiresAutomaticDroppingDevice
	@property
	def RequiredFireCategory(self) -> tRSFireCategoryType:
		return self.___requiredFireCategory

	@RequiresPowerLimitation.setter
	def RequiresPowerLimitation(self, aRequiresPowerLimitation : Long):
		self.___requiresPowerLimitation = aRequiresPowerLimitation
	@PermittedStaticContactForce.setter
	def PermittedStaticContactForce(self, aGradientCurve : tForceN):
		self.___permittedStaticContactForce = aGradientCurve
	@PermittedMaxContactForce.setter
	def PermittedMaxContactForce(self, aPermittedMaxContactForce : tForceN):
		self.___permittedMaxContactForce = aPermittedMaxContactForce
	@RequiresAutomaticDroppingDevice.setter
	def RequiresAutomaticDroppingDevice(self, aRequiresAutomaticDroppingDevice : Long):
		self.___requiresAutomaticDroppingDevice = aRequiresAutomaticDroppingDevice
	@RequiredFireCategory.setter
	def RequiredFireCategory(self, aRequiredFireCategory : tRSFireCategoryType):
		self.___requiredFireCategory = aRequiredFireCategory

	def __init__(self):
		self.___requiresPowerLimitation : Long = 0
		"""flag, whether a current or power limitation on board is required"""
		self.___permittedStaticContactForce : tForceN = tForceN.tForceN()
		"""value of the permitted static contact force of the pantograph, in [N]"""
		self.___permittedMaxContactForce : tForceN = tForceN.tForceN()
		# @AssociationType Common.tForceN
		# @AssociationType Common.tForceN
		# """value of the permitted maximum (dynamic) contact force of the pantograph, in [N]"""
		self.___requiresAutomaticDroppingDevice : Long = 0
		"""flag, whether an automatic dropping device at the pantographs is required"""
		self.___requiredFireCategory : tRSFireCategoryType = tRSFireCategoryType.tRSFireCategoryType()
		# @AssociationType Infrastructure.tRSFireCategoryType
		# """information on the required fire category of the rolling stock"""

