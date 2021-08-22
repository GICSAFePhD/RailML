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

	def create_ElectrificationSystem(self):
		if self.ElectrificationSystem == None:
			self.ElectrificationSystem = []
		self.ElectrificationSystem.append(ElectrificationSystem.ElectrificationSystem())
    
	def __init__(self):
		self.___electrificationSystem : ElectrificationSystem = None
		# @AssociationType Common.ElectrificationSystem*
		# @AssociationMultiplicity 1..*