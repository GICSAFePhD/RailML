#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tExtentOfControl import tExtentOfControl
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class SystemAssetConnectedToIL(EntityIL):
	"""List of System Assets that are connected to a specific IL. These system assets are at least known to the interlocking."""
	def setExtentOfControl(self, aExtentOfControl : tExtentOfControl):
		self.___extentOfControl = aExtentOfControl

	def getExtentOfControl(self) -> tExtentOfControl:
		return self.___extentOfControl

	def setConnectedSystemAsset(self, aConnectedSystemAsset : EntityILref):
		self._connectedSystemAsset = aConnectedSystemAsset

	def getConnectedSystemAsset(self) -> EntityILref:
		return self._connectedSystemAsset

	def __init__(self):
		self.___extentOfControl : tExtentOfControl = None
		# @AssociationType Interlocking.tExtentOfControl
		# """The level of control of the asset by the interlocking."""
		self._connectedSystemAsset : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the connected system asset."""

