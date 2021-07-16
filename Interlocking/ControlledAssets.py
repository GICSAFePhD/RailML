#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.ControlledSignalBox import ControlledSignalBox
from RailML.Interlocking.SystemAssetConnectedToIL import SystemAssetConnectedToIL
from typing import List

class ControlledAssets(object):
	"""container for all references to signalboxes/interlockings and system assets controlled by this controller"""
	def setControlledInterlocking(self, *aControlledInterlocking : ControlledSignalBox):
		self._controlledInterlocking = aControlledInterlocking

	def getControlledInterlocking(self) -> ControlledSignalBox:
		return self._controlledInterlocking

	def setControlledSystemAsset(self, *aControlledSystemAsset : SystemAssetConnectedToIL):
		self._controlledSystemAsset = aControlledSystemAsset

	def getControlledSystemAsset(self) -> SystemAssetConnectedToIL:
		return self._controlledSystemAsset

	def __init__(self):
		self._controlledInterlocking : ControlledSignalBox = None
		# @AssociationType Interlocking.ControlledSignalBox*
		# @AssociationMultiplicity 1..*
		# """The reference to a signalBox (interlocking) controlled from this unit."""
		self._controlledSystemAsset : SystemAssetConnectedToIL = None
		# @AssociationType Interlocking.SystemAssetConnectedToIL*
		# @AssociationMultiplicity 0..*
		# """The reference to a system asset controlled from this unit. It shall not repeat system assets already controlled from a particular interlocking."""

