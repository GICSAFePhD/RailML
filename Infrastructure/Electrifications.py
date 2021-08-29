#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import ElectrificationSection
from typing import List

class Electrifications(object):
	"""umbrella element for all electrification elements"""
	@property
	def ElectrificationSection(self) -> ElectrificationSection:
		return self.___electrificationSection
	
	@ElectrificationSection.setter
	def ElectrificationSection(self, aElectrificationSection : ElectrificationSection):
		self.___electrificationSection = aElectrificationSection

	def create_ElectrificationSection(self):
		if self.ElectrificationSection == None:
			self.ElectrificationSection = []
		self.ElectrificationSection.append(ElectrificationSection.ElectrificationSection())

	def __init__(self):
		self.___electrificationSection : ElectrificationSection = None
		# @AssociationType Infrastructure.ElectrificationSection*
		# @AssociationMultiplicity 1..*

