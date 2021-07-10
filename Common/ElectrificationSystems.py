#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import ElectrificationSystem
from typing import List

class ElectrificationSystems(object):
	def setElectrificationSystem(self, *aElectrificationSystem : ElectrificationSystem*):
		self._electrificationSystem = aElectrificationSystem

	def getElectrificationSystem(self) -> ElectrificationSystem*:
		return self._electrificationSystem

	def __init__(self):
		self._electrificationSystem : ElectrificationSystem = None
		# @AssociationType Common.ElectrificationSystem*
		# @AssociationMultiplicity 1..*

