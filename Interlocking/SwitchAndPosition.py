#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tSwitchPosition
from Interlocking import EntityILref
from Interlocking import AssetAndState
from typing import List

class SwitchAndPosition(AssetAndState):
	"""A tuple (Switch, position). This refers to a switch and its position."""
	def setInPosition(self, aInPosition : tSwitchPosition):
		self.___inPosition = aInPosition

	def getInPosition(self) -> tSwitchPosition:
		return self.___inPosition

	def setRefersToSwitch(self, aRefersToSwitch : EntityILref):
		self._refersToSwitch = aRefersToSwitch

	def getRefersToSwitch(self) -> EntityILref:
		return self._refersToSwitch

	def __init__(self):
		self.___inPosition : tSwitchPosition = None
		# @AssociationType Interlocking.tSwitchPosition
		# """The position the switch is in."""
		self._refersToSwitch : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the switch."""

