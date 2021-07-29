#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import OpEquipment, OpOperations, FunctionalInfrastructureEntity
from typing import List

class OperationalPoint(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	"""The OperationalPoint defines a point in the railway network that is essential for railway operation. Typical examples for railway operational points are stations, block signals or stopping points. Operational points allow an interaction between the railway operator and the train driver."""
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def Timezone(self) -> str:
		return self.___timezone
	@property
	def InfrastructureManagerRef(self) -> tElementWithIDref:
		return self.___infrastructureManagerRef
	@property
	def ConnectedToLine(self) -> tElementWithIDref:
		return self.___connectedToLine
	@property
	def LimitedByBorder(self) -> tElementWithIDref:
		return self.___limitedByBorder
	@property
	def OpEquipment(self) -> OpEquipment:
		return self.___opEquipment
	@property
	def OpOperations(self) -> OpOperations:
		return self.___opOperations

	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@Timezone.setter
	def Timezone(self, aTimezone : str):
		self.___timezone = aTimezone
	@InfrastructureManagerRef.setter
	def InfrastructureManagerRef(self, aInfrastructureManagerRef : tElementWithIDref):
		self.___infrastructureManagerRef = aInfrastructureManagerRef
	@ConnectedToLine.setter
	def ConnectedToLine(self, aConnectedToLine : tElementWithIDref):
		self.___connectedToLine = aConnectedToLine
	@LimitedByBorder.setter
	def LimitedByBorder(self, aLimitedByBorder : tElementWithIDref):
		self.___limitedByBorder = aLimitedByBorder
	@OpEquipment.setter
	def OpEquipment(self, aOpEquipment : OpEquipment):
		self.___opEquipment = aOpEquipment
	@OpOperations.setter
	def OpOperations(self, aOpOperations : OpOperations):
		self.___opOperations = aOpOperations

	def __init__(self):
		self.___belongsToParent : tRef = tRef.tRef()
		"""references the one and only parent operational point of this operational point"""
		self.___basedOnTemplate : tRef = tRef.tRef()
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """references a generic operational point"""
		self.___timezone : str = ""
		"""the timezone of the operational point as defined in the tz database, e.g. "Europe/Berlin"""
		self.___infrastructureManagerRef : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		self.___connectedToLine : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a railway line (section) that is connected with this operational point"""
		self.___limitedByBorder : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a border element that delimits the operational point"""
		self.___opEquipment : OpEquipment = OpEquipment.OpEquipment()
		# @AssociationType Infrastructure.OpEquipment
		# @AssociationMultiplicity 0..1
		# """child element summarizing the equipment of the operational point"""
		self.___opOperations : OpOperations = OpOperations.OpOperations()
		# @AssociationType Infrastructure.OpOperations
		# @AssociationMultiplicity 0..1
		# """child element summarizing the operational aspects of the operational point"""

