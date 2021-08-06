#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tSectionVacancy, EntityILref, AssetAndState
from typing import List

class SectionAndVacancy(AssetAndState.AssetAndState):
	"""Tuple of a track vacancy detection section and its state (occupied, vacant)"""
	@property
	def InState(self) -> tSectionVacancy:
		return self.___inState
	@property
	def RefersToSection(self) -> EntityILref:
		return self.___refersToSection

	@InState.setter
	def InState(self, aInState : tSectionVacancy):
		self.___inState = aInState
	@RefersToSection.setter
	def RefersToSection(self, aRefersToSection : EntityILref):
		self.___refersToSection = aRefersToSection

	def __init__(self):
		self.___inState : tSectionVacancy = tSectionVacancy.tSectionVacancy()
		# @AssociationType Interlocking.tSectionVacancy
		# """The occupation status of the TVD section."""
		self.___refersToSection : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the TVD section."""

