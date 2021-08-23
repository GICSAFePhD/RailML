#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tNavigability, tUsage
from RailML.RailTopoModel import RTM_NetworkResource
from typing import List

class RTM_Relation(RTM_NetworkResource.RTM_NetworkResource):
	@property
	def Navigability(self) -> tNavigability:
		return self.___navigability
	@property
	def PositionOnA(self) -> tUsage:
		return self.___positionOnA
	@property
	def PositionOnB(self) -> tUsage:
		return self.___positionOnB
	@property
	def ElementA(self) -> tElementWithIDref:
		return self.___elementA
	@property
	def ElementB(self) -> tElementWithIDref:
		return self.___elementB

	@Navigability.setter
	def Navigability(self, aNavigability : tNavigability):
		self.___navigability = aNavigability
	@PositionOnA.setter
	def PositionOnA(self, aPositionOnA : tUsage):
		self.___positionOnA = aPositionOnA
	@PositionOnB.setter
	def PositionOnB(self, aPositionOnB : tUsage):
		self.___positionOnB = aPositionOnB
	@ElementA.setter
	def ElementA(self, aElementA : tElementWithIDref):
		self.___elementA = aElementA
	@ElementB.setter
	def ElementB(self, aElementB : tElementWithIDref):
		self.___elementB = aElementB

	def __init__(self):
		self.___navigability : tNavigability = None#tNavigability.tNavigability()
		# @AssociationType schemas.3.1.tNavigability
		self.___positionOnA : tUsage = None#tUsage.tUsage()
		self.___positionOnB : tUsage = None#tUsage.tUsage()
		# @AssociationType schemas.3.1.tUsage
		# @AssociationType schemas.3.1.tUsage
		self.___elementA : tElementWithIDref = None#tElementWithIDref.tElementWithIDref()
		self.___elementB : tElementWithIDref = None#tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 1
		# @AssociationType Common.tElementWithIDref
		# @AssociationMultiplicity 1

