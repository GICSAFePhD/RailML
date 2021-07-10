#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import SwitchIL
from typing import List

class SwitchesIL(object):
	"""container for all switchIL elements"""
	def setSwitchIL(self, *aSwitchIL : SwitchIL*):
		self._switchIL = aSwitchIL

	def getSwitchIL(self) -> SwitchIL*:
		return self._switchIL

	def __init__(self):
		self._switchIL : SwitchIL = None
		# @AssociationType Interlocking.SwitchIL*
		# @AssociationMultiplicity 1..*
		# """The switch is a track asset where a train can change from one track to another. Here the functional aspects for interlocking operation are considered."""

