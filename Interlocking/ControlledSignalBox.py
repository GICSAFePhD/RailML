#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tExtentOfControl, EntityILref, EntityIL
from typing import List

class ControlledSignalBox(EntityIL.EntityIL):
	"""The control relation from the controller to a signalBox (interlocking)"""
	@property
	def tExtentOfControl(self) -> tExtentOfControl:
		return self.___extentOfControl
	@property
	def ConnectedSignalBox(self) -> EntityILref:
		return self.___connectedSignalBox

	@tExtentOfControl.setter
	def tExtentOfControl(self, atExtentOfControl : tExtentOfControl):
		self.___extentOfControl = atExtentOfControl
	@ConnectedSignalBox.setter
	def ConnectedSignalBox(self, aConnectedSignalBox : EntityILref):
		self.___connectedSignalBox = aConnectedSignalBox

	def __init__(self):
		self.___extentOfControl : tExtentOfControl = tExtentOfControl.tExtentOfControl()
		# @AssociationType Interlocking.tExtentOfControl
		# """The control level"""
		self.___connectedSignalBox : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the controlled signalBox"""

