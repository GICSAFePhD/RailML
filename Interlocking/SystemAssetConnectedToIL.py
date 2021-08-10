#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tExtentOfControl, EntityILref, EntityIL
from typing import List

class SystemAssetConnectedToIL(EntityIL.EntityIL):
	"""List of System Assets that are connected to a specific IL. These system assets are at least known to the interlocking."""
	@property
	def ExtentOfControl(self) -> tExtentOfControl:
		return self.___extentOfControl
	@property
	def ConnectedSystemAsset(self) -> EntityILref:
		return self.___connectedSystemAsset

	@ExtentOfControl.setter
	def ExtentOfControl(self, aExtentOfControl : tExtentOfControl):
		self.___extentOfControl = aExtentOfControl
	@ConnectedSystemAsset.setter
	def ConnectedSystemAsset(self, aConnectedSystemAsset : EntityILref):
		self.___connectedSystemAsset = aConnectedSystemAsset

	def __init__(self):
		self.___extentOfControl : tExtentOfControl = tExtentOfControl.tExtentOfControl()
		# @AssociationType Interlocking.tExtentOfControl
		# """The level of control of the asset by the interlocking."""
		self.___connectedSystemAsset : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the connected system asset."""