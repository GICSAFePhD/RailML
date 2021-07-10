#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import ElectrificationSection
from typing import List

class Electrifications(object):
	"""umbrella element for all electrification elements"""
	def setElectrificationSection(self, *aElectrificationSection : ElectrificationSection*):
		self._electrificationSection = aElectrificationSection

	def getElectrificationSection(self) -> ElectrificationSection*:
		return self._electrificationSection

	def __init__(self):
		self._electrificationSection : ElectrificationSection = None
		# @AssociationType Infrastructure.ElectrificationSection*
		# @AssociationMultiplicity 1..*

