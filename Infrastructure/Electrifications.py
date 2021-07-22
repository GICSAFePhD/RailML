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

	def __init__(self):
		self.___electrificationSection : ElectrificationSection = ElectrificationSection.ElectrificationSection()
		# @AssociationType Infrastructure.ElectrificationSection*
		# @AssociationMultiplicity 1..*

