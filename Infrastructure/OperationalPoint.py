#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.OpEquipment import OpEquipment
from RailML.Infrastructure.OpOperations import OpOperations
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class OperationalPoint(FunctionalInfrastructureEntity):
	"""The OperationalPoint defines a point in the railway network that is essential for railway operation. Typical examples for railway operational points are stations, block signals or stopping points. Operational points allow an interaction between the railway operator and the train driver."""
	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def setTimezone(self, aTimezone : str):
		self.___timezone = aTimezone

	def getTimezone(self) -> str:
		return self.___timezone

	def setInfrastructureManagerRef(self, *aInfrastructureManagerRef : tElementWithIDref):
		self._infrastructureManagerRef = aInfrastructureManagerRef

	def getInfrastructureManagerRef(self) -> tElementWithIDref:
		return self._infrastructureManagerRef

	def setConnectedToLine(self, *aConnectedToLine : tElementWithIDref):
		self._connectedToLine = aConnectedToLine

	def getConnectedToLine(self) -> tElementWithIDref:
		return self._connectedToLine

	def setLimitedByBorder(self, *aLimitedByBorder : tElementWithIDref):
		self._limitedByBorder = aLimitedByBorder

	def getLimitedByBorder(self) -> tElementWithIDref:
		return self._limitedByBorder

	def setOpEquipment(self, aOpEquipment : OpEquipment):
		self._opEquipment = aOpEquipment

	def getOpEquipment(self) -> OpEquipment:
		return self._opEquipment

	def setOpOperations(self, aOpOperations : OpOperations):
		self._opOperations = aOpOperations

	def getOpOperations(self) -> OpOperations:
		return self._opOperations

	def __init__(self):
		self.___belongsToParent : tRef = None
		"""references the one and only parent operational point of this operational point"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """references a generic operational point"""
		self.___timezone : str = None
		"""the timezone of the operational point as defined in the tz database, e.g. "Europe/Berlin"""
		self._infrastructureManagerRef : tElementWithIDref = None
		self._connectedToLine : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a railway line (section) that is connected with this operational point"""
		self._limitedByBorder : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a border element that delimits the operational point"""
		self._opEquipment : OpEquipment = None
		# @AssociationType Infrastructure.OpEquipment
		# @AssociationMultiplicity 0..1
		# """child element summarizing the equipment of the operational point"""
		self._opOperations : OpOperations = None
		# @AssociationType Infrastructure.OpOperations
		# @AssociationMultiplicity 0..1
		# """child element summarizing the operational aspects of the operational point"""

