#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tExtentOfControl import tExtentOfControl
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class TrackAssetConnectedToIL(EntityIL):
	"""List of Track Assets that are connected to a specific IL. This list would typically be kept in one or more separate files. This approach allows the IM to split the assets under control of a specific interlocking into different areas. Each area would be allocated a list of Track Assets Connected to the IL. This supports for instance a scenario in which an interlocking is split into several smaller ones during a resignalling project."""
	def setExtentOfControl(self, aExtentOfControl : tExtentOfControl):
		self.___extentOfControl = aExtentOfControl

	def getExtentOfControl(self) -> tExtentOfControl:
		return self.___extentOfControl

	def setConnectedTrackAsset(self, aConnectedTrackAsset : EntityILref):
		self._connectedTrackAsset = aConnectedTrackAsset

	def getConnectedTrackAsset(self) -> EntityILref:
		return self._connectedTrackAsset

	def __init__(self):
		self.___extentOfControl : tExtentOfControl = None
		# @AssociationType Interlocking.tExtentOfControl
		# """The level of control of the asset by the interlocking."""
		self._connectedTrackAsset : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the connected track asset."""

