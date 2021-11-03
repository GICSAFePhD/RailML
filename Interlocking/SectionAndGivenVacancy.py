#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import AssetAndGivenState, SectionAndVacancy
from typing import List

class SectionAndGivenVacancy(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the TVD section and its state plus the level of enforcement"""
	@property
	def RelatedSectionAndVacancy(self) -> SectionAndVacancy:
		return self.___relatedSectionAndVacancy
	
	@RelatedSectionAndVacancy.setter
	def RelatedSectionAndVacancy(self, aRelatedSectionAndVacancy : SectionAndVacancy):
		self.___relatedSectionAndVacancy = aRelatedSectionAndVacancy

	def create_RelatedSectionAndVacancy(self):
		self.RelatedSectionAndVacancy = SectionAndVacancy.SectionAndVacancy()
    
	def __init__(self):
		super().__init__()
		self.___relatedSectionAndVacancy : SectionAndVacancy = None
		# @AssociationType Interlocking.SectionAndVacancy
		# @AssociationMultiplicity 1
		# """the tuple of references to the TVD section and its state plus the level of enforcement"""