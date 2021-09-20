#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tExtentOfControl, EntityILref,  EntityIL
from typing import List

class TrackAssetConnectedToIL(EntityIL.EntityIL):
	"""List of Track Assets that are connected to a specific IL. This list would typically be kept in one or more separate files. This approach allows the IM to split the assets under control of a specific interlocking into different areas. Each area would be allocated a list of Track Assets Connected to the IL. This supports for instance a scenario in which an interlocking is split into several smaller ones during a resignalling project."""
	@property
	def ExtentOfControl(self) -> tExtentOfControl:
		return self.___extentOfControl
	@property
	def ConnectedTrackAsset(self) -> EntityILref:
		return self.___connectedTrackAsset

	@ExtentOfControl.setter
	def ExtentOfControl(self, aExtentOfControl : tExtentOfControl):
		self.___extentOfControl = aExtentOfControl
	@ConnectedTrackAsset.setter
	def ConnectedTrackAsset(self, aConnectedTrackAsset : EntityILref):
		self.___connectedTrackAsset = aConnectedTrackAsset

	def create_ConnectedTrackAsset(self):
		if self.ConnectedTrackAsset == None:
			self.ConnectedTrackAsset = []
		self.ConnectedTrackAsset.append(EntityILref.EntityILref())
	
	def __init__(self):
		super().__init__()
		self.___extentOfControl : tExtentOfControl = None
		# @AssociationType Interlocking.tExtentOfControl
		# """The level of control of the asset by the interlocking."""
		self.___connectedTrackAsset : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the connected track asset."""

