#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import AssetAndGivenState, SectionAndVacancy
from typing import List

class SectionAndGivenVacancy(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the TVD section and its state plus the level of enforcement"""
	@property
	def SectionAndVacancy(self) -> SectionAndVacancy:
		return self.___relatedSectionAndVacancy
	
	@SectionAndVacancy.setter
	def SectionAndVacancy(self, aSectionAndVacancy : SectionAndVacancy):
		self.___relatedSectionAndVacancy = aSectionAndVacancy

	def __init__(self):
		self.___relatedSectionAndVacancy : SectionAndVacancy = SectionAndVacancy.SectionAndVacancy()
		# @AssociationType Interlocking.SectionAndVacancy
		# @AssociationMultiplicity 1
		# """the tuple of references to the TVD section and its state plus the level of enforcement"""
