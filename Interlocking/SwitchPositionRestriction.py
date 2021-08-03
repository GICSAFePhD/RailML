#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tSwitchPosition, SwitchAndPosition, DerailerAndPosition, EntityIL
from typing import List

class SwitchPositionRestriction(EntityIL.EntityIL):
	"""For some relations between movable elements restrictions apply concerning the combination of both elements positions."""
	@property
	def tSwitchPosition(self) -> tSwitchPosition:
		return self.___restrictedPosition
	@property
	def SwitchAndPosition(self) -> SwitchAndPosition:
		return self.___relatedSwitchInPosition
	@property
	def DerailerAndPosition(self) -> DerailerAndPosition:
		return self.___relatedDerailerInPosition

	@tSwitchPosition.setter
	def tSwitchPosition(self, atSwitchPosition : tSwitchPosition):
		self.___restrictedPosition = atSwitchPosition
	@SwitchAndPosition.setter
	def SwitchAndPosition(self, aSwitchAndPosition : SwitchAndPosition):
		self.___relatedSwitchInPosition = aSwitchAndPosition
	@DerailerAndPosition.setter
	def DerailerAndPosition(self, aDerailerAndPosition : DerailerAndPosition):
		self.___relatedDerailerInPosition = aDerailerAndPosition

	def __init__(self):
		self.___restrictedPosition : tSwitchPosition = tSwitchPosition.tSwitchPosition()
		# @AssociationType Interlocking.tSwitchPosition
		# """This is the position which is needed when the other element has the named state/position."""
		self.___relatedSwitchInPosition : SwitchAndPosition = SwitchAndPosition.SwitchAndPosition()
		# @AssociationType Interlocking.SwitchAndPosition
		# @AssociationMultiplicity 0..1
		# """This is the reference and the state/position of the other switch of the relation."""
		self.___relatedDerailerInPosition : DerailerAndPosition = DerailerAndPosition.DerailerAndPosition()
		# @AssociationType Interlocking.DerailerAndPosition
		# @AssociationMultiplicity 0..1
		# """This is the reference and the state/position of the derailer of the relation."""

