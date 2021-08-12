#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import ElectrificationSystem
from typing import List

class ElectrificationSystems(object):
	@property
	def ElectrificationSystem(self) -> ElectrificationSystem:
		return self.___electrificationSystem

	@ElectrificationSystem.setter
	def ElectrificationSystem(self, aElectrificationSystem : ElectrificationSystem):
		self.___electrificationSystem = aElectrificationSystem

	def createElectrificationSystem(self):
		self.ElectrificationSystem = ElectrificationSystem.ElectrificationSystem()
    
	def __init__(self):
		self.___electrificationSystem : ElectrificationSystem = None #ElectrificationSystem.ElectrificationSystem()
		# @AssociationType Common.ElectrificationSystem*
		# @AssociationMultiplicity 1..*