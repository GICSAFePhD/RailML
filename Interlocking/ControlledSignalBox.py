#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tExtentOfControl
from Interlocking import EntityILref
from Interlocking import EntityIL
from typing import List

class ControlledSignalBox(EntityIL):
	"""The control relation from the controller to a signalBox (interlocking)"""
	def setExtentOfControl(self, aExtentOfControl : tExtentOfControl):
		self.___extentOfControl = aExtentOfControl

	def getExtentOfControl(self) -> tExtentOfControl:
		return self.___extentOfControl

	def setConnectedSignalBox(self, aConnectedSignalBox : EntityILref):
		self._connectedSignalBox = aConnectedSignalBox

	def getConnectedSignalBox(self) -> EntityILref:
		return self._connectedSignalBox

	def __init__(self):
		self.___extentOfControl : tExtentOfControl = None
		# @AssociationType Interlocking.tExtentOfControl
		# """The control level"""
		self._connectedSignalBox : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the controlled signalBox"""

