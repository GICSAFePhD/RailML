#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tSectionVacancy
from Interlocking import EntityILref
from Interlocking import AssetAndState
from typing import List

class SectionAndVacancy(AssetAndState):
	"""Tuple of a track vacancy detection section and its state (occupied, vacant)"""
	def setInState(self, aInState : tSectionVacancy):
		self.___inState = aInState

	def getInState(self) -> tSectionVacancy:
		return self.___inState

	def setRefersToSection(self, aRefersToSection : EntityILref):
		self._refersToSection = aRefersToSection

	def getRefersToSection(self) -> EntityILref:
		return self._refersToSection

	def __init__(self):
		self.___inState : tSectionVacancy = None
		# @AssociationType Interlocking.tSectionVacancy
		# """The occupation status of the TVD section."""
		self._refersToSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the TVD section."""

