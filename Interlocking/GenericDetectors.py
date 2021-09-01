#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import GenericDetector
from typing import List

class GenericDetectors(object):
	"""contains all GenericDetector elements"""
	@property
	def GenericDetector(self) -> GenericDetector:
		return self.___genericDetector
	
	@GenericDetector.setter
	def GenericDetector(self, *aGenericDetector : GenericDetector):
		self.___genericDetector = aGenericDetector

	def __init__(self):
		self.___genericDetector : GenericDetector = None
		# @AssociationType Interlocking.GenericDetector*
		# @AssociationMultiplicity 1..*
		# """Device for detecting the exceeding of a particular characteristic."""