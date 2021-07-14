#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.TvdSection import TvdSection
from typing import List

class TvdSections(object):
	"""container element for all TvdSection elements"""
	def setTvdSection(self, *aTvdSection : TvdSection):
		self._tvdSection = aTvdSection

	def getTvdSection(self) -> TvdSection:
		return self._tvdSection

	def __init__(self):
		self._tvdSection : TvdSection = None
		# @AssociationType Interlocking.TvdSection*
		# @AssociationMultiplicity 1..*
		# """track vacancy detection (TVD) section reports train occupancy to the interlocking"""

