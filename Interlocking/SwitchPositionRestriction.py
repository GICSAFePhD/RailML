#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tSwitchPosition
from Interlocking import SwitchAndPosition
from Interlocking import DerailerAndPosition
from Interlocking import EntityIL
from typing import List

class SwitchPositionRestriction(EntityIL):
	"""For some relations between movable elements restrictions apply concerning the combination of both elements positions."""
	def setRestrictedPosition(self, aRestrictedPosition : tSwitchPosition):
		self.___restrictedPosition = aRestrictedPosition

	def getRestrictedPosition(self) -> tSwitchPosition:
		return self.___restrictedPosition

	def setRelatedSwitchInPosition(self, aRelatedSwitchInPosition : SwitchAndPosition):
		self._relatedSwitchInPosition = aRelatedSwitchInPosition

	def getRelatedSwitchInPosition(self) -> SwitchAndPosition:
		return self._relatedSwitchInPosition

	def setRelatedDerailerInPosition(self, aRelatedDerailerInPosition : DerailerAndPosition):
		self._relatedDerailerInPosition = aRelatedDerailerInPosition

	def getRelatedDerailerInPosition(self) -> DerailerAndPosition:
		return self._relatedDerailerInPosition

	def __init__(self):
		self.___restrictedPosition : tSwitchPosition = None
		# @AssociationType Interlocking.tSwitchPosition
		# """This is the position which is needed when the other element has the named state/position."""
		self._relatedSwitchInPosition : SwitchAndPosition = None
		# @AssociationType Interlocking.SwitchAndPosition
		# @AssociationMultiplicity 0..1
		# """This is the reference and the state/position of the other switch of the relation."""
		self._relatedDerailerInPosition : DerailerAndPosition = None
		# @AssociationType Interlocking.DerailerAndPosition
		# @AssociationMultiplicity 0..1
		# """This is the reference and the state/position of the derailer of the relation."""

