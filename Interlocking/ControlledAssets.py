#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import ControlledSignalBox, SystemAssetConnectedToIL
from typing import List

class ControlledAssets(object):
	"""container for all references to signalboxes/interlockings and system assets controlled by this controller"""
	@property
	def ControlledSignalBox(self) -> ControlledSignalBox:
		return self.___controlledInterlocking
	@property
	def SystemAssetConnectedToIL(self) -> SystemAssetConnectedToIL:
		return self.___controlledSystemAsset

	@ControlledSignalBox.setter
	def ControlledSignalBox(self, aControlledSignalBox : ControlledSignalBox):	# TODO *aControlledSignalBox
		self.___controlledInterlocking = aControlledSignalBox
	@SystemAssetConnectedToIL.setter
	def SystemAssetConnectedToIL(self, aSystemAssetConnectedToIL : SystemAssetConnectedToIL):	# TODO *aSystemAssetConnectedToIL
		self.___controlledSystemAsset = aSystemAssetConnectedToIL

	def create_ControlledSignalBox(self):
		if self.ControlledSignalBox == None:
			self.ControlledSignalBox = []
		self.ControlledSignalBox.append(ControlledSignalBox.ControlledSignalBox())
	def create_SystemAssetConnectedToIL(self):
		if self.SystemAssetConnectedToIL == None:
			self.SystemAssetConnectedToIL = []
		self.SystemAssetConnectedToIL.append(SystemAssetConnectedToIL.SystemAssetConnectedToIL())

	def __init__(self):
		self.___controlledInterlocking : ControlledSignalBox = None
		# @AssociationType Interlocking.ControlledSignalBox*
		# @AssociationMultiplicity 1..*
		# """The reference to a signalBox (interlocking) controlled from this unit."""
		self.___controlledSystemAsset : SystemAssetConnectedToIL = None
		# @AssociationType Interlocking.SystemAssetConnectedToIL*
		# @AssociationMultiplicity 0..*
		# """The reference to a system asset controlled from this unit. It shall not repeat system assets already controlled from a particular interlocking."""