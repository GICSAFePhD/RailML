#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import TvdSection
from typing import List

class TvdSections(object):
	"""container element for all TvdSection elements"""
	@property
	def TvdSection(self) -> TvdSection:
		return self.___tvdSection
	
	@TvdSection.setter
	def TvdSection(self, aTvdSection : TvdSection): # TODO *aTvdSection
		self.___tvdSection = aTvdSection

	def create_TvdSection(self):
		if self.TvdSection == None:
			self.TvdSection = []
		self.TvdSection.append(TvdSection.TvdSection())
	
	def __init__(self):
		self.___tvdSection : TvdSection = None
		# @AssociationType Interlocking.TvdSection*
		# @AssociationMultiplicity 1..*
		# """track vacancy detection (TVD) section reports train occupancy to the interlocking"""