#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tSwitchPosition, EntityILref, AssetAndState
from typing import List

class SwitchAndPosition(AssetAndState.AssetAndState):
	"""A tuple (Switch, position). This refers to a switch and its position."""
	@property
	def InPosition(self) -> tSwitchPosition:
		return self.___inPosition
	@property
	def RefersToSwitch(self) -> EntityILref:
		return self.___refersToSwitch

	@InPosition.setter
	def InPosition(self, aInPosition : tSwitchPosition):
		self.___inPosition = aInPosition
	@RefersToSwitch.setter
	def RefersToSwitch(self, aRefersToSwitch : EntityILref):
		self.___refersToSwitch = aRefersToSwitch

	def __init__(self):
		super().__init__()
		self.___inPosition : tSwitchPosition = None
		# @AssociationType Interlocking.tSwitchPosition
		# """The position the switch is in."""
		self.___refersToSwitch : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the switch."""