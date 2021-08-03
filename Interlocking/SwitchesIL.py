#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SwitchIL
from typing import List

class SwitchesIL(object):
	"""container for all switchIL elements"""
	@property
	def SwitchIL(self) -> SwitchIL:
		return self.___switchIL
	
	@SwitchIL.setter
	def SwitchIL(self, *aSwitchIL : SwitchIL):
		self.___switchIL = aSwitchIL

	def __init__(self):
		self.___switchIL : SwitchIL = SwitchIL.SwitchIL()
		# @AssociationType Interlocking.SwitchIL*
		# @AssociationMultiplicity 1..*
		# """The switch is a track asset where a train can change from one track to another. Here the functional aspects for interlocking operation are considered."""

