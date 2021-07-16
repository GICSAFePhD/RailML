#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.ShuntingZone import ShuntingZone
from typing import List

class ShuntingZones(object):
	def setShuntingZone(self, *aShuntingZone : ShuntingZone):
		self._shuntingZone = aShuntingZone

	def getShuntingZone(self) -> ShuntingZone:
		return self._shuntingZone

	def __init__(self):
		self._shuntingZone : ShuntingZone = None
		# @AssociationType Interlocking.ShuntingZone*
		# @AssociationMultiplicity 1..*
		# """Simple zone defined for shunting movements."""

