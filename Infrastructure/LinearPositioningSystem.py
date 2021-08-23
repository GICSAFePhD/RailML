#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_LinearAnchorPoint, RTM_PositioningSystem, RTM_NamedResource
from RailML.Common import Name 
from RailML.Infrastructure import Validity, tLrsMethod
from typing import List

class LinearPositioningSystem(RTM_PositioningSystem.RTM_PositioningSystem,RTM_NamedResource.RTM_NamedResource):
	@property
	def LinearReferencingMethod(self) -> tLrsMethod:
		return self.___linearReferencingMethod
	@property
	def StartMeasure(self) -> complex:
		return self.___startMeasure
	@property
	def EndMeasure(self) -> complex:
		return self.___endMeasure
	@property
	def Units(self) -> str:
		return self.___units
	@property
	def RTM_LinearAnchorPoint(self) -> RTM_LinearAnchorPoint:
		return self.___anchor
	@property
	def Name(self) -> Name:
		return self.___name
	@property
	def IsValid(self) -> Validity:
		return self.___isValid	

	@LinearReferencingMethod.setter
	def LinearReferencingMethod(self, aLinearReferencingMethod : tLrsMethod):
		self.___linearReferencingMethod = aLinearReferencingMethod
	@StartMeasure.setter
	def StartMeasure(self, aStartMeasure : complex):
		self.___startMeasure = aStartMeasure
	@EndMeasure.setter
	def EndMeasure(self, aEndMeasure : complex):
		self.___endMeasure = aEndMeasure
	@Units.setter
	def Units(self, aUnits : str):
		self.___units = aUnits
	@RTM_LinearAnchorPoint.setter
	def RTM_LinearAnchorPoint(self, aRTM_LinearAnchorPoint : RTM_LinearAnchorPoint):
		self.___anchor = aRTM_LinearAnchorPoint
	@Name.setter
	def Name(self, aName : Name):
		self.___name = aName
	@IsValid.setter
	def IsValid(self, aIsValid : Validity):
		self.___isValid = aIsValid

	def __init__(self):
		self.___linearReferencingMethod : tLrsMethod = None#tLrsMethod.tLrsMethod()
		# @AssociationType schemas.3.1.tLrsMethod
		self.___startMeasure : complex = 0
		self.___endMeasure : complex = 0
		self.___units : str = ""
		"""use SI units (e.g. metres) whenever possible"""
		self.___anchor : RTM_LinearAnchorPoint = None#RTM_LinearAnchorPoint.RTM_LinearAnchorPoint()
		# @AssociationType Infrastructure.RTM.RTM_LinearAnchorPoint*
		# @AssociationMultiplicity 0..*
		self.___name : Name = None
		self.___isValid : Validity = None

