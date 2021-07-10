#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import GenericDetector
from typing import List

class GenericDetectors(object):
	"""contains all GenericDetector elements"""
	def setGenericDetector(self, *aGenericDetector : GenericDetector*):
		self._genericDetector = aGenericDetector

	def getGenericDetector(self) -> GenericDetector*:
		return self._genericDetector

	def __init__(self):
		self._genericDetector : GenericDetector = None
		# @AssociationType Interlocking.GenericDetector*
		# @AssociationMultiplicity 1..*
		# """Device for detecting the exceeding of a particular characteristic."""

