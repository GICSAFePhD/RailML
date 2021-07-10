#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import SectionAndVacancy
from Interlocking import AssetAndGivenState
from typing import List

class SectionAndGivenVacancy(AssetAndGivenState):
	"""the tuple of references to the TVD section and its state plus the level of enforcement"""
	def setRelatedSectionAndVacancy(self, aRelatedSectionAndVacancy : SectionAndVacancy):
		self._relatedSectionAndVacancy = aRelatedSectionAndVacancy

	def getRelatedSectionAndVacancy(self) -> SectionAndVacancy:
		return self._relatedSectionAndVacancy

	def __init__(self):
		self._relatedSectionAndVacancy : SectionAndVacancy = None
		# @AssociationType Interlocking.SectionAndVacancy
		# @AssociationMultiplicity 1
		# """the tuple of references to the TVD section and its state plus the level of enforcement"""

