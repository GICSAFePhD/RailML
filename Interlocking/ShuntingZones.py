#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import ShuntingZone
from typing import List

class ShuntingZones(object):
	@property
	def ShuntingZone(self) -> ShuntingZone:
		return self.___shuntingZone
	
	@ShuntingZone.setter
	def ShuntingZone(self, *aShuntingZone : ShuntingZone):
		self.___shuntingZone = aShuntingZone

	def __init__(self):
		self.___shuntingZone : ShuntingZone = None
		# @AssociationType Interlocking.ShuntingZone*
		# @AssociationMultiplicity 1..*
		# """Simple zone defined for shunting movements."""