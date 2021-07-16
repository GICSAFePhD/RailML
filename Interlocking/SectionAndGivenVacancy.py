#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from RailML.Interlocking.SectionAndGivenVacancy import SectionAndVacancy #TODO CIRCULAR!
from RailML.Interlocking.AssetAndGivenState import AssetAndGivenState
from typing import List

class SectionAndGivenVacancy(AssetAndGivenState):
	"""the tuple of references to the TVD section and its state plus the level of enforcement"""
	#def setRelatedSectionAndVacancy(self, aRelatedSectionAndVacancy : SectionAndVacancy): #TODO CIRCULAR!
	#	self._relatedSectionAndVacancy = aRelatedSectionAndVacancy

	#def getRelatedSectionAndVacancy(self) -> SectionAndVacancy:	#TODO CIRCULAR!
	#	return self._relatedSectionAndVacancy

	def __init__(self):
		#self._relatedSectionAndVacancy : SectionAndVacancy = None	#TODO CIRCULAR!
		# @AssociationType Interlocking.SectionAndVacancy
		# @AssociationMultiplicity 1
		# """the tuple of references to the TVD section and its state plus the level of enforcement"""
		pass #TODO CIRCULAR!
